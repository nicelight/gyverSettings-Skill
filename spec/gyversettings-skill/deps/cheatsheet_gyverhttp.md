---
title: GyverHTTP — шпаргалка
updated: 2025-12-30
---

- Роутинг: `server.onRequest([](Request req){ switch(req.path().hash()) { ... } });`
- Отправка: `server.send(code)`, `server.sendFile(f, mime)`, `sendFile_P(data, len, mime, gzip)`.
- CORS: можно отключить в Settings дефайном `SETS_NO_CORS` (управляет `server.useCors`).
- WS: отдельные адаптеры SettingsGyverWS/AsyncWS требуют arduinoWebSockets/ESPAsyncWebServer/ESPAsyncTCP.
- Auth: в Settings проверка по `authenticate(authToken)` в обработчике `/fetch`/`/upload`/`/ota`.
