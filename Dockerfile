# Используем официальный образ Python
FROM python:3.11-slim

# Установка зависимостей
RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Указываем переменную окружения (если нужно)
ENV FLASK_APP=run.py
ENV FLASK_ENV=development
ENV PYTHONUNBUFFERED=1

# Пробрасываем порт
EXPOSE 5000

# Команда запуска
CMD ["flask", "run", "--host=0.0.0.0"]
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:app"]