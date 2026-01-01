---
title: GyverSettings-skill — обзор артефактов
updated: 2026-01-01
---

# Структура и назначение

- `index.md` — короткий список разделов.
- `sources.yaml` — откуда брать исходные доки/README (Settings и зависимости) и локальные файлы проекта.

## dist/
- `gyver_settings_docs.md` — слитые доки Settings (8 файлов).
- `gyver_settings_cheatsheet.md` — выжимка API/flows (init, build/update, widgets, OTA, FS, logger, WS/Async/Camera, дефайны).

## recipes/
- Сценарии: `new-project.md`, `refactor-checklist.md`, `debug-playbook.md` и др.

## templates/
- Кодовые сниппеты: билдер/виджеты/DB binding, loop/tick, OTA hook, FS init и пр.

## playbooks/
- Чеклисты: отладка, обновление, релиз.

## deps/
- Шпаргалки по зависимостям: GyverDB, GyverHTTP, BSON/Table, утилиты (StringUtils/GTL/StreamIO/Stamp/Table), конспекты README.
- `index.md` — когда подтягивать какой файл.

## examples/
- `libdeps_index.json` — индекс примеров из `.pio/libdeps/*/<lib>/examples/**` (см. `examples/libdeps_index.schema.md`), поле `priority: settings|deps`.
- Settings (по умолчанию): `examples/settings/summaries/*.md`, `examples/settings/snippets/*.cpp`.
- Deps (по запросу): `examples/deps/summaries/*.md`, `examples/deps/snippets/*.cpp`.
- Примеры не копируются целиком: анализ по локальным файлам в `.pio/libdeps`.

## scripts/
- `scripts/index_libdeps_examples.(ps1|py)` — индексирует примеры, генерирует `libdeps_index.json`, summaries и snippets.
- `scripts/refresh_gyversettings.(ps1|py)` — тянет доки/README из sources.yaml, собирает dist/cheatsheet, генерирует recipes/templates/playbooks.
