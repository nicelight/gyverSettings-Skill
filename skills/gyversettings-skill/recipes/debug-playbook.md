---
title: Settings — debug playbook
updated: 2025-12-30
---

# Базовые шаги
- Лог Serial: убедиться, что `begin()`/`tick()` вызываются, WiFiConnector сообщает о состоянии.
- FS: `LittleFS.begin(true)` на ESP32; проверить, что файл `/data.db` создаётся.
- DB: `db.changed()`/`db.dump()` для проверки записей.

# UI/HTTP
- Нет UI: проверить маршруты (GyverHTTP), CORS (`SETS_NO_CORS`), статус WiFi/AP, captive.
- Медленно/таймауты: уменьшить лишние виджеты, проверить память.

# OTA
- Проверить размер прошивки (flash), Content-Length, RAM.
- При ошибке — смотреть `Update.hasError()`.

# FS операции
- `/fetch`/`/upload`: авторизация, путь к файлу, наличие LittleFS/SD.

# WS/Async
- Если используете WS/Async адаптеры — убедиться в зависимостях (ESPAsyncWebServer/arduinoWebSockets/ESPAsyncTCP) и правильном include.

# Частые проблемы
- AP не закрывается: `WiFiConnector.closeAP` или флаг из DB.
- Значения не сохраняются: не вызван `db.init` или `SETT_NO_DB` выключил работу с БД.
- CORS: для внешних фронтов включить/отключить `SETS_NO_CORS`.
