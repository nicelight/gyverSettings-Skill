// OTA и файловый менеджер (работает через встроенные маршруты Settings)
// Требует: LittleFS/SD и аутентификацию Settings.
#include <SettingsGyver.h>
#include <GyverDBFile.h>
#include <LittleFS.h>

extern SettingsGyver sett;
extern GyverDBFile db;

// В onBuild добавить кнопку OTA или подсказку, но в целом OTA по /ota уже доступно при авторизации.
// Файлы: /fetch (GET path), /upload (POST path + body).
// Здесь лишь пример инициализации FS и DB, обычно это в setup().

void init_fs_db() {
    LittleFS.begin(true);
    db.begin();
}
