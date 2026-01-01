---
title: GyverSettings-skill — runbook разработки
updated: 2026-01-02
owner: tech
---

# Цель
Собрать пакет артефактов для `$skill-creator` под скилл **GyverSettings-skill** (RU), который помогает разрабатывать/рефакторить/отлаживать проекты на библиотеке **Settings by AlexGyver** (ESP32/ESP8266, PlatformIO/Arduino) со всем кастомным стеком зависимостей.

# Архитектура (гибрид)
- Офлайн-готовый curated пакет (cheatsheet, dist-доки, recipes, templates, playbooks, deps, индекс примеров).
- Управляемое обновление артефактов скриптами: тянем доки/README из GitHub, индексируем локальные примеры в `.pio/libdeps`.
- ADR: `spec/adr/ADR-0001.md`.

# Что передать `$skill-creator`
- Название и назначение: `GyverSettings-skill` (RU) для разработки/рефакторинга/отладки Settings (ESP32/ESP8266, PlatformIO/Arduino) со стеком кастомных зависимостей.
- Список ресурсов: см. `spec/docs/ARTEFACTS.md` (пути относительны `spec/gyversettings-skill/`; включает dist/recipes/templates/playbooks/deps/examples + обзорные файлы).
- Служебные скрипты (обновление): `spec/gyversettings-skill/scripts/refresh_gyversettings.py`, `spec/gyversettings-skill/scripts/index_libdeps_examples.py`.
- Источники: `spec/gyversettings-skill/sources.yaml` (raw-доки Settings/README зависимостей, локальные файлы проекта для воспроизводимого обновления).

======== 

- Ресурсы (кратко, пути относительны `spec/gyversettings-skill/`):
  - dist: `dist/gyver_settings_cheatsheet.md`, `dist/gyver_settings_docs.md`.
  - recipes: `recipes/new-project.md`, `recipes/refactor-checklist.md`, `recipes/debug-playbook.md`.
  - templates: `templates/init_loop.cpp`, `templates/builder_widgets_advanced.cpp`, `templates/ota_fs.cpp`.
  - playbooks: `playbooks/debug.md`, `playbooks/update.md`.
  - deps: `deps/index.md`, `deps/cheatsheet_gyverdb.md`, `deps/cheatsheet_gyverhttp.md`, `deps/cheatsheet_bson_table.md`, `deps/cheatsheet_stringutils_gtl_streamio_stamp_table.md`, `deps/readme_set.md`.
  - examples: `examples/libdeps_index.json`, `examples/libdeps_index.schema.md`; summaries/snippets по умолчанию — `examples/settings/summaries|snippets`, по запросу для зависимостей — `examples/deps/summaries|snippets`.
  - обзор/структура: `README.md`, `index.md`.
- Скрипты (обновление артефактов):
  - `refresh_gyversettings.py` — тянет доки/README из `sources.yaml`, обновляет `dist/gyver_settings_docs.md` и `deps/readme_set.md` (PyYAML + requests).
  - `index_libdeps_examples.py` — индексирует `.pio/libdeps/*/*/examples/**`, генерирует `examples/libdeps_index.*` и summaries/snippets (Settings по умолчанию, deps по запросу).
- Источники: `sources.yaml` — raw-доки Settings (`docs/1.main.md … 8.custom.md`, README/README_EN), README зависимостей (GTL, GyverDB, StringUtils, GyverHTTP, BSON, Stamp, Table, StreamIO, FOR_MACRO, WiFiConnector), локальные файлы (`platformio.ini`, `.pio/libdeps/*`).

- Ожидаемое поведение скилла:
  - Базово грузить cheatsheet + релевантные recipes/templates/playbooks по типу запроса (new/refactor/debug/codegen).
  - По необходимости подмешивать deps-шпаргалки (GyverDB/HTTP/BSON/Table/утилиты).
  - Примеры использовать через `libdeps_index` + summaries/snippets (без подгрузки raw).
  - Обновление контента — по явному запуску скриптов из `scripts/`.
