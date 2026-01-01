---
title: GyverSettings-skill — спецификация и использование
updated: 2026-01-01
owner: tech
---

# Назначение
Скилл **GyverSettings-skill** помогает разрабатывать, рефакторить и отлаживать проекты на библиотеке Settings by AlexGyver (ESP32/ESP8266, PlatformIO/Arduino) с учётом её кастомных зависимостей. Включает конспекты, рецепты, шаблоны кода, индексы примеров и служебные скрипты обновления.

# Размещение в репозитории
- Исходники скилла: `skills/gyversettings-skill/`
  - `SKILL.md` — триггер/описание поведения и навигация по ресурсам.
  - `dist/` — слитые доки и шпаргалки (cheatsheet + полные доки).
  - `recipes/` — сценарии (new-project, refactor, debug).
  - `templates/` — кодовые сниппеты (init_loop, advanced widgets, OTA/FS).
  - `playbooks/` — чеклисты (debug, update).
  - `deps/` — шпаргалки по зависимостям + конспекты README.
  - `examples/` — индекс примеров и авторазборы (Settings — по умолчанию, deps — по запросу).
  - `scripts/` — служебные скрипты обновления (`refresh_gyversettings.py`, `index_libdeps_examples.py`).
  - `README.md`, `index.md`, `sources.yaml`.
- Готовый пакет: `skills/dist/gyversettings-skill.skill` (+ `skills/dist/CHECKSUMS.txt`).

# Поведение скилла (как пользоваться)
- Базовый контекст: `dist/gyver_settings_cheatsheet.md` + релевантные `recipes/`, `templates/`, `playbooks/`.
- Глубокие вопросы по Settings: подключать `dist/gyver_settings_docs.md`.
- Примеры:
  - по умолчанию — `examples/settings/summaries|snippets` и `examples/libdeps_index.json` (priority=settings);
  - зависимости — `examples/deps/...` только при расследовании проблем в deps.
- Зависимости: при вопросах про БД/HTTP/бинарные таблицы/утилиты — открывать соответствующие файлы из `deps/`.
- Кодовые ответы: опираться на `templates/` или snippets из examples (Settings).

# Обновление артефактов
1. Обновить доки/README (тянет GitHub raw):
   ```
   py -X utf8 spec/docs/gyversettings/scripts/refresh_gyversettings.py
   ```
   Требуются PyYAML и requests.
2. Переиндексировать примеры (читает `.pio/libdeps` текущего проекта):
   ```
   py -X utf8 spec/docs/gyversettings/scripts/index_libdeps_examples.py
   ```
   Формирует `examples/libdeps_index.json` и перегенерирует summaries/snippets (Settings — по умолчанию, deps — тоже генерируются, но подключать их следует по запросу).

# Пакетирование (если нужен .skill)
- Использовать дистрибутив skill-creator (`package_skill.py`), указав каталог `skills/gyversettings-skill/` и выход `skills/dist/`.
- Пример (указать свой путь к package_skill.py):
  ```
  python path/to/package_skill.py skills/gyversettings-skill skills/dist
  ```

# Примечания
- Все файлы в UTF-8.
- Полный список и связи см. в `SKILL.md` (навигатор) и `index.md`.
