#!/bin/bash

# Скрипт для развертывания Telegram бота на Ubuntu сервере

echo "🚀 Развертывание Telegram бота..."

# Обновление системы
sudo apt update && sudo apt upgrade -y

# Установка Python и pip
sudo apt install python3 python3-pip python3-venv -y

# Создание виртуального окружения
python3 -m venv telegram_bot_env
source telegram_bot_env/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Создание systemd сервиса для автозапуска
sudo tee /etc/systemd/system/telegram-bot.service > /dev/null <<EOF
[Unit]
Description=Telegram Bot Service
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$(pwd)
Environment=PATH=$(pwd)/telegram_bot_env/bin
ExecStart=$(pwd)/telegram_bot_env/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Перезагрузка systemd и запуск сервиса
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot.service

echo "✅ Развертывание завершено!"
echo "📝 Не забудьте:"
echo "   1. Добавить токен бота в bot.py"
echo "   2. Добавить фото photo.jpg (если нужно)"
echo "   3. Запустить сервис: sudo systemctl start telegram-bot"