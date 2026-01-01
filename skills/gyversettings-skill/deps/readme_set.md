---
title: README зависимостей — конспект
updated: auto
---

## GTL
[![latest](https://img.shields.io/github/v/release/GyverLibs/GTL.svg?color=brightgreen)](https://github.com/GyverLibs/GTL/releases/latest/download/GTL.zip)
[![PIO](https://badges.registry.platformio.org/packages/gyverlibs/library/GTL.svg)](https://registry.platformio.org/libraries/gyverlibs/GTL)
[![Foo](https://img.shields.io/badge/Website-AlexGyver.ru-blue.svg?style=flat-square)](https://alexgyver.ru/)
[![Foo](https://img.shields.io/badge/%E2%82%BD%24%E2%82%AC%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B0-orange.svg?style=flat-square)](https://alexgyver.ru/support_alex/)
[![Foo](https://img.shields.io/badge/README-ENGLISH-blueviolet.svg?style=flat-square)](https://github-com.translate.goog/GyverLibs/GTL?_x_tr_sl=ru&_x_tr_tl=en)  

[![Foo](https://img.shields.io/badge/ПОДПИСАТЬСЯ-НА%20ОБНОВЛЕНИЯ-brightgreen.svg?style=social&logo=telegram&color=blue)](https://t.me/GyverLibs)

# Gyver Template Library
Набор шаблонных инструментов
- Умные указатели
- Динамические массивы
- Буферы
- Связанный список

### Совместимость
Совместима со всеми Arduino платформами (используются Arduino-функции)

## Содержание
- [Использование](#usage)
- [Версии](#versions)
- [Установка](#install)
- [Баги и обратная связь](#feedback)

<a id="usage"></a>

## Использование
### Аллокатор
`array_x`/`stack_x` используют сишный аллокатор `realloc` для изменения размера. Это позволяет менять размер без создания дыр в памяти, как в других vector-подобных библиотеках, память используется очень сильно эффективнее. Но в то же время **GTL-массивы не вызывают конструкторы и деструкторы**, поэтому категорически не рекомендуется использовать их с объектами, которые содержат динамические данные (например String) или copy/move семантику!!! 

### move
`gtl::array` и `gtl::stack` поддерживают copy/move семантику, имеется функция `gtl::move(x)`:

- `gtl::array<> a(b)` - copy
- `gtl::array<> a(gtl::move(b))` - move

### gtl::array
Динамический массив

```cpp
// доступ к буферу
T* buf();
operator T*();

// размер в кол-ве элементов
uint16_t size();

// размер в байтах
size_t sizeBytes();

// очистить (заполнить нулями)
void clear();

// изменить размер в количестве элементов T
bool resize(uint16_t size);

// удалить буфер
void reset();

// переместить (swap) из другого экземпляра
void move(array& other);
```

### gtl::stack_x
Динамический массив, хранит данные линейно, позволяет добавлять и убирать их. Имеет несколько вариантов:
- `stack` - динамический буфер
- `stack_ext` - внешний буфер
- `stack_static` - внутренний статический буфер

```cpp
// экспортировать в файл
bool writeToFile(FS& fs, const char* path);

// импортировать из файла
bool readFromFile(FS& fs, const char* path);

// экспортировать в Stream (напр. файл)
bool writeTo(TS& stream);

// импортировать из Stream (напр. файл)

## GyverDB
[![latest](https://img.shields.io/github/v/release/GyverLibs/GyverDB.svg?color=brightgreen)](https://github.com/GyverLibs/GyverDB/releases/latest/download/GyverDB.zip)
[![PIO](https://badges.registry.platformio.org/packages/gyverlibs/library/GyverDB.svg)](https://registry.platformio.org/libraries/gyverlibs/GyverDB)
[![Foo](https://img.shields.io/badge/Website-AlexGyver.ru-blue.svg?style=flat-square)](https://alexgyver.ru/)
[![Foo](https://img.shields.io/badge/%E2%82%BD%24%E2%82%AC%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B0-orange.svg?style=flat-square)](https://alexgyver.ru/support_alex/)
[![Foo](https://img.shields.io/badge/README-ENGLISH-blueviolet.svg?style=flat-square)](https://github-com.translate.goog/GyverLibs/GyverDB?_x_tr_sl=ru&_x_tr_tl=en)  

[![Foo](https://img.shields.io/badge/ПОДПИСАТЬСЯ-НА%20ОБНОВЛЕНИЯ-brightgreen.svg?style=social&logo=telegram&color=blue)](https://t.me/GyverLibs)

# GyverDB
Простая база данных для Arduino:
- Хранение данных в парах ключ-значение
- Поддерживает все целочисленные типы, float, строки и бинарные данные
- Быстрая автоматическая конвертация данных между разными типами
- Быстрый доступ благодаря хэш ключам и бинарному поиску - в 10 раз быстрее библиотеки [Pairs](https://github.com/GyverLibs/Pairs) и в 11 раз быстрее Preferences (ESP32)
- Компактная реализация - 8 байт на одну ячейку
- Встроенный механизм автоматической записи на флешку ESP8266/ESP32

### Совместимость
Совместима со всеми Arduino платформами (используются Arduino-функции)

### Зависимости
- [StreamIO](https://github.com/GyverLibs/StreamIO)
- [GTL](https://github.com/GyverLibs/GTL) v1.0.6+
- [StringUtils](https://github.com/GyverLibs/StringUtils) v1.4.15+
- [FOR_MACRO](https://github.com/GyverLibs/FOR_MACRO) v1.0.0+

## Содержание
- [Документация](#docs)
- [Использование](#usage)
- [Версии](#versions)
- [Установка](#install)
- [Баги и обратная связь](#feedback)

<a id="docs"></a>

## Документация
Настройки компиляции перед подключением библиотеки
```cpp
#define DB_NO_UPDATES  // убрать стек обновлений
#define DB_NO_FLOAT    // убрать поддержку float
#define DB_NO_INT64    // убрать поддержку int64
#define DB_NO_CONVERT  // не конвертировать данные (принудительно менять тип ячейки, keepTypes не работает)
```

### GyverDB
```cpp
// конструктор
// можно зарезервировать ячейки
GyverDB(uint16_t reserve = 0);

// не изменять тип ячейки (конвертировать данные если тип отличается) (умолч. true)
void keepTypes(bool keep);

// было изменение бд
bool changed();

// сбросить флаг изменения бд
void clearChanged();

// вывести всё содержимое БД
void dump(Print& p);

// полный вес БД
size_t size();

// экспортный размер БД (для writeTo)
size_t writeSize();

// экспортировать БД в Stream (напр. файл)
bool writeTo(Stream& stream);

// экспортировать БД в буфер размера writeSize()
bool writeTo(uint8_t* buffer);

// импортировать БД из Stream (напр. файл)
bool readFrom(Stream& stream, size_t len);

// импортировать БД из буфера
bool readFrom(const uint8_t* buffer, size_t len);


## StringUtils
[![latest](https://img.shields.io/github/v/release/GyverLibs/StringUtils.svg?color=brightgreen)](https://github.com/GyverLibs/StringUtils/releases/latest/download/StringUtils.zip)
[![PIO](https://badges.registry.platformio.org/packages/gyverlibs/library/StringUtils.svg)](https://registry.platformio.org/libraries/gyverlibs/StringUtils)
[![Foo](https://img.shields.io/badge/Website-AlexGyver.ru-blue.svg?style=flat-square)](https://alexgyver.ru/)
[![Foo](https://img.shields.io/badge/%E2%82%BD%24%E2%82%AC%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B0-orange.svg?style=flat-square)](https://alexgyver.ru/support_alex/)
[![Foo](https://img.shields.io/badge/README-ENGLISH-blueviolet.svg?style=flat-square)](https://github-com.translate.goog/GyverLibs/StringUtils?_x_tr_sl=ru&_x_tr_tl=en)  

[![Foo](https://img.shields.io/badge/ПОДПИСАТЬСЯ-НА%20ОБНОВЛЕНИЯ-brightgreen.svg?style=social&logo=telegram&color=blue)](https://t.me/GyverLibs)

# StringUtils
Набор инструментов для работы со строками
- Быстрые функции конвертации
- Парсинг, разбивание по разделителям
- Несколько классов-конвертеров данных в строку и обратно для использования в других библиотеках
- Кодирование и раскодирование base64, url, unicode, йцукен/qwerty-раскладки

### Совместимость
Совместима со всеми Arduino платформами (используются Arduino-функции)

## Содержание
- [Документация](#docs)
- [Версии](#versions)
- [Установка](#install)
- [Баги и обратная связь](#feedback)

<a id="docs"></a>

## Документация
### `Text`
Класс-обёртка для всех типов строк. Может быть создана в конструкторе из:
- `"const char"` - строки
- `char[]` - строки
- `F("f-строки")`
- `PROGMEM` - строки
- `String` - строки

Особенности:
- Хранит тип и длину строки
- Позволяет **печататься**, **конвертироваться** в любой целочисленный формат и **сравниваться** с переменными всех стандартных типов, а также сравниваться с любыми другими строками
- Вывод в подстроки разными способами, поиск и разделение
- **Не может изменять исходную строку**, все операции только "для чтения"
- **Не создаёт копию строки** и работает с оригинальной строкой, т.е. *оригинальная строка должна быть в памяти на время существования Text*
- Если создана из String строки, то оригинальная String строка не должна меняться в процессе работы экземпляра Text

```cpp
// ====== КОНСТРУКТОР ======
Text(String& str);
Text(const String& str);
Text(const uint8_t* str, uint16_t len);
Text(const char* str, int16_t len = 0, bool pgm = 0);
Text(const __FlashStringHelper* str, int16_t len = 0);

// ======== СИСТЕМА ========
operator bool();                    // Статус строки, существует или нет
bool valid();                       // Статус строки, существует или нет
bool pgm();                         // Строка из Flash памяти
uint16_t length();                  // Длина строки
uint16_t readLen();                 // посчитать и вернуть длину строки (const)
void calcLen();                     // пересчитать и запомнить длину строки (non-const)
Type type();                        // Тип строки
const uint8_t* bytes();             // Получить указатель на строку. Всегда вернёт указатель, отличный от nullptr!
const char* str();                  // Получить указатель на строку. Всегда вернёт ненулевой указатель
const char* end();                  // указатель на конец строки. Всегда вернёт ненулевой указатель
bool terminated();                  // строка валидна и оканчивается \0

// ======== UNICODE ========
// Длина строки с учётом unicode символов
uint16_t lengthUnicode();

// получить позицию юникод символа в строке, если она содержит юникод
uint16_t posToUnicode(uint16_t pos);

// получить реальную позицию символа в строке, если она содержит юникод
uint16_t unicodeToPos(uint16_t pos);

// ======== ХЭШ ========
size_t hash();              // хэш строки size_t
uint32_t hash32();          // хэш строки 32 бит

// ======== PRINT ========
size_t printTo(Print& p);   // Напечатать в Print (c учётом длины)

## GyverHTTP
[![latest](https://img.shields.io/github/v/release/GyverLibs/GyverHTTP.svg?color=brightgreen)](https://github.com/GyverLibs/GyverHTTP/releases/latest/download/GyverHTTP.zip)
[![PIO](https://badges.registry.platformio.org/packages/gyverlibs/library/GyverHTTP.svg)](https://registry.platformio.org/libraries/gyverlibs/GyverHTTP)
[![Foo](https://img.shields.io/badge/Website-AlexGyver.ru-blue.svg?style=flat-square)](https://alexgyver.ru/)
[![Foo](https://img.shields.io/badge/%E2%82%BD%24%E2%82%AC%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B0-orange.svg?style=flat-square)](https://alexgyver.ru/support_alex/)
[![Foo](https://img.shields.io/badge/README-ENGLISH-blueviolet.svg?style=flat-square)](https://github-com.translate.goog/GyverLibs/GyverHTTP?_x_tr_sl=ru&_x_tr_tl=en)  

[![Foo](https://img.shields.io/badge/ПОДПИСАТЬСЯ-НА%20ОБНОВЛЕНИЯ-brightgreen.svg?style=social&logo=telegram&color=blue)](https://t.me/GyverLibs)

# GyverHTTP
Очень простой и лёгкий HTTP сервер и полуасинхронный HTTP клиент
- Быстрая отправка и получение файлов
- Удобный минималистичный API

### Совместимость
Совместима со всеми Arduino платформами (используются Arduino-функции)

## Содержание
- [Использование](#usage)
- [Версии](#versions)
- [Установка](#install)
- [Баги и обратная связь](#feedback)

<a id="usage"></a>

## Использование
### StreamWriter
Быстрый отправлятель данных в Print, поддерживает работу с файлами и PROGMEM. Читает в буфер и отправляет блоками, что многократно быстрее обычной отправки
```cpp
StreamWriter(Stream* stream, size_t size);
StreamWriter(const uint8_t* buf, size_t len, bool pgm = 0);

// размер данных
size_t length();

// установить размер блока отправки
void setBlockSize(size_t bsize);

// напечатать в принт
size_t printTo(Print& p);
```

### StreamReader
Быстрый читатель данных из Stream известной длины. Буферизирует и записывает блоками в потребителя, что многократно быстрее обычного чтения
```cpp
StreamReader(Stream* stream = nullptr, size_t len = 0);

// прочитать в строку
String readString();

// установить таймаут
void setTimeout(size_t tout);

// установить размер блока
void setBlockSize(size_t bsize);

// прочитать в буфер, вернёт true при успехе
bool readBytes(uint8_t* buf);

// вывести в write(uint8_t*, size_t)
template <typename T>
bool writeTo(T& p);

// общий размер входящих данных
size_t length();

// корреткность ридера
operator bool();

Stream* stream;
```

### Client
```cpp
size_t write(uint8_t data);
size_t write(const uint8_t* buffer, size_t size);

// ==========================

// установить новый хост и порт
void setHost(const char* host, uint16_t port);

## BSON
[![latest](https://img.shields.io/github/v/release/GyverLibs/BSON.svg?color=brightgreen)](https://github.com/GyverLibs/BSON/releases/latest/download/BSON.zip)
[![PIO](https://badges.registry.platformio.org/packages/gyverlibs/library/BSON.svg)](https://registry.platformio.org/libraries/gyverlibs/BSON)
[![Foo](https://img.shields.io/badge/Website-AlexGyver.ru-blue.svg?style=flat-square)](https://alexgyver.ru/)
[![Foo](https://img.shields.io/badge/%E2%82%BD%24%E2%82%AC%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B0-orange.svg?style=flat-square)](https://alexgyver.ru/support_alex/)
[![Foo](https://img.shields.io/badge/README-ENGLISH-blueviolet.svg?style=flat-square)](https://github-com.translate.goog/GyverLibs/BSON?_x_tr_sl=ru&_x_tr_tl=en)  

[![Foo](https://img.shields.io/badge/ПОДПИСАТЬСЯ-НА%20ОБНОВЛЕНИЯ-brightgreen.svg?style=social&logo=telegram&color=blue)](https://t.me/GyverLibs)

# BSON
Простой "бинарный" вариант JSON пакета, собирается линейно:
- В среднем в 2-3 раза легче обычного JSON, собирается сильно быстрее
- В ~4 раза быстрее String строки в сборке
- Поддерживает "коды": число, которое может быть ключом или значением, а при распаковке заменится на строку из списка по индексу
- Строки не нужно экранировать
- Поддержка целых чисел 0..8 байт
- Поддержка float с указанием количества знаков точности
- Поддержка JSON массивов и объектов ключ:значение
- Поддержка упаковки произвольных бинарных данных
- Не содержит запятых, они добавляются при распаковке
- Лимит длины `8192` байт для всего: значение кодов, длина строк, длина бинарных данных

### Совместимость
Совместима со всеми Arduino платформами (используются Arduino-функции)

### Зависимости
- [StringUtils](https://github.com/GyverLibs/StringUtils)
- [GTL](https://github.com/GyverLibs/GTL)

## Содержание
- [Использование](#usage)
- [Версии](#versions)
- [Установка](#install)
- [Баги и обратная связь](#feedback)

<a id="usage"></a>

## Использование
### Структура пакета
![bson](/docs/bson.png)

### Динамическая сборка, BSON
```cpp
// прибавить данные любого типа
BSON& add(T data);
void operator=(T data);
void operator+=(T data);

// float
BSON& add(float data, int dec);
BSON& add(double data, int dec);

// ключ
BSON& operator[](T key);

// контейнер, всегда вернёт true. type: '{', '[', '}', ']'
bool operator()(char type);

// бинарные данные
bool beginBin(uint16_t size);
BSON& add(const void* data, size_t size, bool pgm = false);

// строки
BSON& beginStr(size_t len);

// зарезервировать размер
bool reserve(size_t size);

// зарезервировать, элементов (добавить к текущему размеру буфера)
bool addCapacity(size_t size);

// установить увеличение размера для уменьшения количества мелких реаллокаций. Умолч. 8
void setOversize(uint16_t oversize);

// размер в байтах
size_t length();

// доступ к буферу
uint8_t* buf();

// очистить

## Stamp
[![latest](https://img.shields.io/github/v/release/GyverLibs/Stamp.svg?color=brightgreen)](https://github.com/GyverLibs/Stamp/releases/latest/download/Stamp.zip)
[![PIO](https://badges.registry.platformio.org/packages/gyverlibs/library/Stamp.svg)](https://registry.platformio.org/libraries/gyverlibs/Stamp)
[![Foo](https://img.shields.io/badge/Website-AlexGyver.ru-blue.svg?style=flat-square)](https://alexgyver.ru/)
[![Foo](https://img.shields.io/badge/%E2%82%BD%24%E2%82%AC%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B0-orange.svg?style=flat-square)](https://alexgyver.ru/support_alex/)
[![Foo](https://img.shields.io/badge/README-ENGLISH-blueviolet.svg?style=flat-square)](https://github-com.translate.goog/GyverLibs/Stamp?_x_tr_sl=ru&_x_tr_tl=en)

[![Foo](https://img.shields.io/badge/ПОДПИСАТЬСЯ-НА%20ОБНОВЛЕНИЯ-brightgreen.svg?style=social&logo=telegram&color=blue)](https://t.me/GyverLibs)

# Stamp
Библиотека для хранения и манипуляции со временем
- Более удобная в использовании, чем встроенная time.h
- Используются более быстрые алгоритмы преобразования, чем в time.h
- Парсинг из строк
- Может считать и поддерживать время на базе millis()
- Работает ~до 2106 года

### Совместимость
Совместима со всеми Arduino платформами (используются Arduino-функции)

## Содержание
- [Документация](#reference)
- [Пример](#example)
- [Версии](#versions)
- [Установка](#install)
- [Баги и обратная связь](#feedback)

<a id="reference"></a>

## Документация
### Часовой пояс
Настраивается глобально для всех инструментов библиотеки

```cpp
void setStampZone(int zone);    // установить глобальную часовую зону в часах или минутах
int getStampZone();             // получить глобальную часовую зону в минутах
```

### Утилиты
Набор функций для работы со временем и датой

```cpp
// время в секунды
uint32_t StampUtils::timeToSeconds(uint8_t hours, uint8_t minutes, uint8_t seconds);

// високосный год
bool StampUtils::isLeap(uint16_t year);

// дней в месяце без учёта года (февраль 28)
uint8_t StampUtils::daysInMonth(uint8_t month);

// дней в месяце с учётом високосного года
uint8_t StampUtils::daysInMonth(uint8_t month, uint16_t year);

// дней года к месяцу (янв 0, фев 31, март 59/60...)
uint16_t StampUtils::daysToMonth(uint8_t month, uint16_t year);

// дата в день текущего года (начиная с 1)
uint16_t StampUtils::dateToYearDay(uint8_t day, uint8_t month, uint16_t year);

// дата в день недели (пн 1.. вс 7)
uint8_t StampUtils::dateToWeekDay(uint8_t day, uint8_t month, uint16_t year);

// дата в количество дней с 01.01.2000 (начиная с 0)
uint16_t StampUtils::dateToDays2000(uint8_t day, uint8_t month, uint16_t year);

// дата в unix время, zone в минутах
uint32_t StampUtils::dateToUnix(uint8_t day, uint8_t month, uint16_t year, uint8_t hour, uint8_t minute, uint8_t seconds, int16_t zone = 0);
```

### Макросы
```cpp
// время и дата компиляции
__TIME_SEC__
__TIME_MIN__
__TIME_HOUR__
__DATE_DAY__
__DATE_MONTH__
__DATE_YEAR__

// unix с часовой зоной компьютера

## Table
[![latest](https://img.shields.io/github/v/release/GyverLibs/Table.svg?color=brightgreen)](https://github.com/GyverLibs/Table/releases/latest/download/Table.zip)
[![PIO](https://badges.registry.platformio.org/packages/gyverlibs/library/Table.svg)](https://registry.platformio.org/libraries/gyverlibs/Table)
[![Foo](https://img.shields.io/badge/Website-AlexGyver.ru-blue.svg?style=flat-square)](https://alexgyver.ru/)
[![Foo](https://img.shields.io/badge/%E2%82%BD%24%E2%82%AC%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B0-orange.svg?style=flat-square)](https://alexgyver.ru/support_alex/)
[![Foo](https://img.shields.io/badge/README-ENGLISH-blueviolet.svg?style=flat-square)](https://github-com.translate.goog/GyverLibs/Table?_x_tr_sl=ru&_x_tr_tl=en)  

[![Foo](https://img.shields.io/badge/ПОДПИСАТЬСЯ-НА%20ОБНОВЛЕНИЯ-brightgreen.svg?style=social&logo=telegram&color=blue)](https://t.me/GyverLibs)

# Table
Динамическая бинарная таблица для Arduino
- Поддерживает все численные типы данных, символы и нуль-терминированные строки в любом сочетании
- Динамическое добавление строк, прокрутка и прочие удобные фичи для ведения логов
- Автоматическая запись в файл при изменении (esp)
- Возможность добавления строк без чтения файла
- Вес в среднем в 2 раза меньше, чем у текстовой CSV

### Совместимость
Совместима со всеми Arduino платформами (используются Arduino-функции)

### Зависимости
- GTL
- StreamIO

## Содержание
- [Документация](#docs)
- [Примеры](#examples)
- [Версии](#versions)
- [Установка](#install)
- [Баги и обратная связь](#feedback)

<a id="docs"></a>

## Документация
### cell_t
Тип данных ячейки
```cpp
cell_t::None,
cell_t::Int8,
cell_t::Uint8,
cell_t::Int16,
cell_t::Uint16,
cell_t::Int32,
cell_t::Uint32,
cell_t::Float,
cell_t::Int64,
cell_t::Uint64,
cell_t::Unix,   // uint32
cell_t::Char,   // одиночный символ
cell_t::Char8,  // строка макс. 8 символов
cell_t::Char16,
cell_t::Char32,
cell_t::Char64,
cell_t::Char128,
cell_t::Char256,
```

В строковых типах ячеек указана максимальная длина строки без учёта нулевого символа, т.е. `Char16` может хранить строку до 16 символов включительно - размер буфера у ячейки 17 символов.

### Table
```cpp
Table();

// строк, столбцов, типы данных ячеек
Table(uint16_t rows, uint8_t cols, ...);

// создать таблицу (строк, столбцов, типы данных ячеек)
bool create(uint16_t rows, uint8_t cols, ...);

// инициализировать количество и типы столбцов (не изменит таблицу если совпадает)
bool init(uint8_t cols, ...);

// получить строку таблицы. Отрицательные числа - получить с конца
tbl::Row operator[](int row);

// получить строку таблицы. Отрицательные числа - получить с конца
tbl::Row get(int row);

// получить ячейку
tbl::Cell get(int row, uint8_t col);


## StreamIO
[![latest](https://img.shields.io/github/v/release/GyverLibs/StreamIO.svg?color=brightgreen)](https://github.com/GyverLibs/StreamIO/releases/latest/download/StreamIO.zip)
[![PIO](https://badges.registry.platformio.org/packages/gyverlibs/library/StreamIO.svg)](https://registry.platformio.org/libraries/gyverlibs/StreamIO)
[![Foo](https://img.shields.io/badge/Website-AlexGyver.ru-blue.svg?style=flat-square)](https://alexgyver.ru/)
[![Foo](https://img.shields.io/badge/%E2%82%BD%24%E2%82%AC%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B0-orange.svg?style=flat-square)](https://alexgyver.ru/support_alex/)
[![Foo](https://img.shields.io/badge/README-ENGLISH-blueviolet.svg?style=flat-square)](https://github-com.translate.goog/GyverLibs/StreamIO?_x_tr_sl=ru&_x_tr_tl=en)  

[![Foo](https://img.shields.io/badge/ПОДПИСАТЬСЯ-НА%20ОБНОВЛЕНИЯ-brightgreen.svg?style=social&logo=telegram&color=blue)](https://t.me/GyverLibs)

# StreamIO
Обёртка для чтения и записи Stream и массивов-буферов одним классом

### Совместимость
Совместима со всеми Arduino платформами (используются Arduino-функции)

## Содержание
- [Использование](#usage)
- [Версии](#versions)
- [Установка](#install)
- [Баги и обратная связь](#feedback)

<a id="usage"></a>

## Использование

<a id="versions"></a>

## Версии
- v1.0

<a id="install"></a>
## Установка
- Библиотеку можно найти по названию **StreamIO** и установить через менеджер библиотек в:
    - Arduino IDE
    - Arduino IDE v2
    - PlatformIO
- [Скачать библиотеку](https://github.com/GyverLibs/StreamIO/archive/refs/heads/main.zip) .zip архивом для ручной установки:
    - Распаковать и положить в *C:\Program Files (x86)\Arduino\libraries* (Windows x64)
    - Распаковать и положить в *C:\Program Files\Arduino\libraries* (Windows x32)
    - Распаковать и положить в *Документы/Arduino/libraries/*
    - (Arduino IDE) автоматическая установка из .zip: *Скетч/Подключить библиотеку/Добавить .ZIP библиотеку…* и указать скачанный архив
- Читай более подробную инструкцию по установке библиотек [здесь](https://alexgyver.ru/arduino-first/#%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA)
### Обновление
- Рекомендую всегда обновлять библиотеку: в новых версиях исправляются ошибки и баги, а также проводится оптимизация и добавляются новые фичи
- Через менеджер библиотек IDE: найти библиотеку как при установке и нажать "Обновить"
- Вручную: **удалить папку со старой версией**, а затем положить на её место новую. "Замену" делать нельзя: иногда в новых версиях удаляются файлы, которые останутся при замене и могут привести к ошибкам!

<a id="feedback"></a>

## Баги и обратная связь
При нахождении багов создавайте **Issue**, а лучше сразу пишите на почту [alex@alexgyver.ru](mailto:alex@alexgyver.ru)  
Библиотека открыта для доработки и ваших **Pull Request**'ов!

При сообщении о багах или некорректной работе библиотеки нужно обязательно указывать:
- Версия библиотеки
- Какой используется МК
- Версия SDK (для ESP)
- Версия Arduino IDE
- Корректно ли работают ли встроенные примеры, в которых используются функции и конструкции, приводящие к багу в вашем коде
- Какой код загружался, какая работа от него ожидалась и как он работает в реальности
- В идеале приложить минимальный код, в котором наблюдается баг. Не полотно из тысячи строк, а минимальный код

## FOR_MACRO
[![latest](https://img.shields.io/github/v/release/GyverLibs/FOR_MACRO.svg?color=brightgreen)](https://github.com/GyverLibs/FOR_MACRO/releases/latest/download/FOR_MACRO.zip)
[![PIO](https://badges.registry.platformio.org/packages/gyverlibs/library/FOR_MACRO.svg)](https://registry.platformio.org/libraries/gyverlibs/FOR_MACRO)
[![Foo](https://img.shields.io/badge/Website-AlexGyver.ru-blue.svg?style=flat-square)](https://alexgyver.ru/)
[![Foo](https://img.shields.io/badge/%E2%82%BD%24%E2%82%AC%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B0-orange.svg?style=flat-square)](https://alexgyver.ru/support_alex/)
[![Foo](https://img.shields.io/badge/README-ENGLISH-blueviolet.svg?style=flat-square)](https://github-com.translate.goog/GyverLibs/FOR_MACRO?_x_tr_sl=ru&_x_tr_tl=en)  

[![Foo](https://img.shields.io/badge/ПОДПИСАТЬСЯ-НА%20ОБНОВЛЕНИЯ-brightgreen.svg?style=social&logo=telegram&color=blue)](https://t.me/GyverLibs)

# FOR_MACRO
Variadic for макрос

### Совместимость
Совместима со всеми Arduino платформами (используются Arduino-функции)

## Содержание
- [Использование](#usage)
- [Версии](#versions)
- [Установка](#install)
- [Баги и обратная связь](#feedback)

<a id="usage"></a>

## Использование
`FOR_MACRO` - макрос, позволяющий применить другой макрос к variadic списку аргументов, по сути вызывает указанный макрос для каждого аргумента. По умолчанию поддерживает максимум 512 аргументов, можно сгенерировать макрос на любое количество аргументов при помощи приложенного python-скрипта.

Для использования макроса нужно создать два своих макроса - один будет макро-функцией, которая применяется к каждому аргументу, а вторая - сам макрос, который будет использоваться. Первая макро-функция должна иметь вид `F(N, i, p, val)`, где:
- `N` - количество аргументов
- `i` - счётчик, начинается с конца-1 из за особенностей реализации
- `p` - параметр
- `val` - текущий аргумент

Сам `FOR_MACRO` нужно вызвать со следующим списком аргументов в реализации своего макроса:
- `func` - объявленная ранее макро-функция
- `p` - параметр, может быть чем угодно. Можно поставить `0` если не нужен
- `__VA_ARGS__` - список аргументов (из многоточия)

Как это работает будет понятнее на примерах:
```cpp
#define MF1(N, i, p, val) N,
#define FOR_1(...) FOR_MACRO(MF1, 0, __VA_ARGS__)

FOR_1(test, kek, string);   // развернётся в 3, 3, 3,
```
```cpp
#define MF2(N, i, p, val) i,
#define FOR_2(...) FOR_MACRO(MF2, 0, __VA_ARGS__)

FOR_2(test, kek, string);   // развернётся в 2, 1, 0
```
```cpp
#define MF3(N, i, p, val) p,
#define FOR_3(...) FOR_MACRO(MF3, 0, __VA_ARGS__)

FOR_3(test, kek, string);   // развернётся в 0, 0, 0 (параметр)
```
```cpp
#define MF4(N, i, p, val) val,
#define FOR_4(...) FOR_MACRO(MF4, 0, __VA_ARGS__)

FOR_4(test, kek, string);   // развернётся в test, kek, string,
```
```cpp
#define MF5(N, i, p, val) #val,
#define FOR_5(...) FOR_MACRO(MF5, 0, __VA_ARGS__)

FOR_5(test, kek, string);   // развернётся в "test", "kek", "string",
```

Более реальный пример - создание строк
```cpp
#define MF6(N, i, p, val) const char* p##_##i = #val;
#define FOR_6(name, ...) FOR_MACRO(MF6, name, __VA_ARGS__)

FOR_6(strings, test, kek, string);
// развернётся в 
// const char* strings_2 = "test"; 
// const char* strings_1 = "kek"; 
// const char* strings_0 = "string";
```
```cpp

## WiFiConnector
[![latest](https://img.shields.io/github/v/release/GyverLibs/WiFiConnector.svg?color=brightgreen)](https://github.com/GyverLibs/WiFiConnector/releases/latest/download/WiFiConnector.zip)
[![PIO](https://badges.registry.platformio.org/packages/gyverlibs/library/WiFiConnector.svg)](https://registry.platformio.org/libraries/gyverlibs/WiFiConnector)
[![Foo](https://img.shields.io/badge/Website-AlexGyver.ru-blue.svg?style=flat-square)](https://alexgyver.ru/)
[![Foo](https://img.shields.io/badge/%E2%82%BD%24%E2%82%AC%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B0-orange.svg?style=flat-square)](https://alexgyver.ru/support_alex/)
[![Foo](https://img.shields.io/badge/README-ENGLISH-blueviolet.svg?style=flat-square)](https://github-com.translate.goog/GyverLibs/WiFiConnector?_x_tr_sl=ru&_x_tr_tl=en)  

[![Foo](https://img.shields.io/badge/ПОДПИСАТЬСЯ-НА%20ОБНОВЛЕНИЯ-brightgreen.svg?style=social&logo=telegram&color=blue)](https://t.me/GyverLibs)

# WiFiConnector
Асинхронное подключение к WiFi с созданием точки доступа при таймауте подключения

### Совместимость
ESP8266, ESP32

## Содержание
- [Использование](#usage)
- [Версии](#versions)
- [Установка](#install)
- [Баги и обратная связь](#feedback)

<a id="usage"></a>

## Использование
Использовать в случаях, когда пароль от WiFi хранится "где-то". При передаче пустой строки будет запущена точка доступа. Если подключиться не получится - также развернётся точка доступа для веб-интерфейса и прочего.

### Описание классов
```cpp
// имя AP, пароль AP, таймаут в секундах, отключать AP при успешном подключении к STA (иначе AP_STA)
WiFiConnectorClass(const String& APname = "ESP AP",
                    const String& APpass = "",
                    uint16_t timeout = 60 * 3,
                    bool closeAP = true);

// установить имя AP
void setName(const String& name);

// установить пароль AP
void setPass(const String& pass);

// установить таймаут подключения в секундах. 0 - отключить таймаут
void setTimeout(uint16_t timeout);

// автоматически отключать AP при подключении к STA (умолч. вкл)
void closeAP(bool close);

// подключить обработчик успешного подключения
void onConnect(ConnectorCallback cb);

// подключить обработчик ошибки подключения, вызовется после старта AP
void onError(ConnectorCallback cb);

// подключиться. Вернёт false если ssid не задан, будет запущена AP
bool connect(const String& ssid, const String& pass = emptyString);

// вызывать в loop. Вернёт true при смене состояния
bool tick();

// состояние подключения. true - подключен, false - запущена АР
bool connected();

// в процессе подключения
bool connecting();
```

### Примеры
```cpp
#include <Arduino.h>
#include <WiFiConnector.h>

void setup() {
    WiFiConnector.connect("SSID", "PASS");

    WiFiConnector.onConnect([]() {
        Serial.print("Connected. Local IP: ");
        Serial.println(WiFi.localIP());
    });
    WiFiConnector.onError([]() {
        Serial.print("WiFi error. AP IP: ");
        Serial.println(WiFi.softAPIP());
    });
