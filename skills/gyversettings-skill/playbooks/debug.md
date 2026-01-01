---
title: Playbook — отладка Settings
updated: 2025-12-30
---

- **Инициализация**: FS `LittleFS.begin(true)`, DB `db.begin()/init`, WiFiConnector `setName/closeAP/connect`, Settings `begin/onBuild/onUpdate/tick`.
- **UI не открывается**: проверить WiFi/AP доступ, captive (если нужен), CORS (`SETS_NO_CORS`), маршруты GyverHTTP, Serial-логи.
- **Данные не сохраняются**: убедиться, что нет `SETT_NO_DB`, все ключи `db.init(...)`, есть запись файла `/data.db`.
- **OTA**: размер прошивки и flash, `Update.hasError()`, корректный Content-Length, питание.
- **FS**: путь, наличие LittleFS/SD, права; `/fetch`/`/upload` требуют авторизации.
- **WS/Async**: зависимости (ESPAsyncWebServer/arduinoWebSockets/ESPAsyncTCP), правильный адаптер.
- **Ресурсы**: уменьшить виджеты/графику, следить за RAM/flash; gzip UI уже встроен.
