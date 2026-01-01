---
title: libdeps_index.json — схема
updated: 2025-12-29
---

# Назначение
Индекс примеров из локальных библиотек в `.pio/libdeps/*/<lib>/examples/**`. Содержит только метаданные и пути; содержимое читается по запросу.

# Формат JSON
Массив объектов:
```json
[
  {
    "lib": "Settings",
    "version": "1.3.13",
    "env": "esp32dev",
    "example": "Basic",
    "path": ".pio/libdeps/esp32dev/Settings/examples/Basic",
    "priority": "settings",
    "has_platformio_ini": true,
    "has_src": true,
    "has_data": false,
    "tags": ["settings", "gyver-http", "fs", "ota"],
    "hash": "optional-sha1-of-path-list"
  }
]
```

## Поля
- `lib` (string) — имя библиотеки из `library.properties`.
- `version` (string) — версия библиотеки.
- `env` (string) — имя окружения PlatformIO (по каталогу в `.pio/libdeps`).
- `example` (string) — имя примера (по папке).
- `path` (string) — относительный путь к корню примера.
- `has_platformio_ini` (bool) — есть `platformio.ini` в примере.
- `has_src` (bool) — есть исходники (`src/*.cpp` или `*.ino`).
- `has_data` (bool) — есть `data/`.
- `tags` (array[string], optional) — эвристические теги (например: `gyver-http`, `async`, `ws`, `fs`, `ota`, `camera`, `logger`, `graphs`).
- `hash` (string, optional) — хэш списка путей файлов для быстрой проверка изменений.
