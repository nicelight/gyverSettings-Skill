---
id: context
version: 1
updated: 2025-12-29
owner: techlead
---

# Устойчивый контекст

## Среды и развёртывания
- Разработка: PlatformIO, ESP32 DevKit (Arduino), LittleFS.
- Текущая задача: подготовка артефактов для Agent Skill (GyverSettings-skill); развёртывание на устройство не требуется.

## Стек и архитектура
- Библиотека Settings by AlexGyver + зависимости: GTL, GyverDB, StringUtils, GyverHTTP, BSON, Stamp, Table, StreamIO; косвенно FOR_MACRO. Частый напарник: WiFiConnector.
- Settings включает встроенный gzip веб-UI, HTTP на GyverHTTP, бинарный протокол (BSON/Table), файловый менеджер, OTA, логгер; адаптеры Gyver/ESP/Async/WS/Camera.

## Конфигурация и секреты
- Локально: `.pio/libdeps/esp32dev` содержит версии зависимостей; `platformio.ini` фиксирует `gyverlibs/Settings` и `gyverlibs/WiFiConnector`.
- Секреты отсутствуют; примеры используют тестовые креды.

## Команды разработчика (pre-commit чек-лист)
- Соблюдать UTF-8 без BOM; проверки чтением через `py -X utf8 ...`.
- Обновление артефактов — будущий скрипт `scripts/refresh_gyversettings.(ps1|py)` (добавить).
- Проверка структуры артефактов `spec/docs/gyversettings` (dist/recipes/templates/playbooks/index).

## Мониторинг и Ops
- Не применяется для задачи создания скилла; фокус на офлайн-артефактах и управляемом обновлении.
