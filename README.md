# GyverSettings Skill Pack

Добро пожаловать! Этот репозиторий — рабочая площадка для скилла **GyverSettings-skill**, который помогает разрабатывать, рефакторить и отлаживать проекты на библиотеке Settings by AlexGyver (ESP32/ESP8266, PlatformIO/Arduino) вместе с её кастомным стеком зависимостей.

## Что внутри
- 📂 `skills/gyversettings-skill/` — исходники скилла (SKILL.md, dist/cheatsheet+доки, recipes, templates, playbooks, deps-шпаргалки, примеры, scripts, sources.yaml).
- 📦 `skills/dist/gyversettings-skill.skill` — упакованный скилл + `CHECKSUMS.txt`.
- 🛠️ Служебные скрипты обновления:
  - `spec/docs/gyversettings/scripts/refresh_gyversettings.py` — тянет доки Settings и README зависимостей.
  - `spec/docs/gyversettings/scripts/index_libdeps_examples.py` — индексирует примеры из `.pio/libdeps` (разделяет Settings/Deps).
- 📝 Документация:
  - `spec/docs/gyversettings-skill.md` — спецификация и как пользоваться скиллом.
  - `spec/gyversettings-skill/README.md` — обзор артефактов скилла.

## Как обновить артефакты
```powershell
# обновить доки/README
py -X utf8 spec/docs/gyversettings/scripts/refresh_gyversettings.py
# проиндексировать примеры из .pio/libdeps
py -X utf8 spec/docs/gyversettings/scripts/index_libdeps_examples.py
```
Все файлы в UTF-8.

## Как запаковать скилл
```powershell
$creator = "path/to/package_skill.py"   # из дистрибутива skill-creator
python $creator skills/gyversettings-skill skills/dist
```
Результат — `skills/dist/gyversettings-skill.skill`.

## Куда смотреть дальше
- Для навигации по ресурсам скилла — `skills/gyversettings-skill/SKILL.md` и `skills/gyversettings-skill/README.md`.
- Для подробной спецификации и сценариев использования — `spec/docs/gyversettings-skill.md`.
