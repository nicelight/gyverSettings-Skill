---
title: GyverDB — шпаргалка
updated: 2025-12-30
---

- Ключи: макрос `DB_KEYS(ns, key1, key2, ...)`; доступ `db[ns::key]`.
- Инициализация: `db.begin(); db.init(hash, default);` — создаёт при отсутствии.
- Типы: хранит int/float/string/binary; конверсия включена, если `DB_NO_CONVERT` не задан.
- Хранение: с `GyverDBFile` пишется в LittleFS/SD; файл путь задаётся в конструкторе.
- Настройки: `keepTypes(bool)`, `changed()/clearChanged()`, `writeTo/readFrom` для экспорта.
- Оптимизации: можно отключать `DB_NO_FLOAT`, `DB_NO_INT64`, `DB_NO_UPDATES` для экономии.
