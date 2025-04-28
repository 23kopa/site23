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


def get_disk_usage():
    """Функция для получения состояния диска на сервере через SSH."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(VPS_IP, username=VPS_USER, password=VPS_PASSWORD)
        # Используем команду du для получения размера директорий с исключением /proc
        stdin, stdout, stderr = ssh.exec_command('du -h --exclude=/proc --max-depth=1 /')
        disk_usage = stdout.read().decode()  # Чтение и декодирование вывода

        # Преобразуем вывод в словарь для использования в шаблоне
        usage_lines = disk_usage.splitlines()
        usage_data = []
        for line in usage_lines:
            parts = line.split('\t')
            if len(parts) == 2:
                size, directory = parts
                usage_data.append({'size': size, 'directory': directory})

        return usage_data
    except Exception as e:
        return f"Ошибка при получении состояния диска: {e}"
    finally:
        ssh.close()

def get_active_processes():
    """Функция для получения активных процессов на сервере через SSH."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(VPS_IP, username=VPS_USER, password=VPS_PASSWORD)
        # Используем команду ps для получения списка процессов
        stdin, stdout, stderr = ssh.exec_command('ps aux --sort=-%cpu')
        processes = stdout.read().decode()  # Чтение и декодирование вывода

        # Преобразуем вывод в список для использования в шаблоне
        process_lines = processes.splitlines()
        process_data = []
        for line in process_lines[1:]:  # Пропускаем первую строку с заголовками
            parts = line.split()
            if len(parts) >= 11:
                pid = parts[1]
                user = parts[0]
                cpu = parts[2]
                memory = parts[3]
                command = " ".join(parts[10:])
                process_data.append({
                    'pid': pid,
                    'user': user,
                    'cpu': cpu,
                    'memory': memory,
                    'command': command
                })

        return process_data[:10]
    except Exception as e:
        return f"Ошибка при получении активных процессов: {e}"
    finally:
        ssh.close()


import paramiko


# Статистика бота
@app.route('/')
def home():
    # Здесь можно выводить статистику, например, активных пользователей
    disk_usage = get_disk_usage()  # Получаем состояние диска
    active_processes = get_active_processes()
    return render_template('index.html', disk_usage=disk_usage, processes=active_processes)


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
    # Укажи абсолютные пути к сертификату и ключу
    app.run(
        host='0.0.0.0', 
        port=5000, 
        ssl_context=('/etc/letsencrypt/live/botmanager.site/fullchain.pem', '/etc/letsencrypt/live/botmanager.site/privkey.pem')
    )
