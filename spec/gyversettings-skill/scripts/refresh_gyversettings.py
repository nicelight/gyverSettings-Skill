#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Обновление артефактов GyverSettings-skill:
- тянет доки Settings из GitHub (по sources.yaml) → dist/gyver_settings_docs.md
- собирает конспекты README зависимостей → deps/readme_set.md
"""

from pathlib import Path
import sys
import requests
import textwrap

try:
    import yaml
except ImportError:
    print("Не установлен PyYAML (pip install pyyaml)", file=sys.stderr)
    sys.exit(1)

SCRIPT_DIR = Path(__file__).resolve().parent
SPEC = SCRIPT_DIR.parent
SOURCES = SPEC / "sources.yaml"
DIST_DOCS = SPEC / "dist" / "gyver_settings_docs.md"
DEPS_README = SPEC / "deps" / "readme_set.md"


def fetch(url: str) -> str:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.text


def build_docs(settings_docs: dict) -> None:
    repo = settings_docs["repo"].rstrip("/")
    files = settings_docs["files"]
    parts = ["---", "title: Settings — слитые доки", "updated: auto", "---", ""]
    for fname in files:
        url = f"{repo}/{fname}"
        print(f"fetch {url}")
        try:
            txt = fetch(url)
        except Exception as e:
            print(f"warn: cannot fetch {url}: {e}", file=sys.stderr)
            continue
        parts.append(f"# {fname}")
        parts.append(txt.strip())
        parts.append("")
    DIST_DOCS.parent.mkdir(parents=True, exist_ok=True)
    DIST_DOCS.write_text("\n".join(parts), encoding="utf-8")
    print(f"written {DIST_DOCS}")


def build_deps_readme(deps_cfg: dict) -> None:
    repos = deps_cfg.get("repos", {})
    files = deps_cfg.get("files", ["README.md"])
    blocks = ["---", "title: README зависимостей — конспект", "updated: auto", "---", ""]
    for name, repo in repos.items():
        repo = repo.rstrip("/")
        content = None
        for fname in files:
            url = f"{repo}/{fname}"
            try:
                content = fetch(url)
                break
            except Exception:
                continue
        if not content:
            blocks.append(f"## {name}\n(не удалось скачать README)\n")
            continue
        snippet = "\n".join(content.splitlines()[:80])
        blocks.append(f"## {name}\n{snippet}\n")
    DEPS_README.parent.mkdir(parents=True, exist_ok=True)
    DEPS_README.write_text("\n".join(blocks), encoding="utf-8")
    print(f"written {DEPS_README}")


def main() -> int:
    if not SOURCES.exists():
        print(f"Нет sources.yaml: {SOURCES}", file=sys.stderr)
        return 1
    cfg = yaml.safe_load(SOURCES.read_text(encoding="utf-8"))
    settings_docs = cfg["sources"]["settings_docs"]
    deps_readme = cfg["sources"]["deps_readme"]

    build_docs(settings_docs)
    build_deps_readme(deps_readme)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
