# Команды для развертывания на Ubuntu сервере

## Способ 1: Автоматический (рекомендуется)

```bash
# 1. Загрузите файлы на сервер (через scp, git или другим способом)
scp -r . user@your-server:/home/user/telegram-bot/

# 2. Подключитесь к серверу
ssh user@your-server

# 3. Перейдите в папку проекта
cd telegram-bot

# 4. Сделайте скрипт исполняемым и запустите
chmod +x deploy.sh
./deploy.sh

# 5. Добавьте токен бота в bot.py
nano bot.py
# Замените YOUR_BOT_TOKEN на реальный токен

# 6. Запустите бота
sudo systemctl start telegram-bot
```

## Способ 2: Ручная установка

```bash
# Обновление системы
sudo apt update && sudo apt upgrade -y

# Установка Python
sudo apt install python3 python3-pip python3-venv -y

# Создание виртуального окружения
python3 -m venv telegram_bot_env
source telegram_bot_env/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Запуск бота (для тестирования)
python bot.py
```

## Способ 3: Через Docker

```bash
# Создайте Dockerfile (см. ниже)
docker build -t telegram-bot .
docker run -d --name telegram-bot telegram-bot
```

## Управление сервисом

```bash
# Запуск
sudo systemctl start telegram-bot

# Остановка
sudo systemctl stop telegram-bot

# Перезапуск
sudo systemctl restart telegram-bot

# Статус
sudo systemctl status telegram-bot

# Логи
sudo journalctl -u telegram-bot -f
```

## Загрузка файлов на сервер

### Через SCP:
```bash
scp -r . user@your-server:/home/user/telegram-bot/
```

### Через Git:
```bash
# На сервере
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### Через SFTP:
```bash
sftp user@your-server
put -r local-folder remote-folder
```