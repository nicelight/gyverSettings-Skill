---
title: GyverSettings-skill — артефакты для $skill-creator
updated: 2026-01-02
owner: tech
---

# Назначение
Краткий перечень файлов, которые нужно включить в пакет скилла. Все пути относительны `spec/gyversettings-skill/`.

# Основной пакет
- dist: `dist/gyver_settings_cheatsheet.md` (шпаргалка по Settings), `dist/gyver_settings_docs.md` (слитые доки).
- recipes: `recipes/new-project.md`, `recipes/refactor-checklist.md`, `recipes/debug-playbook.md`.
- templates: `templates/init_loop.cpp`, `templates/builder_widgets_advanced.cpp`, `templates/ota_fs.cpp`.
- playbooks: `playbooks/debug.md`, `playbooks/update.md`.
- deps: `deps/index.md`, `deps/cheatsheet_gyverdb.md`, `deps/cheatsheet_gyverhttp.md`, `deps/cheatsheet_bson_table.md`, `deps/cheatsheet_stringutils_gtl_streamio_stamp_table.md`, `deps/readme_set.md`.
- examples: `examples/libdeps_index.json`, `examples/libdeps_index.schema.md`; summaries/snippets по умолчанию из `examples/settings/summaries|snippets`, по запросу — `examples/deps/summaries|snippets`.
- обзор: `README.md`, `index.md`, `sources.yaml`.

# Служебные скрипты
- `scripts/refresh_gyversettings.py` — подтягивает доки/README из `sources.yaml`, собирает dist/cheatsheet и deps-конспекты.
- `scripts/index_libdeps_examples.py` — индексирует примеры из `.pio/libdeps/*/*/examples/**`, генерирует `examples/libdeps_index.*` и summaries/snippets (отдельно для Settings и deps).
