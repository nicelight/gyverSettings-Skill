// Инициализация Settings + GyverDBFile + WiFiConnector (GyverHTTP адаптер)
#include <LittleFS.h>
#include <GyverDBFile.h>
#include <SettingsGyver.h>
#include <WiFiConnector.h>

DB_KEYS(kk, wifi_ssid, wifi_pass, close_ap);

GyverDBFile db(&LittleFS, "/data.db");
SettingsGyver sett("Project", &db);

static void build(sets::Builder& b) {
    sets::Group g(b, "WiFi");
    b.Input(kk::wifi_ssid, "SSID");
    b.Pass(kk::wifi_pass, "Pass", "");
    if (b.Switch(kk::close_ap, "Close AP")) WiFiConnector.closeAP(db[kk::close_ap]);
    if (b.Button("Connect")) WiFiConnector.connect(db[kk::wifi_ssid], db[kk::wifi_pass]);
}

static void update(sets::Updater& u) {
    // обрабатывайте события/значения при необходимости
}

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
