---
title: Settings — чеклист рефакторинга/обновления
updated: 2025-12-30
---

# Версии и зависимости
- Проверить `library.properties`/`platformio.ini` версии Settings и стека (GTL, GyverDB, StringUtils, GyverHTTP, BSON, Stamp, Table, StreamIO).
- Если меняете адаптер (Gyver → Async/WS/ESP/Camera), убедитесь в наличии нужных зависимостей (ESPAsyncWebServer/arduinoWebSockets/ESPAsyncTCP).

# Дефайны/опции
- `SETT_NO_DB` — убрать GyverDB (требует ручного хранения).
- `SETS_NO_CORS` — отключить CORS.
- GyverDB: `DB_NO_UPDATES/DB_NO_FLOAT/DB_NO_INT64/DB_NO_CONVERT` при необходимости экономии.

# Кодовая база
- Инициализация: FS (`LittleFS.begin(true)`), DB (`db.init`), WiFi (Connector), Settings `begin()/onBuild/onUpdate/tick()`.
- Пересобрать build/update под новый адаптер (если меняется).
- Проверить пути файлов `/data.db`, OTA/FS обработчики (если переименованы).

# Тесты/ручная проверка
- UI открывается, build отрабатывает, значения сохраняются в DB.
- WiFi STA/AP работает, OTA и файловый менеджер отвечают.
- Размер прошивки/FS укладывается в разделы.

# Типовые миграции
- Обновление Settings 1.x → 1.3+: учесть появление WS, графиков, настроек времени; проверить совместимость зависимостей (минимальные версии из README).
