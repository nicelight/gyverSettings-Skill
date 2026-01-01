---
title: Settings — рецепт нового проекта
updated: 2025-12-30
---

# PlatformIO
```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
board_build.filesystem = littlefs
lib_deps =
    gyverlibs/Settings
    gyverlibs/WiFiConnector
```

# Инициализация (пример)
```cpp
#include <LittleFS.h>
#include <GyverDBFile.h>
#include <SettingsGyver.h>
#include <WiFiConnector.h>

DB_KEYS(kk, wifi_ssid, wifi_pass, close_ap);
GyverDBFile db(&LittleFS, "/data.db");
SettingsGyver sett("Project", &db);

void build(sets::Builder& b) {
    sets::Group g(b, "WiFi");
    b.Input(kk::wifi_ssid, "SSID");
    b.Pass(kk::wifi_pass, "Pass", "");
    if (b.Button("Connect")) WiFiConnector.connect(db[kk::wifi_ssid], db[kk::wifi_pass]);
}

void update(sets::Updater& u) {}

void setup() {
    Serial.begin(115200);
    LittleFS.begin(true);
    db.begin();
    db.init(kk::wifi_ssid, "");
    db.init(kk::wifi_pass, "");
    db.init(kk::close_ap, true);
    WiFiConnector.setName("Project");
    WiFiConnector.closeAP(db[kk::close_ap]);
    WiFiConnector.connect(db[kk::wifi_ssid], db[kk::wifi_pass]);
    sett.begin();
    sett.onBuild(build);
    sett.onUpdate(update);
}

void loop() {
    WiFiConnector.tick();
    sett.tick();
}
```

# Мини-чеклист
- FS: `LittleFS.begin(true)` на ESP32.
- DB: `db.init` для всех ключей с дефолтом.
- WiFi: имя AP/STA, таймауты, `closeAP`.
- Settings: выбрать адаптер (Gyver/ESP/Async/WS/Camera), если нужен другой — заменить include и класс.
- Память: следите за OTA/FS размером; gzip UI встроен в прошивку.
