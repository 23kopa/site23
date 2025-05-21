from flask import Blueprint, jsonify, redirect, url_for, render_template
from app.services.vps_service import get_cpu_usage, get_cpu_cores, get_cpu_frequency, get_network_info
from app.services.ssh_service import ssh_execute

bp = Blueprint('botmanager', __name__)

@bp.route('/bot')
def botmanager():
    return render_template('pages/botmanager.html')

@bp.route('/cpu_usage')
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

@bp.route('/nginx_status')
def nginx_status():
    command = 'systemctl is-active nginx'
    stdout, stderr = ssh_execute(command)
    if stderr:
        return jsonify({'status': 'Ошибка при получении статуса Nginx'})
    return jsonify({'status': stdout.strip()})

@bp.route('/network_info')
def network_info():
    info = get_network_info()
    return jsonify(info)