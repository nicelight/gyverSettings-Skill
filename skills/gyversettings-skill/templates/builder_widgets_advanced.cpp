// Пример добавления расширенных виджетов Settings
#include <SettingsGyver.h>

extern GyverDBFile db;

static void build_advanced(sets::Builder& b) {
    sets::Group g(b, "Advanced");
    b.Slider(kk::slider_val, "Slider", 0, 100);
    b.Switch(kk::led_state, "LED State");
    b.Select(kk::mode, "Mode", "Off|On|Auto");
    b.Number(kk::num_val, "Number", 0, 1000);
    b.Log("Log", 20);  // web logger
    b.HTML("Note", "<b>Custom HTML block</b>");
    b.Graph("Graph", kk::table_key);  // требует Table/BSON данных
}
