# Самострой-бот (Telethon) — конфиг для Railway

В этот ZIP входят базовые файлы, чтобы развернуть бота на Railway, не настраивая вручную сервер.

## Содержимое

- `samastroi_telethon.py` — минимальный шаблон бота на Telethon. Замените на свой реальный файл бота.
- `create_session.py` — скрипт для создания Telegram-сессии (`.session` файла).
- `requirements.txt` — зависимости Python.
- `Dockerfile` — инструкция для сборки Docker-образа на Railway.
- `railway.json` — минимальная конфигурация Railway (использовать Dockerfile).
- `Procfile` — тип процесса (worker) для совместимости с Heroku-стилем.
- `.env.example` — пример файла переменных окружения.

## Как использовать с Railway

1. **Локально** создайте файл сессии:
   ```bash
   python create_session.py
   ```
   После успешной авторизации появится файл `samostroi.session`. Его нужно положить рядом с кодом.

2. Замените `samastroi_telethon.py` на ваш реальный файл бота, если он отличается.

3. Загрузите всё содержимое в репозиторий GitHub.

4. В Railway:
   - создайте новый проект;
   - привяжите репозиторий GitHub;
   - в разделе Variables добавьте переменные:
     - `TG_API_ID`
     - `TG_API_HASH`
     - `TG_PHONE` (при необходимости)
     - `SESSION_FILE` (если имя `.session` другое)
   - запустите деплой.

5. Railway соберёт Docker-образ на основе `Dockerfile` и запустит команду:
   ```bash
   python samastroi_telethon.py
   ```

При необходимости вы можете дописать в Dockerfile дополнительные системные пакеты или Python-зависимости.
