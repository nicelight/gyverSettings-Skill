---
title: Playbook — обновление Settings/стека
updated: 2025-12-30
---

- Зафиксировать текущие версии Settings + deps (GTL, GyverDB, StringUtils, GyverHTTP, BSON, Stamp, Table, StreamIO).
- Проверить требования адаптера (Gyver/ESP/Async/WS/Camera) и внешние зависимости (ESPAsyncWebServer, arduinoWebSockets, ESPAsyncTCP).
- Просмотреть CHANGELOG/README для минимальных версий и известных несовместимостей.
- Прогнать сборку + UI smoke: открыть панель, проверить сохранение в DB, WiFi/AP, OTA/FS.
- Обновить `libdeps_index` (примеры) при смене версии: запустить `scripts/index_libdeps_examples`.
- При необходимости — пересобрать dist/cheatsheet (скрипт `refresh_gyversettings`).
