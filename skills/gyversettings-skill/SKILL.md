---
name: gyversettings-skill
description: >
  Помощь в разработке, рефакторинге и отладке проектов на библиотеке Settings by AlexGyver
  (ESP32/ESP8266, PlatformIO/Arduino) со стэком кастомных зависимостей. Используй, когда нужно
  строить UI/бекенд Settings, работать с GyverDB/LittleFS/OTA/HTTP/WS, разбирать примеры или
  искать рецепты/шпаргалки по зависимостям.
---

# Быстрый старт
- Для типовых вопросов грузить `dist/gyver_settings_cheatsheet.md` + нужные recipes/templates/playbooks.
- При глубоком разборе — подключать `dist/gyver_settings_docs.md`.
- Примеры: по умолчанию использовать `examples/settings/summaries|snippets` и `examples/libdeps_index.json`; примеры зависимостей брать из `examples/deps/...` только по запросу.
- Зависимости: при вопросах про БД/HTTP/бинарные таблицы — открывать файлы из `deps/` (см. ниже).

# Навигация по ресурсам (references)
- dist: `dist/gyver_settings_cheatsheet.md`, `dist/gyver_settings_docs.md`.
- recipes: `recipes/new-project.md`, `recipes/refactor-checklist.md`, `recipes/debug-playbook.md`.
- templates: `templates/init_loop.cpp`, `templates/builder_widgets_advanced.cpp`, `templates/ota_fs.cpp`.
- playbooks: `playbooks/debug.md`, `playbooks/update.md`.
- deps: `deps/index.md`, `deps/cheatsheet_gyverdb.md`, `deps/cheatsheet_gyverhttp.md`, `deps/cheatsheet_bson_table.md`, `deps/cheatsheet_stringutils_gtl_streamio_stamp_table.md`, `deps/readme_set.md`.
- examples: `examples/libdeps_index.json` (поле `priority: settings|deps`); settings → `examples/settings/summaries|snippets`, deps → `examples/deps/summaries|snippets`.
- обзор: `README.md`, `index.md`, `sources.yaml`.

# Поведение при ответах
- Отвечая на вопросы по Settings: опирайся на cheatsheet/recipes/templates/playbooks; при необходимости углубляйся в `dist/gyver_settings_docs.md`.
- Примеры: используй summaries/snippets из `examples/settings/...`; для зависимостей — только если пользователь просит или есть явная проблема в deps.
- Если нужен код: бери из templates или snippets (Settings), дополняй по месту.
- Если вопрос про зависимость: подключи соответствующую `deps/cheatsheet_*.md` и/или пример из `examples/deps/...`.

# Обновление артефактов (служебно)
- Обновить доки/README: `py -X utf8 spec/docs/gyversettings/scripts/refresh_gyversettings.py` (PyYAML + requests).
- Переиндексировать примеры: `py -X utf8 spec/docs/gyversettings/scripts/index_libdeps_examples.py` (читает `.pio/libdeps`).

# Notes
- Все файлы UTF-8. UI Settings вшит в прошивку, CORS управляется `SETS_NO_CORS`, DB можно отключить `SETT_NO_DB`.
