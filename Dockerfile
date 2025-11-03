FROM python:3.11-slim

# Установка рабочей директории
WORKDIR /app

# Копирование файлов
COPY requirements.txt .
COPY bot.py .
COPY photo.jpg . 

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Запуск бота
CMD ["python", "bot.py"]