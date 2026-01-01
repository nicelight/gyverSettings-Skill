#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Индексация примеров из .pio/libdeps/*/*/examples/**.
Собирает метаданные (lib, version, env, example, path, flags, tags),
пишет examples/libdeps_index.json и генерирует summaries/snippets из примеров.
"""

from pathlib import Path
import json
import sys
import re

ROOT = Path(__file__).resolve().parents[4]
LIBDEPS = ROOT / ".pio" / "libdeps"
SPEC = ROOT / "spec" / "docs" / "gyversettings" / "examples"
INDEX = SPEC / "libdeps_index.json"


def parse_properties(path: Path) -> dict:
    data = {}
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            data[k.strip()] = v.strip()
    return data


def detect_tags(text: str) -> list:
    tags = set()
    if "SettingsGyverWS" in text or "ESPAsyncWebServer" in text:
        tags.add("ws")
    if "SettingsAsync" in text or "ESPAsyncWebServer" in text:
        tags.add("async")
    if "SettingsESP" in text:
        tags.add("esp-webserver")
    if "SettingsCamera" in text or "CAM" in text:
        tags.add("camera")
    if "LittleFS" in text or "SPIFFS" in text:
        tags.add("fs")
    if "OTA" in text or "beginOta" in text:
        tags.add("ota")
    if "Logger" in text or "Log" in text:
        tags.add("logger")
    if "Graph" in text or "Table" in text:
        tags.add("graphs")
    if "Settings" in text:
        tags.add("settings")
    return sorted(tags)


def find_primary_source(example_path: Path) -> Path | None:
    candidates = [
        example_path / "src" / "main.cpp",
        example_path / "main.cpp",
        example_path / "src" / "main.ino",
        example_path / "main.ino",
    ]
    for c in candidates:
        if c.exists():
            return c
    # fallback: первый .cpp/.ino в дереве
    files = list(example_path.rglob("*.cpp")) + list(example_path.rglob("*.ino"))
    return files[0] if files else None


def sanitize_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name)


def main() -> int:
    if not LIBDEPS.exists():
        print(f"Нет каталога libdeps: {LIBDEPS}", file=sys.stderr)
        return 1

    SPEC.mkdir(parents=True, exist_ok=True)
    # settings-only summaries/snippets
    (SPEC / "settings" / "summaries").mkdir(parents=True, exist_ok=True)
    (SPEC / "settings" / "snippets").mkdir(parents=True, exist_ok=True)
    # deps (по запросу)
    (SPEC / "deps" / "summaries").mkdir(parents=True, exist_ok=True)
    (SPEC / "deps" / "snippets").mkdir(parents=True, exist_ok=True)

    index = []

    for env_dir in sorted(LIBDEPS.iterdir()):
        if not env_dir.is_dir():
            continue
        env_name = env_dir.name
        for lib_dir in sorted(env_dir.iterdir()):
            if not lib_dir.is_dir():
                continue
            examples_dir = lib_dir / "examples"
            if not examples_dir.exists():
                continue

            props = parse_properties(lib_dir / "library.properties") if (lib_dir / "library.properties").exists() else {}
            lib_name = props.get("name", lib_dir.name)
            lib_ver = props.get("version", "")

            for example_root in sorted(p for p in examples_dir.iterdir() if p.is_dir()):
                example_name = example_root.name
                rel_path = example_root.relative_to(ROOT)

                has_ini = any(p.name == "platformio.ini" for p in example_root.rglob("platformio.ini"))
                has_src = any(p.suffix in (".cpp", ".ino", ".h") for p in example_root.rglob("*"))
                has_data = (example_root / "data").exists()

                primary = find_primary_source(example_root)
                is_settings = lib_name.lower().startswith("settings")
                base = SPEC / ("settings" if is_settings else "deps")
                snippet_path = base / "snippets" / f"{sanitize_name(lib_name)}_{sanitize_name(example_name)}.cpp"
                summary_path = base / "summaries" / f"{sanitize_name(lib_name)}_{sanitize_name(example_name)}.md"

                snippet_content = ""
                tags = []
                if primary:
                    text = primary.read_text(encoding="utf-8", errors="ignore")
                    tags = detect_tags(text)
                    snippet_content = text

                # summary
                summary_lines = [
                    f"# {lib_name} {lib_ver} / {example_name}",
                    f"- env: {env_name}",
                    f"- path: {rel_path.as_posix()}",
                    f"- primary: {primary.relative_to(example_root).as_posix() if primary else 'n/a'}",
                    f"- has_platformio_ini: {has_ini}",
                    f"- has_src: {has_src}",
                    f"- has_data: {has_data}",
                    f"- tags: {', '.join(tags) if tags else '-'}",
                    "",
                    "## Files",
                ]
                for p in sorted(example_root.rglob("*")):
                    if p.is_file():
                        summary_lines.append(f"- {p.relative_to(example_root).as_posix()}")
                summary_path.write_text("\n".join(summary_lines), encoding="utf-8")

                # snippet (limit size to avoid huge)
                if snippet_content:
                    snippet_path.write_text(snippet_content[:12000], encoding="utf-8")
                else:
                    snippet_path.write_text("// no primary source found\n", encoding="utf-8")

                index.append(
                    {
                        "lib": lib_name,
                        "version": lib_ver,
                        "env": env_name,
                        "example": example_name,
                        "path": rel_path.as_posix(),
                        "priority": "settings" if is_settings else "deps",
                        "has_platformio_ini": has_ini,
                        "has_src": has_src,
                        "has_data": has_data,
                        "tags": tags,
                    }
                )

    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Индекс записан: {INDEX} ({len(index)} примеров)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
