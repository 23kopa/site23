from flask import Flask, render_template, redirect, url_for, request, session, jsonify
import paramiko
from aiogram import Bot, Dispatcher
import os
import psutil
import socket

app = Flask(__name__)
app.secret_key = 'kopauser'

# ! Настройки для бота
API_TOKEN = '7505610899:AAF2RxxuifLLUhqprRvDDrOBs_-1TrdPADU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ! Настройки для VPS (SSH)
VPS_IP = '185.22.172.242'
VPS_USER = 'root'
VPS_PASSWORD = 'cN5tUXWYfj395b61Br'


# ! SSH Connect to VPS
def ssh_execute(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(VPS_IP, username=VPS_USER, password=VPS_PASSWORD)
        stdin, stdout, stderr = ssh.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()
    except Exception as e:
        return "", f"SSH error: {e}"
    finally:
        ssh.close()


# ! Функции

# Функция для получения использования CPU
def get_cpu_usage():
    # Используем psutil для получения процента использования CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# Функция для получения количества ядер процессора
def get_cpu_cores():
    physical_cores = psutil.cpu_count(logical=False)  # физические ядра
    logical_cores = psutil.cpu_count(logical=True)    # логические ядра
    return physical_cores, logical_cores

# Функция для получения частоты процессора
def get_cpu_frequency():
    freq = psutil.cpu_freq()
    return freq.current, freq.min, freq.max  # Текущая, минимальная и максимальная частота процессора

# Маршрут для получения данных о CPU
@app.route('/cpu_usage')
def cpu_usage():
    cpu_usage = get_cpu_usage()
    physical_cores, logical_cores = get_cpu_cores()
    current_freq, min_freq, max_freq = get_cpu_frequency()

    return jsonify({
        'cpu_usage': cpu_usage,
        'physical_cores': physical_cores,
        'logical_cores': logical_cores,
        'current_freq': current_freq,
        'min_freq': min_freq,
        'max_freq': max_freq
    })

# Функция для получения информации о сети
def get_network_info():
    net_io = psutil.net_io_counters()  # Получаем статистику по трафику
    net_if_addrs = psutil.net_if_addrs()  # Получаем информацию об интерфейсах

    network_info = {
        'bytes': {
            'sent': net_io.bytes_sent,  # Отправлено байтов
            'recv': net_io.bytes_recv,  # Получено байтов
        },
        'packets': {
            'sent': net_io.packets_sent,  # Отправлено пакетов
            'recv': net_io.packets_recv,  # Получено пакетов
        },
    }
    return network_info

# Маршрут для получения информации о сети
@app.route('/network_info')
def network_info():
    info = get_network_info()
    return jsonify(info)

# Disk Memory
def get_disk_usage():
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


# Статус Nginx
@app.route('/nginx_status')
def nginx_status():
    command = 'systemctl is-active nginx'
    stdout, stderr = ssh_execute(command)
    if stderr:
        return jsonify({'status': 'Ошибка при получении статуса Nginx'})
    return jsonify({'status': stdout.strip()})


# Статус SSL-сертификатов
@app.route('/ssl_status')
def ssl_status():
    command = 'openssl x509 -in /etc/ssl/certs/botmanager.crt -noout -dates'  # Путь к вашему сертификату
    stdout, stderr = ssh_execute(command)
    if stderr:
        return jsonify({'status': 'Ошибка при получении статуса SSL-сертификатов'})
    return jsonify({'status': stdout.strip()})


# Запуск бота на сервере
@app.route('/start_bot')
def start_bot():
    command = 'sudo systemctl start mybot'
    stdout, stderr = ssh_execute(command)
    if stderr:
        # Обработка ошибки, если она есть
        return f"Ошибка при запуске бота: {stderr}"
    return redirect(url_for('home'))


# Остановка бота на сервере
@app.route('/stop_bot')
def stop_bot():
    command = 'sudo systemctl stop mybot'
    stdout, stderr = ssh_execute(command)
    if stderr:
        # Обработка ошибки, если она есть
        return f"Ошибка при остановке бота: {stderr}"
    return redirect(url_for('home'))


# Перезагрузка бота на сервере
@app.route('/restart_bot')
def restart_bot():
    command = 'sudo systemctl restart mybot'
    stdout, stderr = ssh_execute(command)
    if stderr:
        # Обработка ошибки, если она есть
        return f"Ошибка при перезагрузке бота: {stderr}"
    return redirect(url_for('home'))


@app.route('/logs')
def logs():
    stdout, stderr = ssh_execute('cat /var/log/syslog | tail -n 50')  # пример команды
    logs_output = stdout if stdout else stderr
    return render_template('test.html', logs=logs_output)

@app.route('/bot')
def botmanager():
    return render_template('bot.html')


# ! Запуск веб-приложения
@app.route('/')
def home():
    # Здесь можно выводить статистику, например, активных пользователей
    # active_processes = get_active_processes()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        ssl_context=('/etc/letsencrypt/live/botmanager.site/fullchain.pem', '/etc/letsencrypt/live/botmanager.site/privkey.pem')
    )
