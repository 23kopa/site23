from flask import Flask, render_template, redirect, url_for
import paramiko
from aiogram import Bot, Dispatcher

app = Flask(__name__)

# Настройки для бота
API_TOKEN = '7505610899:AAF2RxxuifLLUhqprRvDDrOBs_-1TrdPADU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Настройки для VPS (SSH)
VPS_IP = '185.22.172.242'
VPS_USER = 'root'
VPS_PASSWORD = 'cN5tUXWYfj395b61Br'


# Статистика бота
@app.route('/')
def home():
    # Здесь можно выводить статистику, например, активных пользователей
    return render_template('index.html')


# Запуск бота на сервере
@app.route('/start_bot')
def start_bot():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(VPS_IP, username=VPS_USER, password=VPS_PASSWORD)
    ssh.exec_command('sudo systemctl start mybot')
    ssh.close()
    return redirect(url_for('home'))


# Остановка бота на сервере
@app.route('/stop_bot')
def stop_bot():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(VPS_IP, username=VPS_USER, password=VPS_PASSWORD)
    ssh.exec_command('sudo systemctl stop mybot')
    ssh.close()
    return redirect(url_for('home'))


# Перезагрузка бота на сервере
@app.route('/restart_bot')
def restart_bot():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(VPS_IP, username=VPS_USER, password=VPS_PASSWORD)
    ssh.exec_command('sudo systemctl restart mybot')
    ssh.close()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=(
        '/etc/letsencrypt/live/botmanager.site/fullchain.pem',
        '/etc/letsencrypt/live/botmanager.site/privkey.pem'
    ))
