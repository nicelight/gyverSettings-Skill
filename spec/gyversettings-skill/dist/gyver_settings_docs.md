---
title: Settings — слитые доки
updated: auto
---

# 1.main.md
## Настройки компиляции
```cpp
#define SETT_NO_DB      // полностью отключить поддержку GyverDB
#define SETT_NO_TABLE   // полностью отключить поддержку Table
```

## Типы данных
### Text
`Text` - это обёртка для текстовых данных из библиотеки [StringUtils](https://github.com/GyverLibs/StringUtils), см. документацию там. Text может конвертироваться в любые другие типы и сравниваться с ними, а также имеет множество инструментов для парсинга и поиска.

```cpp
Serial.println(b.build.value);  // печатается
b.build.value == 123;           // сравнивается
b.build.value == "123";         // сравнивается
b.build.value.toFloat();        // конвертируется
int b = b.build.value;          // авто-конвертируется
```

При передаче в функцию библиотеки аргумент `Text` может быть любым строковым типом:

```cpp
void foo(Text);     // условная функция библиотеки

String s;
foo(s);
foo("cstring");
foo(F("F-string"));
```

Если в качестве строкового значения нужно число - используйте конструктор `Value`, например `b.Color("col", "Color", Value(int_var));`

### AnyPtr
Указатель на переменную любого типа: `float`, `double`, любой целочисленный, `String`, `AnyPtr(char[], size_t len)`. В этот аргумент происходит "подключение" переменной, чтобы библиотека могла её менять:

```cpp
void foo(AnyPtr);   // условная функция библиотеки

uint32_t ul;
int arr[2];
float fl;
String s;
char buf[10];

foo(nullptr);   // по умолчанию, передано "ничего"
foo(&ul);
foo(&arr[0]);
foo(&fl);
foo(&s);
foo(AnyPtr(buf, 10));   // для char-буфера нужно явно указать длину
```

## Описание классов
- `SettingsT` (*SettingsT.h*) - вебсервер и клиент на выбор (для связи через Ethernet например)
- `SettingsGyver` (*SettingsGyver.h*) - вебсервер GyverHTTP
- `SettingsESP` (*SettingsESP.h*) - стандартный вебсервер ESP
- `SettingsAsync` (*SettingsAsync.h*) - асинхронный ESPAsyncWebserver
- `SettingsGyverWS` (*SettingsGyverWS.h*) - вебсервер GyverHTTP + websocket
- `SettingsESPWS` (*SettingsESPWS.h*) - стандартный вебсервер ESP + websocket
- `SettingsAsyncWS` (*SettingsAsyncWS.h*) - асинхронный ESPAsyncWebserver + websocket

### Вебсокет
Версия с вебсокетом позволяет отправлять обновления сразу **из любого места в программе**. Также обмен данных с сервером осуществляется быстрее, чем в обычной HTTP версии.

### SettingsXxx
```cpp
Settings(const String& title = "", GyverDB* db = nullptr);

// запустить. captive - запустить mdns для автооткрытия окна в режиме AP при подключении к точке
// domain - домен, по которому есп будет доступна в локальной сети по адресу домен.local
void begin(bool captive = true, const char* domain = nullptr);

// установить версию прошивки для отображения в меню
void setVersion(const char* ver);

// установить пароль на вебморду. Пустая строка "" чтобы отключить
void setPass(Text pass);

// перезагрузить страницу. Можно вызывать где угодно + в обработчике update
void reload(bool force = false);

// установить заголовок страницы
void setTitle(const String& title);

// подключить базу данных
void attachDB(GyverDB* db);

// использовать автоматические обновления из БД (при изменении записи новое значение отправится в браузер)
void useAutoUpdates(bool use);

// обработчик билда типа f(sets::Builder& b)
void onBuild(BuildCallback cb);

// обработчик скачивания файлов с устройства типа f(Text path)
void onFetch(FileCallback cb);

// обработчик загрузки файлов на устройство типа f(Text path)
void onUpload(FileCallback cb);

// обработчик подключения браузера f()
void onFocusChange(FocusCallback cb);

// обработчик обновлений типа f(sets::Updater& upd) [ДЛЯ ВЕРСИЙ БЕЗ ВЕБСОКЕТА]
void onUpdate(UpdateCallback cb);

// начать обновления [ДЛЯ ВЕРСИЙ С ВЕБСОКЕТОМ]
InlineUpdater updater();

// тикер, вызывать в родительском классе
void tick();

// вебморда открыта в браузере
bool focused();

// установить размер пакета (умолч. 1024 Б). 0 - отключить разбивку на пакеты. Не работает для Async-версии
void setPacketSize(size_t size);

// установить кастом js код из PROGMEM
void setCustom(const char* js, size_t len, bool gz = false);

// установить кастом js код из файла
void setCustomFile(const char* path, bool gz = false);

// установить инфо о проекте (отображается на вкладке настроек и файлов)
void setProjectInfo(const char* name, const char* link = nullptr);

// время с браузера
StampKeeper rtc;

// настройки вебморды
Config config;
{
    // таймаут отправки слайдера, мс. 0 чтобы отключить
    uint16_t sliderTout = 100;

    // таймаут ожидания ответа сервера, мс
    uint16_t requestTout = 2000;

    // период обновлений, мс. 0 чтобы отключить
    uint16_t updateTout = 2500;

    // основная цветовая схема
    Colors theme = Colors::Green;

    // использовать файловый менеджер
    bool useFS = true;
}
```

### Builder
```cpp
// инфо о билде
Build build;

// авто-ID следующего виджета
size_t nextID();

// указатель на текущий SettingsXxx
void* thisSettings();

// перезагрузить страницу (вызывать в действии, например if (...click() b.reload()))
void reload(bool force = false);

// было действие с каким-то из виджетов выше
bool wasSet();

// сбросить флаг чтения wasSet
void clearSet();

// КОНТЕЙНЕРЫ
// разрешить неавторизованным клиентам следующий код
bool beginGuest();

// запретить неавторизованным клиентам
void endGuest();

// группа
bool beginGroup(Text title = Text());
void endGroup();

// вложенное меню
bool beginMenu(Text title);
void endMenu();

// true, если в вебморде было открыто текущее меню
bool enterMenu();

// горизонтальная группа виджетов [DivType::Line | DivType::Block]
bool beginRow(Text title = Text(), DivType divtype = DivType::Default);
void endRow();

// ряд кнопок
bool beginButtons();
void endButtons();
```

#### Пассивные виджеты
```cpp
// ================= LINK =================
void Link(Text label, Text url);

// ================= LOG =================
void Log(size_t id, Logger& log, Text label = "");
void Log(Logger& log, Text label = "");

// ================= LABEL =================
// текстовое значение, может обновляться по id
void Label(size_t id, Text label = "", Text text = Text(), uint32_t color = SETS_DEFAULT_COLOR);
void Label(size_t id, Text label, Text text, sets::Colors color);
void Label(Text label = "", Text text = Text(), uint32_t color = SETS_DEFAULT_COLOR);
void Label(Text label, Text text, sets::Colors color);

// лейбл с численным значением (выполняется быстрее, весит меньше)
void LabelNum(size_t id, Text label, T text, uint32_t color = SETS_DEFAULT_COLOR);
void LabelNum(size_t id, Text label, T text, sets::Colors color);
void LabelNum(Text label, T text, uint32_t color = SETS_DEFAULT_COLOR);
void LabelNum(Text label, T text, sets::Colors color);

void LabelFloat(size_t id, Text label, float text, uint8_t dec = 2, uint32_t color = SETS_DEFAULT_COLOR);
void LabelFloat(size_t id, Text label, float text, uint8_t dec, sets::Colors color);
void LabelFloat(Text label, float text, uint8_t dec = 2, uint32_t color = SETS_DEFAULT_COLOR);
void LabelFloat(Text label, float text, uint8_t dec, sets::Colors color);

// ================= LED =================
// светодиод (value 1 включен - зелёный, value 0 выключен - красный)
void LED(size_t id, Text label, bool value);
void LED(size_t id, Text label = "");
void LED(Text label, bool value);
void LED(Text label = "");

// светодиод с цветом на выбор
void LED(size_t id, Text label, bool value, uint32_t colorOff, uint32_t colorOn);
void LED(size_t id, Text label, bool value, Colors colorOff, Colors colorOn);
void LED(Text label, bool value, uint32_t colorOff, uint32_t colorOn);
void LED(Text label, bool value, Colors colorOff, Colors colorOn);

// ================= IMAGE =================
// изображение, url или path на флешке
void Image(size_t id, Text label, Text path);
void Image(Text label, Text path);

// ================= STREAM =================
// видео с камеры ESP32-CAM
void Stream();

// ================= TEXT =================
// текстовый абзац
void Paragraph(size_t id, Text label = "", Text text = Text());
void Paragraph(Text label = "", Text text = Text());

// ================= HTML =================
// HTML
void HTML(size_t id, Text label = "", Text html = Text());
void HTML(Text label = "", Text html = Text());

// ================= TABLE =================
// таблица. CSV текст, или путь к CSV файлу .csv, или путь к бинарной таблице .tbl. Подписи - список с разделением ';'
void Table(size_t id, Text table, Text labels = Text());
void Table(Text table, Text labels = Text());

// таблица из бинарной таблицы в RAM. Подписи - список с разделением ';'
void Table(size_t id, ::Table& table, Text labels = Text());
void Table(::Table& table, Text labels = Text());

// ================= GAUGE =================
void LinearGauge(size_t id, Text label = "", float min = 0, float max = 100, Text unit = Text(), float value = NAN, uint32_t color = SETS_DEFAULT_COLOR);
void LinearGauge(size_t id, Text label, float min, float max, Text unit, float value, Colors color);
void LinearGauge(Text label = "", float min = 0, float max = 100, Text unit = Text(), float value = NAN, uint32_t color = SETS_DEFAULT_COLOR);
void LinearGauge(Text label, float min, float max, Text unit, float value, Colors color);

// ================= PLOT =================
// бегущий график. Принимает обновления вида float[]. Подписи разделяются ;
void PlotRunning(size_t id, Text labels = Text(), uint16_t period = 200);
void PlotRunning(Text labels = Text(), uint16_t period = 200);

// собирающийся график. Принимает обновления вида float[]. Подписи разделяются ;
void PlotStack(size_t id, Text labels = Text());
void PlotStack(Text labels = Text());

// график с временем точек. Требует таблицу формата [unix, y1, y2...]. Путь к таблице в FS (.tbl, .csv). Подписи разделяются ;
void Plot(size_t id, Text path = Text(), Text labels = Text());
void Plot(Text path = Text(), Text labels = Text());

// график с временем точек. Требует таблицу формата [unix, y1, y2...]. Подписи разделяются ;
void Plot(size_t id, Table& table, Text labels = Text(), bool clearTable = true);
void Plot(Table& table, Text labels = Text(), bool clearTable = true);

// таймлайн. Требует таблицу формата [unix, mask] - Mask, [unix, y1, y2...] - All, [unix, n, y] Single. Путь к таблице в FS (.tbl, .csv). Подписи разделяются ;
void PlotTimeline(size_t id, Text path, TMode mode, Text labels);
void PlotTimeline(Text path, TMode mode, Text labels);

// таймлайн. Требует таблицу формата [unix, mask] - Mask, [unix, y1, y2...] - All, [unix, n, y] Single. Подписи разделяются ;
void PlotTimeline(size_t id, Table& table, TMode mode, Text labels, bool clearTable = true);
void PlotTimeline(Table& table, TMode mode, Text labels, bool clearTable = true);

TMode = sets::TMode::Single | sets::TMode::All | sets::TMode::Mask
```

#### Активные виджеты
```cpp
// ================= INPUT =================
// ввод текста и цифр [результат - строка], подключаемая переменная - любой тип, format - описание regex
bool Input(size_t id, Text label = "", AnyPtr value = nullptr, Text regex = Text(), Text format = Text());
bool Input(Text label = "", AnyPtr value = nullptr, Text regex = Text(), Text format = Text());

// ================= NUMBER =================
// ввод цифр [результат - строка], подключаемая переменная - любой тип, можно указать минимум и максимум
bool Number(size_t id, Text label = "", AnyPtr value = nullptr, float min = NAN, float max = NAN);
bool Number(Text label = "", AnyPtr value = nullptr, float min = NAN, float max = NAN);

// ================= PASS =================
// ввод пароля [результат - строка], подключаемая переменная - любой тип
bool Pass(size_t id, Text label = "", AnyPtr value = nullptr);
bool Pass(Text label = "", AnyPtr value = nullptr);

// ================= COLOR =================
// ввод цвета [результат - 24-бит DEC число], подключаемая переменная - uint32_t
bool Color(size_t id, Text label = "", uint32_t* value = nullptr);
bool Color(Text label = "", uint32_t* value = nullptr);

// ================= SWITCH =================
// переключатель [результат 1/0], подключаемая переменная - bool
bool Switch(size_t id, Text label = "", bool* value = nullptr, uint32_t color = SETS_DEFAULT_COLOR);
bool Switch(size_t id, Text label, bool* value, Colors color);
bool Switch(Text label = "", bool* value = nullptr, uint32_t color = SETS_DEFAULT_COLOR);
bool Switch(Text label, bool* value, Colors color);

// ================= DATE =================
// дата [результат - unix секунды], подключаемая переменная - uint32_t
bool Date(size_t id, Text label = "", uint32_t* value = nullptr, float zone_hours = NAN);
bool Date(Text label = "", uint32_t* value = nullptr, float zone_hours = NAN);

// ================= TIME =================
// время [результат - секунды с начала суток], подключаемая переменная - uint32_t
bool Time(size_t id, Text label = "", uint32_t* value = nullptr);
bool Time(Text label = "", uint32_t* value = nullptr);

// ================= DATETIME =================
// дата и время [результат - unix секунды], подключаемая переменная - uint32_t
bool DateTime(size_t id, Text label = "", uint32_t* value = nullptr, float zone_hours = NAN);
bool DateTime(Text label = "", uint32_t* value = nullptr, float zone_hours = NAN);

// ================= SPINNER =================
// сипннер [результат - число], подключаемая переменная - любой тип
bool Spinner(size_t id, Text label = "", float min = 0, float max = 100, float step = 1, AnyPtr value = nullptr);
bool Spinner(Text label = "", float min = 0, float max = 100, float step = 1, AnyPtr value = nullptr);

// ================= SLIDER =================
// слайдер [результат - число], подключаемая переменная - любой тип
bool Slider(size_t id, Text label = "", float min = 0, float max = 100, float step = 1, Text unit = Text(), AnyPtr value = nullptr, uint32_t color = SETS_DEFAULT_COLOR);
bool Slider(size_t id, Text label, float min, float max, float step, Text unit, AnyPtr value, Colors color);
bool Slider(Text label = "", float min = 0, float max = 100, float step = 1, Text unit = Text(), AnyPtr value = nullptr, uint32_t color = SETS_DEFAULT_COLOR);
bool Slider(Text label, float min, float max, float step, Text unit, AnyPtr value, Colors color);

// двойной слайдер [результат - число], подключаемая переменная - любой тип
bool Slider2(size_t id_min, size_t id_max, Text label = "", float min = 0, float max = 100, float step = 1, Text unit = Text(), AnyPtr value_min = nullptr, AnyPtr value_max = nullptr, uint32_t color = SETS_DEFAULT_COLOR);
bool Slider2(size_t id_min, size_t id_max, Text label, float min, float max, float step, Text unit, AnyPtr value_min, AnyPtr value_max, Colors color);
bool Slider2(Text label = "", float min = 0, float max = 100, float step = 1, Text unit = Text(), AnyPtr value_min = nullptr, AnyPtr value_max = nullptr, uint32_t color = SETS_DEFAULT_COLOR);
bool Slider2(Text label, float min, float max, float step, Text unit, AnyPtr value_min, AnyPtr value_max, Colors color);

// ================= SELECT =================
// опции разделяются ; или \n [результат - индекс (число)]
bool Select(size_t id, Text label, Text options, AnyPtr value = nullptr);
bool Select(Text label, Text options, AnyPtr value = nullptr);

// опции разделяются ; или \n [результат - строка]
bool SelectText(Text label, Text options);

// ================= TABS =================
// опции разделяются ; или \n [результат - индекс (число)]
bool Tabs(size_t id, Text tabs, AnyPtr value = nullptr);
bool Tabs(Text tabs, AnyPtr value = nullptr);

// ================= BUTTON =================
// кнопку можно добавлять как внутри контейнера кнопок, так и как одиночный виджет
bool Button(size_t id, Text label = "", uint32_t color = SETS_DEFAULT_COLOR);
bool Button(Text label = "", uint32_t color = SETS_DEFAULT_COLOR);

bool Button(size_t id, Text label, sets::Colors color);
bool Button(Text label, sets::Colors color);

// кнопка сигналит при нажатии и отпускании, используй b.build.pressed()
bool ButtonHold(size_t id, Text label = "", uint32_t color = SETS_DEFAULT_COLOR);
bool ButtonHold(Text label = "", uint32_t color = SETS_DEFAULT_COLOR);

bool ButtonHold(size_t id, Text label, Colors color);
bool ButtonHold(Text label, Colors color);

// ================= JOYSTICK =================
// флаг center - возвращать в центр при отпускании
bool Joystick(Pos& pos, bool center = false);

// misc
// окно подтверждения, для активации отправь пустой update на его id или update с текстом подтверждения
bool Confirm(size_t id, Text label = "", bool* ptr = nullptr);

// кастомный виджет, type соответствует имени класса. params - ключи и значения
bool Custom(Text type, size_t id, const BSON& params = BSON(), AnyPtr value = nullptr);
```

### Build
Инфо о билде
```cpp
// тип билда
const Type type;

// клиент авторизован
const bool granted;

// id виджета (действие)
const size_t id;

// значение виджета (действие)
const Text value;

// состояние ButtonHold
bool pressed();

// тип - сборка виджетов
bool isBuild();

// тип - действие (обработка клика или значения)
bool isAction();
```

### Контейнеры
```cpp
// контейнер гостевого доступа
class GuestAccess(Builder& b);

// контейнер группы виджетов
class Group(Builder& b, Text title = Text());

// контейнер вложенного меню
class Menu(Builder& b, Text title);

// горизонтальный контейнер [DivType::Default | DivType::Line | DivType::Block]
class Row(Builder& b, Text title, DivType divtype = DivType::Default);

// контейнер кнопок
class Buttons(Builder& b);
```

### Updater
```cpp
// всплывающее уведомление красное
void alert(Text text);

// всплывающее уведомление зелёное
void notice(Text text);

// вызов виджета Confirm
void confirm(size_t id);

// пустой апдейт (например для вызова Confirm)
void update(size_t id);

// апдейт с float
void update(size_t id, float value, uint8_t dec = 2);

// апдейт с числом
void update(size_t id, <любой численный тип> value);

// апдейт с текстом
void update(size_t id, <любой текстовый тип> value);

// апдейт логгера
void update(size_t id, Logger& logger);

// апдейт для двойного слайдера
void update2(size_t id_min, <любой численный тип> value_min, <любой численный тип> value_max);
void update2(size_t id_min, float value_min, float value_max, uint8_t dec = 2);

// апдейт для кастом виджета, params - ключи и значения
void update(size_t id, BSON& params);

// апдейт с цветом
void updateColor(size_t id, uint32_t color);
void updateColor(size_t id, sets::Colors color);

// апдейт для Table
Updater& updateTable(size_t id, Table& table);

// апдейт для графиков из файла
Updater& updatePlot(size_t id, Text path);

// апдейт для running и stack графиков
void updatePlot(size_t id, float data[]);

// апдейт для plot графиков
void updatePlot(size_t id, Table& table, bool clearTable = true);

// апдейт для timeline графиков
void updatePlot(size_t id, Table& table, TMode mode, bool clearTable = true);

TMode = sets::TMode::Single | sets::TMode::All | sets::TMode::Mask
```

### Logger
```cpp
Logger(size_t size);

// наследует Print
void print(любые_данные);
void println(любые_данные);

static String error();
static String warn();
static String info();

// вывод в String
String toString();
```

# 2.start.md
## Установка
Библиотека доступна в менеджере библиотек Arduino и PlatformIO

### Зависимости
- [GTL](https://github.com/GyverLibs/GTL) v1.3.0+
- [GyverDB](https://github.com/GyverLibs/GyverDB) v1.3.0+
- [StringUtils](https://github.com/GyverLibs/StringUtils) v1.4.30+
- [GyverHTTP](https://github.com/GyverLibs/GyverHTTP) v1.0.26+
- [BSON](https://github.com/GyverLibs/BSON) v2.1.0+
- [Stamp](https://github.com/GyverLibs/Stamp) v1.4.0+
- [Table](https://github.com/GyverLibs/Table) v1.2.0+
- [StreamIO](https://github.com/GyverLibs/StreamIO) v1.0.5+

> [!TIP]
> При установке из реестра PIO или Arduino IDE все зависимости установятся автоматически!

Дополнительно (ставится вручную):
- [arduinoWebSockets](https://github.com/Links2004/arduinoWebSockets) для версии SettingsGyverWS/SettingsESPWS
- [ESPAsyncTCP](https://github.com/esphome/ESPAsyncTCP) для версии SettingsAsync/SettingsAsyncWS
- [ESPAsyncWebServer](https://github.com/esphome/ESPAsyncWebServer) для версии SettingsAsync/SettingsAsyncWS

<details>
<summary>platformio.ini</summary>

```ini
[env]
framework = arduino
lib_deps =
    GyverLibs/Settings
    # esphome/ESPAsyncWebServer-esphome   ; для версии SettingsAsync/SettingsAsyncWS
    # esphome/ESPAsyncTCP-esphome         ; для версии SettingsAsync/SettingsAsyncWS
    # links2004/WebSockets                ; для версии SettingsGyverWS/SettingsESPWS

[env:d1_mini]
platform = espressif8266
board = d1_mini
upload_speed = 921600
monitor_speed = 115200
monitor_filters = esp8266_exception_decoder, default
build_type = debug
board_build.filesystem = littlefs

[env:esp32dev]
monitor_speed = 115200
platform = espressif32
board = esp32dev
upload_speed = 921600
board_build.filesystem = littlefs

[env:esp32-c3]
monitor_speed = 115200
platform = espressif32
board = esp32dev
board_build.mcu = esp32c3
upload_speed = 2000000
board_build.f_cpu = 80000000L
board_build.filesystem = littlefs
```
</details>

### Пример для PIO
Есть встроенный пример для PlatformIO - `arduino_pio`: просто перетащи его в окно VS Code, библиотека и нужные платформы установятся автоматически

## Введение
### Термины
- **Вебморда** - веб-приложение, которое хостится на веб-сервере ESP и открывается в браузере
- **Виджет** - единица интерфейса вебморды (кнопка, поле ввода, слайдер)

### Как это работает
Вебморда является самостоятельным веб-приложением, написанным на html/css/js. Её файлы минифицированы, сжаты в gz и вшиты в код библиотеки как PROGMEM массив. В библиотеке настроен вебсервер, который отправляет файлы вебморды при заходе на IP платы в браузере. Лёгкий html файл подгружается каждый раз, а скрипты и стили кешируются браузером для ускорения загрузки. Вебморда общается с платой по http: например при загрузке запрашивает пакет с виджетами и прочей информацией.

### Captive portal
Во всех трёх реализациях сервера из коробки настроен DNS для работы как Captive portal - если ESP работает в режиме точки доступа (`AP` или `AP_STA`), то при подключении к точке автоматически откроется окно браузера со страницей настроек. Если это не нужно - можно отключить, запуская вебморду с флагом на отключение dns: `begin(false)`.

### MDNS
В `begin()` можно передать домен для удобного доступа в локальной сети: `begin(true, "my_settings")`. Здесь `true` запустит режим captive portal (если нужен), а строка `"my_settings"` запустит MDNS сервер для доступа к устройству по адресу `my_settings.local`, помимо прямого доступа по IP платы.

### Приложение для поиска
Позволяет находить устройства с библиотекой в локальной сети и заменяет браузер, вебморда открывается сразу в приложении, кнопка назад возвращает к списку устройств. Чтобы удалить устройство - долгое удержание на нём на смартфоне или правой кнопкой мыши на ПК. Для поиска смартфон/ПК должны быть в одной локальной сети с устройством. В приложении должна быть указана корректная маска подсети (настраивается в роутере). Если в роутере она не менялась - то она там стандартная *255.255.255.0*, как и в приложении по умолчанию.

- [Скачать .apk](https://github.com/GyverLibs/Settings-discover/releases/latest/download/Settings.apk
) последней версии
- [Скачать .html](https://github.com/GyverLibs/Settings-discover/releases/latest/download/index.html) последней версии

## Минимальный пример
```cpp
#include <Arduino.h>

#define WIFI_SSID ""
#define WIFI_PASS ""

#include <SettingsGyver.h>
SettingsGyver sett("My Settings");

void build(sets::Builder& b) {
}

void setup() {
    Serial.begin(115200);
    Serial.println();

    // wifi
    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFI_SSID, WIFI_PASS);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println();
    Serial.print("Connected: ");
    Serial.println(WiFi.localIP());

    // settings
    sett.begin();   // begin(false) если не нужен captive
    sett.onBuild(build);
}

void loop() {
    sett.tick();
}
```

Вместо подключения к AP можно использовать режим точки доступа:

```cpp
WiFi.mode(WIFI_AP);
WiFi.softAP("My Device");
```

> [!WARNING]
> Вызов `sett.begin()` должен осуществляться после настройки режима WiFi

## База данных
Библиотека интегрирована с [GyverDB](https://github.com/GyverLibs/GyverDB) - относительно быстрой базой данных для хранения данных любого типа. В данном случае она используется для хранения "настроек" - значений виджетов вебморды: Settings автоматически читает и обновляет данные в БД. Рекомендуется изучить как работать с БД на странице описания GyverDB по ссылке выше. При использовании `GyverDBFile` база данных будет автоматически записываться в файл при изменениях с браузера, а файловая система позаботится об оптимальном износе Flash памяти.

При запуске нужно **инициализировать** БД, указав ключи и соответствующие им начальные значения и типы. Эти значения будут записаны только в том случае, если запись в БД ещё не существует, т.е. при первом запуске и при добавлении новых записей. В то же время автоматическое обновление БД работает только для существующих записей, т.е. Settings будет работать только с сущестующими ячейками и не создаст новых.

Минимальный пример:

```cpp
#include <LittleFS.h>
#include <GyverDBFile.h>
GyverDBFile db(&LittleFS, "/data.db");  // создать БД в файле

#include <SettingsGyver.h>
SettingsGyver sett("My Settings", &db);   // подключить БД

// объявить хэш-ключи БД через макрос
DB_KEYS(
    keys,
    input,
    slider
);

void setup() {
    // подключение к WiFi...

    // settings
    sett.begin();

    // запуск файловой системы
#ifdef ESP32
    LittleFS.begin(true); // format on fail
#else
    LittleFS.begin();
#endif

    // запуск БД и чтение из файла
    db.begin();
    
    // инициализация БД начальными значениями
    db.init(keys::input, "text");
    db.init(keys::slider, 30);

    // или через макрос инициализации
    // DB_INIT(
    //     db,
    //     (keys::input, "text"),
    //     (keys::slider, 30)
    // );

    // чтение из БД
    Serial.println(db[keys::input]);
    int sld = db[keys::slider];
}

void loop() {
    sett.tick();    // вызывать в loop
}
```

### Несколько БД
Можно использовать несколько баз данных, например одна для сохраняемых в память настроек, вторая для "временных" настроек, которые не нужно сохранять при перезагрузке: `GyverDBFile` сохраняет в файл, а обычная `GyverDB` - нет, живёт чисто в оперативной памяти. Переключаться между БД нужно в билдере таким образом, чтобы после смены БД шли только виджеты с ключами из этой БД. Например

```cpp
GyverDBFile db_flash(&LittleFS, "/data.db");
GyverDB db_ram;

void build(sets::Builder& b) {
    settings.attachDB(&db_ram);
    b.Input("input2"_h, "...");

    settings.attachDB(&db_flash);
    b.Input("input1"_h, "...");
}
```

> После выхода из билдера нужно оставлять подключенной ту БД, для которой нужны автоматические обновления, система не сможет обновляться одновременно с нескольких БД. Также нужно оставлять последней подключенной БД, которая пишет на флешку, чтобы система автоматически вызывала её тикер.

## Файловый менеджер
Библиотека нативно поддерживает бортовую флэш-память с файловой системой `LittleFS`, список файлов выводится в меню при нажатии на кнопку в углу справа. Файлы можно изменять, удалять, скачивать и загружать. Для корректной работы нужно самостоятельно запустить файловую систему в блоке `setup`, если она нужна:

```cpp
void setup() {
#ifdef ESP32
    LittleFS.begin(true); // format on fail
#else
    LittleFS.begin();
#endif
}
```

### SD карта
Библиотека также поддерживает внешнюю SD карту в паре со встроенной флешкой - в файловом менеджере файлы с SD карты выводятся начиная с пути `/sd/`: это **виртуальный путь** - на самой карте они хранятся без него. Если загрузить через менеджер файл по пути `/sd/file.txt`, то на самой SD карте он будет записан просто как `file.txt`.

В программе также используется виртуальный путь - это позволяет работать с файлами не выбирая вручную файловую систему - библиотека сделает это сама. Например для вывода графиков:

```cpp
void build(sets::Builder& b) {
    b.Plot("/plot2.csv");     // из flash
    b.Plot("/sd/plot2.csv");  // из SD
}
```

Для запуска SD карты нужно:

```cpp
// подключить библиотеку
#ifdef ESP8266
#include <SDFS.h>
#else  // ESP32
#include <SD.h>
#endif

void setup() {
    // wifi, settings...

#ifdef ESP8266
    LittleFS.begin();

    // ESP8266 SPI
    // MOSI     MISO    CLK     CS
    // D7(13)   D6(12)  D5(14)  D2(4) default!
    SPI.begin();

    // карта подключена к SPI(MOSI/MISO/CLK) + CS на пине D8 (по умолчанию там D4)
    SDFSConfig cfg(D8);
    SDFS.setConfig(cfg);

    SDFS.begin();
    // sett.fs.setFS(LittleFS, SDFS);  // подключение обеих FS
    sett.fs.sd.setFS(SDFS); // подключение SD
#else
    LittleFS.begin(true);

    // ESP32 SPI
    // xSPI     MOSI    MISO    CLK     CS
    // HSPI     13      12      14      15
    // VSPI     23      19      18      5
    SPI.begin();

    // карта подключена к VSPI (по умолч. SPI=VSPI)
    SD.begin(5);

    // sett.fs.setFS(LittleFS, SD);  // подключение обеих FS
    sett.fs.sd.setFS(SD); // подключение SD
#endif
}
```

После этого карта доступна в программе и в вебморде.

### Список файлов
Реализован удобный вывод списка файлов:

```cpp
String s;

// sett.fs.flash.listDir();    // вывести список файлов flash
// sett.fs.sd.listDir();       // вывести список файлов sd (без префикса /sd/)
// sett.fs.listDir();          // вывести общий список файлов
```

Список выводится с разделением `;`. Это позволяет например передать его в виджет `Select`:

```cpp
void build(sets::Builder& b) {
    // селект с файлами
    String s = sett.fs.flash.listDir();
    b.Select("", s);
}
```

Для определения выбранного пути нужно парсить список по разделителю, например встроенным парсером `Text`:

```cpp
void build(sets::Builder& b) {
    static uint8_t file;

    String s = sett.fs.flash.listDir(s);
    
    if (b.Select("", s, &file)) {
        // выводим выбранный файл при выборе
        String sel = Text(s).getSub(file, ';').toString();
        Serial.println(sel);
    }
}
```

# 3.builder.md
## Билдер и виджеты
Пакет с **виджетами** собирается устройством в **билдере** - функция в программе, которая вызывается, когда приходит запрос от вебморды. Внутри билдера нужно вызвать методы виджетов в том порядке, в котором они должны находиться в вебморде:

```cpp
// минимальный код
SettingsGyver sett;

// билдер
void build(sets::Builder& b) {
    // b.Input(...);
    // b.Button(...);
}

void setup() {
    // подключение к WiFi...

    sett.begin();
    sett.onBuild(build);
}

void loop() {
    sett.tick();
}
```

### ID виджета
У всех виджетов есть вариант функции с ID и без ID. ID виджета нужен для:
- Работа с подключенной базой данных на чтение и запись значений
- Отправка обновлений на виджет
- Разбор действий отдельно от вывода виджетов, чтобы разделить UI и обработку

ID в библиотеке задаётся числом, точно так же как в GyverDB. Для читаемости кода и подсказок IDE удобнее всего задавать ID ключами `DB_KEYS`, как и для базы данных. **Виджеты и база данных - единое целое**, виджет берёт и пишет значение в БД, а мы можем потом прочитать это значение в другом месте в программе.

> Если ID не задан (**анонимный виджет**) - он будет присваиваться библиотекой автоматически (только для активных виджетов). Автоматический ID - это число от `UINT32_MAX`, уменьшается на 1 с каждым вызовом. Если автоматический ID совпадёт с каким-то из вручную заданных - в вебморде высветится ошибка `Duplicated ID`.

```cpp
DB_KEYS(
    kk,
    my_inp,
    button
);

void build(sets::Builder& b) {
    b.Input("My input");                // без ID
    b.Input("my_inp"_h, "My input");    // хэш-строка
    b.Input(SH("my_inp"), "My input");  // хэш-строка
    b.Input(H(my_inp), "My input");     // хэш-строка
    b.Input(kk::my_inp, "My input");    // GyverDB-хэш
}
```

### Взаимодействие с виджетами
Есть несколько способов взаимодействия с виджетами, т.е. отправки и получения значений:
- У виджета можно задать ID, по которому библиотека будет автоматически читать и писать данные в базу данных GyverDB при загрузке вебморды и получения новых значений с неё соответственно. Получить значение можно из любого места в программе, обратившись к БД
- К виджету можно подключить обычную переменную - библиотека будет читать из неё значение и писать при изменениях с вебморды. К БД в этом случае не будет обращений даже при заданном ID
- У виджета без ID и переменной будет значение по умолчанию (0 или пустая строка). Новое значение с вебморды никуда не запишется, но можно прочитать его в момент получения из инфо о билде
- Активный виджет (значение можно менять из вебморды, функция виджета возвращает `bool`) возвращает `true` при изменении значения пользователем и при клике по кнопке

```cpp
String str;
char cstr[20];

void build(sets::Builder& b) {
    // виджет без id и начального значения
    // При установке с вебморды получаем значение напрямую
    if (b.Input("My input")) {
        Serial.println(b.build.value);
    }

    // виджет без id с привязанной String-строкой
    // при установке с вебморды значение запишется в строку
    b.Input("My input", &str);
    b.Input("My input", AnyPtr(cstr, 20));  // для char-массивов

    // виджет с id без привязанной переменной
    // будет работать с базой данных по указанному ключу
    b.Input("my_inp"_h, "My input");

    // действие возвращается независимо от наличия id
    if (b.Button()) Serial.println("btn 1");
    if (b.Button("my_btn2"_h)) Serial.println("btn 2");
}
```

#### Инфо о билде
```cpp
void build(sets::Builder& b) {
    // можно узнать, было ли действие по виджету
    if (b.build.isAction()) {
        Serial.print("Set: 0x");
        Serial.print(b.build.id, HEX);
        Serial.print(" = ");
        Serial.println(b.build.value);
    }
}
```

#### Разделение UI и действий
```cpp
void build(sets::Builder& b) {
    // вывод UI
    b.Input("my_inp"_h, "My input");
    b.Button("my_btn"_h, "My button");

    // обработка действий
    switch (b.build.id) {
        case "my_inp"_h:
            Serial.print("input: ");
            Serial.println(b.build.value);
            break;

        case "my_btn"_h:
            Serial.println("btn click");
            break;
    }
}
```

> Если ID виджета задан и переменная не привязана - будет использоваться БД. Если привязана переменная - будет использоваться она

### Динамические виджеты
Виджеты собираются линейно, вызов функции виджета добавляет его в вебморду. Это означает, что виджеты можно выводить и динамически, особенно удобно это работает с автоматическим id. Например:

```cpp
int numbers[5];

void build(sets::Builder& b) {
    // вывод в цикле
    for (int i = 0; i < 5; i++) {
        b.Input();
    }
    
    // обработка действий также будет работать
    for (int i = 0; i < 5; i++) {
        if (b.Input()) Serial.println(b.build.value);
    }
    
    // массив number с привязанными переменными
    for (int i = 0; i < 5; i++) {
        b.Number(String("number #") + i, &numbers[i]);
    }

    // обработка и действий
    for (int i = 0; i < 5; i++) {
        if (b.Number(String("number #") + i, &numbers[i])) {
            Serial.print(String("number #") + i + ": ");
            Serial.println(numbers[i]);
        }
    }

    // можно и так
    for (int i = 0; i < 5; i++) {
        b.Number(String("number #") + i, &numbers[i]);

        if (b.wasSet()) {
            Serial.print(String("number #") + i + ": ");
            Serial.println(numbers[i]);
            b.clearSet();
        }
    }
}
```

Также можно динамически скрывать виджеты, например по флагу:

```cpp
void build(sets::Builder& b) {
    if (flag) {
        b.Input();
        b.Slider();
        // ...
    }
}
```

Частым сценарием является открытие группы настроек с активацией режима, это можно сделать так:

```cpp
void build(sets::Builder& b) {
    if (b.Switch()) {
        b.reload(); // перезагрузить вебморду по клику на свитч
    }

    // здесь flag должен быть прочитан из БД или переменной
    if (flag) {
        b.Input();
        b.Slider();
        // ...
    }
}
```

Например с БД

```cpp
DB_KEYS(
    kk,
    mode_sw
);

void build(sets::Builder& b) {
    // запись в БД и перезагрузка
    if (b.Switch(kk::mode_sw)) b.reload();

    // чтение из БД
    if (db[kk::mode_sw]) {
        b.Input();
        b.Slider();
        // ...
    }
}
```

### Динамические ID
Если нужны динамические виджеты с привязкой к БД и автоматическим генерированием имён с индексами в цикле, то нужно сложить строку (например через String) и взять у неё хэш:

```cpp
for (int i = 0; i < 5; i++) {
    b.Switch(SH( (String("switch") + i).c_str() ));
}
```

Также можно использовать библиотеку [StringN](https://github.com/GyverLibs/StringN) - она работает в статической памяти и многократно быстрее String, а также сама умеет считать хэш:

```cpp
for (int i = 0; i < 5; i++) {
    b.Switch((String8("switch") + i).hash());
}
```

БД умеет работать со строками напрямую и сама берёт у них хэш:

```cpp
for (int i = 0; i < 5; i++) {
    db.init(String("switch") + i);
}
```

### Иконки лейблов
Можно использовать emoji, они неплохо смотрятся в меню. Например с [удобного сайта](https://symbl.cc/ru/emoji/)

```cpp
b.Input(kk::intw, "🔈Громкость");
```

# 4.widgets.md
## Пассивные виджеты
### Label, LabelNum, LabelFloat
Виджет для отображения текста или цифры. Значение обновляется через `update`, поддерживает изменение цвета через `updateColor`.

### LED
Светодиод, имеет два цвета. Состояние переключает между этими цветами, по умолчанию красный и зелёный, можно задать свои два цвета. Значение состояния обновляется через `update`, также поддерживает изменение цвета напрямую через `updateColor` независимо от состояния.

### Image
Вывод изображения:
- Из Интернета - ссылка начинается с `http`
- Из Flash-памяти - ссылка начинается с `/`

При отправке обновления `update` изображение будет обновлено на новый url.

### Paragraph
Вывод строки текста.

### HTML
Вывод кода в HTML разметке:

```cpp
b.HTML("", R"(<a href="http://google.com">Google</a>)");
```

### Stream
Для запуска стрима с ESP32-CAM нужно подключить `SettingsCamera.h`, в нём можно настроить тип камеры и подключение. Для плат ESP32-CAM AiThinker ничего трогать не нужно. Для запуска стрима нужно инициализировать камеру и запустить стрим, он будет выводиться в виджет `Stream`:

```cpp
bool sets::cameraInit(framesize_t frame_size = FRAMESIZE_VGA, pixformat_t pixel_format = PIXFORMAT_JPEG, int jpeg_quality = 12);
void sets::streamBegin(uint16_t fps = 30, uint16_t port = 82, const char* path = "/stream");
void sets::streamEnd();
```

```cpp
#include <SettingsCamera.h>

void build(sets::Builder& b) {
    b.Stream();
}

void setup() {
    sets::cameraInit();
    sets::streamBegin();
}
```

### Link
Виджет-ссылка, открывает ссылку в новой вкладке.

### Log
Готовый инструмент для ведения логов и отправки в вебморду (почти Web-Serial) - `Logger`:

```cpp
sets::Logger logger(150);   // размер буфера

void build(sets::Builder& b) {
    b.Log(H(log), logger);

    if (b.Button("Test")) {
        // печатать как в Serial в любом месте в программе
        logger.println(millis());
    }
}

void update(sets::Updater& upd) {
    // отправить лог
    upd.update(H(log), logger);
}
```

Логгер автоматически окрашивает строки в цвет статуса, если он передан (указыается в начале строки):

- Не указан - цвет темы
- `info:` - чёрный цвет
- `warn:` - оранжевый цвет
- `err:` - красный цвет

Например `logger.println("warn: some warning);`. Также есть готовые строки, функция возвращает `String` с нужным префиксом:

```cpp
logger.println(sets::Logger::info() + "info text");
logger.println(sets::Logger::warn() + "warn text");
logger.println(sets::Logger::error() + "error text");
```

### Table
Таблица. Передаётся в формате CSV строкой или как путь к файлу на флешке:
- С расширением `.csv` - CSV, горизонтальный разделитель `;`, вертикальный `\n`. Внутри ячеек использование разделителей не допускается
- С расширением `.tbl` - бинарная таблица [Table](https://github.com/GyverLibs/Table)

Подписи - список с разделением `;`.

Может обновляться, даже из файла - отправить в апдейт путь к файлу.

### LinearGauge
Линейная шкала с заполнением, обновляется через апдейт.

## Графики
- У всех вариантов неограниченное количество осей
- Все могут обновляться в реальном времени
- Виджеты графиков поддерживают загрузку данных напрямую из файла с таблицей в формате:
  - Текстовая CSV таблица (разделитель столбцов `;`, строк - `\n`) с расширением `.csv`
  - Бинарная таблица из библиотеки [Table](https://github.com/GyverLibs/Table) с расширением `.tbl`

> [!TIP]
> Если график хранится в файле бинарной таблицы с расширением `.tbl`, то при скачивании его из файлового менеджера он будет конвертирован в читаемый `.csv`

> [!TIP]
> График из файла может обновляться по пути к файлу - надо отправить путь в апдейт

### Названия осей
Названия осей передаются в виде списка с разделителем `;` - `"axis 1;test;test 2"`. Дополнительно для графиков линий:

- Единицы измерения опционально добавляются в конце названия оси в квадратных скобках: `"Value;Temp[°C];USD[ $]"`
- Линию можно сделать пунктирной - для этого нужно добавить тире перед названием оси. Чем больше тире, тем длиннее штрихи: `"-Value;Temp;--USD"`

### Формат времени
Графики Plot и Timeline выводят данные по указанному времени. Это время может быть:

- Unix в секундах (32 бит) или миллисекундах (64 бит) - на графике будет отображаться дата и время точек. Первая точка должна быть отправлена с ненулевым unix
- Если первая точка графика отправлена с нулевым временем `0` - график будет ожидать время в целых миллисекундах и отображаеть на оси в дробных секундах без даты, начиная с 0 секунд. Это удобно, если нужно построить какой-то короткий процесс, не привязанный к реальному времени

### PlotRunning
График с линиями. Данные передаются через апдейт, между апдейтами график двигается с заданной скоростью и показывает предыдущие значения осей.

```cpp
// билдер
b.PlotRunning(H(run), "kek1;kek2");

// апдейт по запросу или через вебсокет
float v[] = {random(100), random(100)};
sett.updater().updatePlot(H(run), v);

// или так
sett.updater().updatePlot(H(run), (const float[]){random(100), random(100)});
```

### PlotStack
График с линиями. Данные передаются через апдейт, график обновляется при получении данных.

```cpp
// билдер
b.PlotStack(H(stack), "kek1;kek2;kek3");

// апдейт по запросу или через вебсокет
float v[] = {random(100), random(100), random(100)};
sett.updater().updatePlot(H(stack), v);

// или так
sett.updater().updatePlot(H(stack), (const float[]){random(100), random(100), random(100)});
```

### Plot
График с линиями. Первый столбец таблицы - unix-время, остальные - значения осей:

```cpp
время   значения...
unix1    v1  v2..
unix2    v1  v2..
unix3    v1  v2..
```

```cpp
b.Plot(H(plot1), "/plot.tbl");
b.Plot(H(plot2), "/table.csv");

// TableFile t(&LittleFS, "/plot.tbl");
// t.begin();
// b.Plot(H(plot3), t);
```

### PlotTimeline
График с состояниями осей вкл/выкл в виде блоков. Первый столбец таблицы - unix-время, остальные - значения осей. Есть три формата данных:

1. Режим `sets::TMode::All`, **остальные** столбцы - состояния (1 или 0) всех осей по одному в столбце:

```cpp
время   значения...
unix1    1 0 1..
unix2    0 0 1..
unix3    1 1 0..
```

2. Режим `sets::TMode::Mask`, **второй** столбец - состояния всех осей в виде битовой маски (1-64 бит), *младший бит - первая ось*:

```cpp
время   значения
unix1    0b1010
unix2    0b0010
unix3    0b1000
```

3. Режим `sets::TMode::Single`, **второй** столбец - номер оси, **третий** - состояние (1 или 0):

```cpp
время   ось значение
unix1    1  1
unix2    2  1
unix3    0  0
```

```cpp
b.PlotTimeline("/tline.csv", sets::TMode::All, "1;2;3;4");
b.PlotTimeline("/tline_mask.csv", sets::TMode::Mask, "1;2;3;4");
b.PlotTimeline("/tline_per.csv", sets::TMode::Single, "1;2;3;4");
```

#### Table
`Table` - класс для удобного создания и редактирования динамических таблиц со столбцами разных типов. Использовать очень просто:

```cpp
// таблица с временем и двумя float столбцами (3 столбца, 0 строк)
Table t(0, 3, cell_t::Uint32, cell_t::Float, cell_t::Float);

// прибавить строки
t.append(unix1, random(100), random(100));
t.append(unix2, random(100), random(100));
```

И теперь её можно отправлять.

#### TableFileStatic
Для ведения долгосрочных логов и построения графика гораздо интереснее использовать `TableFileStatic` - эта таблица хранится в файле и не загружается в оперативную память, что позволяет не ограничивать её размер объёмом оперативки и хранить большие объёмы данных (сотни килобайт), а виджет в свою очередь просто скачивает файл. Этот тип таблиц позволяет прибавлять к себе новые строки, сохраняя настроенный лимит на количество строк, например хранить данные о температуре за последние 3 месяца (чтобы файл не увеличивался до бесконечности).

```cpp
void build(sets::Builder& b) {
    b.Plot(H(plot1), "/file_plot1.tbl");
}

// условно вызывается каждую минуту
void everyMinute() {
    TableFileStatic t(&LittleFS, "/file_plot1.tbl", 100);   // макс. 100 строк, будет смещаться при append()

    // инициализация, должна быть вызвана хотя бы один раз после непосредственного создания файла
    t.init(3, cell_t::Uint32, cell_t::Float, cell_t::Int8);

    // добавление в файл
    t.append(sett.rtc.getUnix(), (random(100) - 50) / 2.0, random(-100, 100));
}
```

## Активные виджеты
### Input
Ввод текста. Поддерживает регулярные выражения и комментарий при ошибке ввода:

```cpp
b.Input("");
b.Input("", nullptr, R"(^\d+$)");
b.Input("", nullptr, R"(^\d+$)", "Только цифры");
```

### Pass
Ввод пароля.

### Number
Ввод цифр.

### Color
Колор-пике, принимает и отправляет цвет в 24-битном формате RRGGBB.

### Switch
Переключатель. поддерживает изменение цвета через `updateColor`.

### Date, DateTime
Дата и дата-время, принимает и отправляет unix-секунды (GMT+0). В браузере выводится с учётом часового пояса браузера, также локальный часовой пояс можно указать вручную.

### Time
Принимает и отправляет время в секундах с начала суток независимо от часового пояса.

### Spinner
Как Number, но с кнопками + и -, увеличивают значение на заданный шаг.

### Slider
Слайдер для ввода значений, при движении отправляет значения с указанным в настройках вебморды периодом. Строка результата кликабельная, можно задать значение вручную - подчиняется настройкам min/max/step.

### Slider2
Двойной слайдер, имеет два ID для минимума и максимума, переменных тоже можно подключить две. Обновляется через метод `update2`.

### Select
Всплывающий список выбора опции, принимает и отправляет индекс опции (начиная с `0`):

- Названия опций передаются в виде строки с разделителем `;`: `"option 1;option 2;my option"`
- Опции можно группировать - имя группы заключается в квадратные скобки, список **должен** начинаться с группы: `"[group 1]option 1;option 2[group2]my option"`
- Опции можно скрывать из списка с сохранением индексации - для этого название опции должно начинаться с `~`: `"option 1;~option 2;my option"` (option 2 будет скрыта)
- Группы тоже можно скрывать из списка с сохранением индексации опций - имя группы должно начинаться с `~`: `"[group 1]option 1;option 2[~group2]my option"` (group2 будет скрыта)

> [!TIP]
> Список опций (в том числе в группе) может заканчиваться `;` - пустая опция добавлена не будет. Это позволяет удобно "собирать" список опций, прибавляя к строке опций `"опция;"` (сразу с разделителем на конце), например `"опция;опция;опция;"`

### SelectText
То же самое что Select, но является просто выбором из списка, не хранит выбранный пункт - просто отправляет его. Прочитать можно в `b.build.value` - `if (b.SelectText("", "foo;bar;option")) Serial.println(b.build.value);`.

Например вот так можно сделать выбор файла и открытие при выборе:

```cpp
if (b.SelectText("Select file", sett.fs.listDir())) {
    File f = sett.fs.openRead(b.build.value.c_str());
    Serial.print("File ");
    Serial.print(b.build.value);
    Serial.print(" size ");
    Serial.println(f.size());
}
```

### Tabs
Вкладки, принимает и отправляет индекс вкладки (начиная с 0). Имена вкладок передаются в виде строки с разделителем `;`: `"tab 1;tab 2;my tab"`. Если вкладок слишком много - их можно перемещать пальцем и курсором. Вернёт `true` при клике по вкладке. Далее в программе можно строить билдер по условиям или в `switch` исходя из значения вкладки.

```cpp
void build(sets::Builder& b) {
    static uint8_t tab; // статическая

    if (b.Tabs("Slider;Button;Input", &tab)) {
        // при нажатии перезагружаемся и выходим
        b.reload();
        return;
    }

    if (tab == 0) {
        b.Slider();
    } else if (tab == 1) {
        b.Button();
    } else if (tab == 2) {
        b.Input();
    }
}
```

Пример с использованием `enum` для читаемости кода:

```cpp
void build(sets::Builder& b) {
    enum Tabs : uint8_t {
        Slider,
        Button,
        Input,
    } static tab;

    if (b.Tabs("Slider;Button;Input", (uint8_t*)&tab)) {
        // при нажатии перезагружаемся и выходим
        b.reload();
        return;
    }

    switch (tab) {
        case Tabs::Slider:
            b.Slider();
            break;
            
        case Tabs::Button:
            b.Button();
            break;

        case Tabs::Input:
            b.Input();
            break;
    }
}
```

### Button
Кнопка. Можно обновлять текст на кнопке через `update` и цвет через `updateColor`. функция вернёт `true` при клике по кнопке.

```cpp
if (b.Button()) {
    Serial.println("Click!");
}
```

### ButtonHold
Кнопка с двумя состояниями. Можно обновлять текст на кнопке через `update` и цвет через `updateColor`. Функция вернёт `true` при нажатии и при отпускании. Для определения состояния нужно опросить `b.build.pressed()`.

```cpp
if (b.ButtonHold()) {
    Serial.println(b.build.pressed());
}
```

### Confirm
Всплывающее окно подтверждения. Функция вернёт `true` при любом выборе юзера. Для определения что именно выбрал юзер можно опросить `b.build.value.toBool()` или подключить `bool` переменную. Для вызова окна нужно отправить обновление с id виджета:

- Если отправить обновление `upd.confirm(id)` - вызовется окно с текстом, заданным в билдере
- Если отправить `upd.update(id, текст)` - вызовется окно с текстом, указанным в апдейте, а текст виджета обновится

```cpp
// вызов Confirm по кнопке
bool cfm_f;

void build(sets::Builder& b) {
    bool res;
    if (b.Confirm(kk::conf, "Confirm", &res)) {
        Serial.println(res);
        // Serial.println(b.build.value.toBool());
    }

    if (b.Button()) cfm_f = true;
}

void update(sets::Updater& u) {
    if (cfm_f) {
        cfm_f = false;
        u.confirm(kk::conf);
    }
}
```

### Joystick
Активный джойстик, принимает переменную для хранения позиции типа `sets::Pos`, которая содержит поля `x` и `y` с координатами от `-255` до `255`. Вернёт `true`, если было изменение:

```cpp
sets::Pos pos;

void builder() {
    b.Joystick(pos);
}

void loop() {
    if (pos) {
        Serial.print(pos.x);
        Serial.print(',');
        Serial.println(pos.y);
    }
}
```

# 5.containers.md
## Контейнеры
Виджеты можно объединять в контейнеры. Контейнер нужно начать и закончить, так как пакет данных собирается линейно в целях оптимизации скорости и памяти.

Метод `beginКонтейнер` всегда вернёт true для красоты организации кода в блоке условия:

```cpp
void build(sets::Builder& b) {
    if (b.beginКонтейнер()) {
        // виджеты...

        b.endКонтейнер();  // закрыть контейнер
    }
}
```

Второй вариант - у всех контейнеров есть парный класс, который сам откроет и закроет контейнер. Нужно создать объект с любым именем и передать ему билдер:

```cpp
void build(sets::Builder& b) {
    {
        sets::Контейнер g(b);  // должен быть первым в блоке

        // виджеты...

    } // автоматически закроется здесь
}
```

### Группа
Объединяет виджеты по вертикали с общим фоном и заголовком:

```cpp
void build(sets::Builder& b) {
    if (b.beginGroup("Group 1")) {
        b.Input();

        b.endGroup();  // закрыть группу
    }
}
```

### Меню
Можно создавать вложенные меню. Указанный заголовок будет отображаться на кнопке и в заголовке страницы при входе на меню. Все виджеты и группы, находящиеся в блоке с меню, будут находиться на отдельной странице. Вложенность меню неограниченная:

```cpp
void build(sets::Builder& b) {
    b.Input();

    {
        sets::Menu g(b, "Submenu");

        b.Input();
    }
}
```

Когда пользователь входит в меню - вызывается билдер, для того чтобы можно было например обновить некоторые поля внутри этого меню. Для опроса события входа используется `b.enterMenu()`:

```cpp
{
    sets::Menu m(b, "menu 1");
    if (b.enterMenu()) Serial.println("menu 1");
    // b.Input();
}
{
    sets::Menu m(b, "menu 2");
    if (b.enterMenu()) Serial.println("menu 2");
    // b.Input();
    {
        sets::Menu m(b, "menu 2.1");
        if (b.enterMenu()) Serial.println("menu 2.1");
        // b.Input();
    }
}
```

### Строка
Можно располагать виджеты горизонтально в строку, у них может быть общее название. Вне группы строка получит белый фон. Если у виджета задано название - он будет пытаться растянуться на всю ширину, если нет - то не будет. Частый вариант использования - первый виджет с названием, остальные мелкие без:

```cpp
void build(sets::Builder& b) {
    {
        sets::Row g(b);
        // sets::Row g(b, "Row");

        b.Slider("Slider");
        b.LED();
        b.Switch();
    }
}
```

У строки **вне группы** есть три стиля:

```cpp
void build(sets::Builder& b) {
    // разные стили Row ВНЕ ГРУППЫ
    if (b.beginRow("", sets::DivType::Default)) {
        b.Switch("Switch");
        b.Switch("Switch");
        b.endRow();
    }
    if (b.beginRow("", sets::DivType::Block)) {
        b.Switch("Switch");
        b.Switch("Switch");
        b.endRow();
    }
    if (b.beginRow("", sets::DivType::Line)) {
        b.Switch("Switch");
        b.Switch("Switch");
        b.endRow();
    }
}
```

### Кнопки
Отдельный тип контейнера - кнопки, внутри него можно добавлять только кнопки. Вне группы у них будет прозрачный фон:

```cpp
void build(sets::Builder& b) {
    {
        sets::Buttons btns(b);

        // кнопка вернёт true при клике
        if (b.Button("Button 1")) {
            Serial.println("Button 1");
        }

        if (b.Button("Button 2", sets::Colors::Blue)) {
            Serial.println("Button 2");
        }
    }
}
```

Если группа кнопок или одиночная кнопка является последней в группе - у кнопки будет другой стиль:

```cpp
void build(sets::Builder& b) {
    {
        sets::Group g(b);
        {
            sets::Buttons g(b);
            b.Button();
            b.Button();
            b.Button();
        }
        b.Button();
    }
    {
        sets::Group g(b);
        {
            sets::Row g(b);
            b.Button();
            b.Button();
            b.Button();
        }
        {
            sets::Buttons g(b);
            b.Button();
            b.Button();
            b.Button();
        }
    }
    {
        sets::Buttons g(b);
        b.Button();
        b.Button();
        b.Button();
    }
    {
        sets::Row g(b);
        b.Button();
        b.Button();
        b.Button();
    }
    b.Button();
}
```

### Авторизация
В системе предусмотрена авторизация: если в прошивке указать отличный от пустой строки пароль - вебморда будет работать в "гостевом" режиме: отображаются только разрешённые гостям виджеты, файловый менеджер и OTA скрыты и заблокированы. Для ввода пароля нужно зайти в меню (правая верхняя кнопка) и нажать на ключик. Серый ключик означает что авторизация отключена, зелёный - клиент авторизован, красный - неверный пароль. Пароль может содержать любые символы и иметь любую длину - в явном виде он не хранится и не передаётся. Пароль сохраняется в браузере и авторизация работает автоматически при перезагрузке страницы.

Для разделения админского и гостевого доступа предусмотрен виртуальный контейнер Guest. Если пароль установлен и клиент не авторизован - он будет видеть только виджеты из гостевых контейнеров. Для корректной работы гостевой контейнер не должен прерываться обычными контейнерами. Пример:

```cpp
void setup() {
    // ...
    // sett.setPass("pass1234");
    sett.setPass(F("pass1234"));  // любая строка
}

void build(sets::Builder& b) {
    if (b.beginGroup("Group 1")) {
        // гости не видят
        b.Pass(kk::pass, "Password");

        // виджеты, которые видят гости и админы
        {
            sets::GuestAccess g(b);
            b.Input(kk::uintw, "uint");
            b.Input(kk::intw, "int");
            b.Input(kk::int64w, "int 64");
        }

        // гости не видят
        {
            sets::Menu m(b, "sub sub");
            b.Label(kk::lbl2, "millis()", "", sets::Colors::Red);
        }

        b.endGroup();
    }
}
```

В гостевой контейнер можно поместить несколько обычных контейнеров, например групп.

> Примечание: если вложенное меню закрыто от гостей, но содержит ещё одно вложенное меню - кнопка открытия меню будет отображаться, но само меню будет пустым

# 6.updates.md
## Обновления
В системе реализован механизм обновлений - вебморда периодически запрашивает "обновления" у устройства. Если база данных подключена - то при изменениях значений в базе где то в программе библиотека **автоматически отправит новые значения** в вебморду (например если какое то значение изменилось при помощи кнопки).

> Примечание: если вебморда открыта одновременно с нескольких браузеров - обновления базы данных получит только тот из них, который запросил их первым. Также можно отправить свои значения, если база данных не подключена или не используется для каких-то виджетов. Для этого нужно подключить обработчик обновлений и вручную отправить данные по id виджета

Отправка обновлений вручную на лейблы:

```cpp
void build(sets::Builder& b) {
    b.Label("lbl1"_h, "Random");
    b.Label("lbl2"_h, "millis()", "", sets::Colors::Red);
}
void update(sets::Updater& upd) {
    upd.update("lbl1"_h, random(100));
    upd.update("lbl2"_h, millis());
}

void setup() {
    sett.begin();
    sett.onBuild(build);
    sett.onUpdate(update);
}

void loop() {
    sett.tick();
}
```

> [!WARNING]
> В функции `update` нельзя складывать строки, либо результат нужно преобразовать к String: `upd.update(id, (String)(str + 123 + "abc"));`. Проблема в несовместимости String API между ядрами esp разных версий

### Обновление цвета
Если у виджета в настройках есть цвет - этот цвет можно обновить в обновлении через `updateColor(id, цвет)`:

```cpp
void build(sets::Builder& b) {
    b.LED(H(led));
}
void update(sets::Updater& upd) {
    upd.updateColor(H(led), 0x00ff00);
    // upd.updateColor(H(led), sets::Colors::Blue);
}
```

### Всплывающие окна
Для вызова всплывающих окон нужно отправить соответствующий апдейт. Для Confirm - с его id, для остальных - просто с текстом:

```cpp
bool cfm_f, notice_f, alert_f;

void build(sets::Builder& b) {
    if (b.beginButtons()) {
        if (b.Button("Notice")) notice_f = true;
        if (b.Button("Error")) alert_f = true;
        if (b.Button("Confirm")) cfm_f = true;
        b.endButtons();
    }

    bool res;
    if (b.Confirm(kk::conf, "Confirm", &res)) {
        Serial.println(res);
        // Serial.println(b.build.value.toBool());
    }
}

void update(sets::Updater& u) {
    if (cfm_f) {
        cfm_f = false;
        u.confirm(kk::conf);
    }
    if (notice_f) {
        notice_f = false;
        u.notice("Уведомление");
    }
    if (alert_f) {
        alert_f = false;
        u.alert("Ошибка");
    }
}
```

## Вебсокет
В версиях библиотеки с вебсокетом обновления работают иначе:

- Вебморда не запрашивает обновления, их нужно отправлять самостоятельно из любого места в программе
- Изменения в БД автоматически отправляются с шагом 300мс

Для отправки обновления используется следующая конструкция:

```cpp
SettingsXxx sett;

void foo() {
    // одно значение
    sett.updater().update(...);

    // несколько значений
    sett.updater()
        .update(...)
        .update(...)
        .update(...)
        .update(...);
}
```

Для вызова доступны все версии функций `update` из обычных обновлений (`updateColor`, `update2`, `alert`...).

> [!WARNING]
> Слишком частая отправка обновлений может замедлить работу программы вплоть до перезагрузки МК! Отправляйте по таймеру, не чаще пары десятков раз в секунду

```cpp
void loop() {
    static uint32_t tmr;
    if (millis() - tmr >= 200) {
        tmr = millis();

        sett.updater()
            .updateColor(H(lbl1), 0xffaabb)
            .update(H(lbl2), random(100));
    }
}
```

Или используйте библиотеку [GTimer](https://github.com/GyverLibs/GTimer):

```cpp
void loop() {
    static GTimer<millis> tmr(500, true);

    if (tmr) {
        sett.updater()
            .update(H(lbl1), millis())
            .update(H(lbl2), random(100));
    }
}
```

# 7.other.md
### Настройки вебморды
Некоторые параметры вебморды можно менять из скетча. Настройки обновляются при перезагрузке страницы:

```cpp
// таймаут отправки слайдера, мс. 0 чтобы отключить
sett.config.sliderTout = 100;

// таймаут ожидания ответа сервера, мс
sett.config.requestTout = 2000;

// период обновлений, мс. 0 чтобы отключить
sett.config.updateTout = 2500;

// основная цветовая схема
sett.config.theme = sets::Colors::Green;
```

### Переполнение стека ESP8266
На ESP8266 может случиться переполнение стека, если вызываемая функция слишком большая. Большая буквально - слишком много кода, т.е. это именно та проблема, которая появится при слишком большом билдере для Settings. Решение простое - разделить билдер на несколько функций, передавая в них `sets::Builder& b`:

```cpp
void build_1(sets::Builder& b) {
    // виджеты...
}
void build_2(sets::Builder& b) {
    // виджеты...
}
void build_3(sets::Builder& b) {
    // виджеты...
}
void build_4(sets::Builder& b) {
    // виджеты...
}

void build(sets::Builder& b) {
    build_1(b);
    build_2(b);
    build_3(b);
    build_4(b);
}
```

Второй вариант - лямбды, он тоже работает:

```cpp
void build(sets::Builder& b) {
    [&](){
        // виджеты...
    }();

    [&](){
        // виджеты...
    }();
}
```

В библиотеке есть удобные макросы:

```cpp
void build(sets::Builder& b) {
    SUB_BUILD_BEGIN
        // виджеты...
        
    SUB_BUILD_NEXT
        // виджеты...

    SUB_BUILD_NEXT
        // виджеты...

    SUB_BUILD_END
}
```

### Статус
- Вебморда отслеживает статус устройства, при потере связи появится текст offline в заголовке страницы. После потери связи вебморда будет запрашивать информацию о виджетах, это очень удобно при разработке - например добавляем виджет, загружаем прошивку. За это время вебморда уже понимает что устройство оффлайн и при первом успешном подключении выводит актуальные виджеты.
- При изменении значений виджетов вебморда следит за доставкой пакета, при ошибке связи появится надпись **error*** у соответствующего виджета
- В программе можно отследить наличие подключения с браузера по флагу `sett.focused()` или подключить обработчик `onFocusChange`

```cpp
sett.onFocusChange([]() {
    Serial.print("Focus: ");
    Serial.println(sett.focused());
});
```

### Время с браузера
При подключении браузер отправляет своё время в unix-формате, а система продолжает его поддерживать при помощи `StampKeeper` из библиотеки [Stamp](https://github.com/GyverLibs/Stamp). Можно использовать для синхронизации внешнего RTC или напрямую:

```cpp

void setup() {
    // ...

    // часовой пояс для rtc
    setStampZone(3);

    sett.rtc.onSecond([]() {
        // каждую секунду если синхронизирован
    });

    sett.rtc.onSync([](uint32_t unix) {
        // момент и время синхронизации
        Serial.print("Sync: ");
        Serial.println(unix);
    });
}

void loop() {
    sett.tick();

    // каждую секунду если синхронизирован
    if (sett.rtc.newSecond()) {
        Serial.println(sett.rtc.toString());
    }
}
```

## Другой вебсервер
Можно поднять библиотеку на любом вебсервере, для этого нужно наследоваться от `sets::SettingsBase` и реализовать нужные методы по аналогии со стандартными `SettingsGyver`, `SettingsESP` и проч.

Самый простой вариант - сделать класс на базе `SettingsT` - он использует вебсервер `GyverHTTP` на базе любого указанного стороннего сервера и клиента:

```cpp
#include "SettingsT.h"

class MySettings : public SettingsT<MyServer, MyClient> {
   public:
    using SettingsT<MyServer, MyClient>::SettingsT;

   private:
    String getMac() override {
        // mac адрес для приложения поиска Settings Discover (необязательно)
    }
    int getRSSI() override {
        // качество связи в % (необязательно)
    }
};
```

где `MyServer` и `MyClient` - класс сервера и клиента для вашей реализации связи, например классы от Ethernet модуля.

# 8.custom.md
## Кастомные виджеты
Раздел в разработке
