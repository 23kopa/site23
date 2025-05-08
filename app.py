from flask import Flask, render_template, redirect, url_for, request, session, jsonify
import paramiko
from aiogram import Bot, Dispatcher

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


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Проверка с кодом
        if username == "admin" and password == "password":
            session['username'] = username  # Сохранение пользователя в сессии
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:  # Проверка, авторизован ли пользователь
        return f"Welcome to your dashboard, {session['username']}!"
    else:
        return redirect(url_for('login'))  # Перенаправление на страницу входа, если не авторизован

@app.route('/get_disk_usage')
def api_disk_usage():
    usage = get_disk_usage()
    return jsonify(usage)

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


# Active Process
""" def get_active_processes():
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
        ssh.close() """


# SSH Connect to VPS
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


# Статистика бота
@app.route('/')
def home():
    # Здесь можно выводить статистику, например, активных пользователей
    # active_processes = get_active_processes()
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        ssl_context=('/etc/letsencrypt/live/botmanager.site/fullchain.pem', '/etc/letsencrypt/live/botmanager.site/privkey.pem')
    )
