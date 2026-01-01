---
title: Settings — краткая шпаргалка
updated: 2025-12-30
---

# Init flow (GyverHTTP адаптер)
1. FS: `LittleFS.begin(true)` (ESP32) / `LittleFS.begin()`.
2. DB: `GyverDBFile db(&LittleFS, "/data.db"); db.begin(); db.init(key, default);`.
3. WiFi (опционально): `WiFiConnector.setName(...); WiFiConnector.closeAP(...); WiFiConnector.connect(ssid, pass);`.
4. Settings: `sett.begin(captive=true, domain=nullptr); sett.onBuild(build); sett.onUpdate(update);`.
5. loop: `WiFiConnector.tick(); sett.tick();`.

# Build/Update
- `onBuild` получает `sets::Builder& b`: создавайте группы/виджеты. Пример:
  ```cpp
  sets::Group g(b, "WiFi");
  b.Input(kk::wifi_ssid, "SSID");
  b.Pass(kk::wifi_pass, "Pass", "");
  if (b.Button("Connect")) WiFiConnector.connect(db[kk::wifi_ssid], db[kk::wifi_pass]);
  ```
- `onUpdate` получает `sets::Updater& u`: реагируйте на события/значения.
- Ключи задаются макросом `DB_KEYS(ns, key1, key2, ...)`.

# Хранилище
- По умолчанию Settings работает с GyverDB (можно отключить `SETT_NO_DB`).
- GyverDBFile автоматически пишет на LittleFS; `db.init(hash, default)` для дефолтов.

# Веб/Endpoints
- Встроенный веб UI вшит в прошивку (gzip, без загрузки fs-образа).
- Роуты GyverHTTP: `/settings`, `/fetch`, `/upload`, `/ota`, `/script.js`, `/style.css`, `/favicon.svg`, `/custom.js`.
- Можно отключить CORS: `SETS_NO_CORS`.

# OTA / FS
- OTA: запрос на `/ota` с авторизацией; использует `Update`.
- FS: `/fetch` (чтение), `/upload` (запись) при успешной авторизации; работает с `LittleFS`/`SD`.

# Адаптеры
- `SettingsGyver` (GyverHTTP, WiFiServer/WiFiClient) — используется здесь.
- `SettingsESP` (ESP WebServer), `SettingsAsync`/`SettingsAsyncWS` (ESPAsyncWebServer), `SettingsGyverWS`, `SettingsCamera`.
- Выбор адаптера влияет на зависимости (arduinoWebSockets / ESPAsyncTCP / ESPAsyncWebServer).

# Дефайны/опции (компиляция)
- `SETT_NO_DB` — убрать поддержку GyverDB.
- `SETS_NO_CORS` — отключить CORS.
- Для GyverDB см. cheat `deps/cheatsheet_gyverdb.md`.

# Типовые проблемы
- Нет UI: проверьте `begin()`/`tick()`, FS init, WiFi/AP доступ, CORS.
- OTA падает: мало RAM/flash, некорректный Content-Length.
- FS ошибки: `LittleFS.begin(true)` на ESP32, права пути, размер раздела.
