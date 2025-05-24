from flask import Blueprint, jsonify, render_template
from flask_login import login_required
from app.services.vps_service import get_cpu_usage, get_cpu_cores, get_cpu_frequency, get_network_info
from app.services.ssh_service import ssh_execute

bp = Blueprint('botmanager', __name__)

@bp.route('/bot')
@login_required  # Защита маршрута
def botmanager():
    return render_template('pages/botmanager.html', columns=4)

@bp.route('/cpu_usage')
@login_required  # Защита API
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
@login_required  # Защита API
def nginx_status():
    command = 'systemctl is-active nginx'
    stdout, stderr = ssh_execute(command)
    if stderr:
        return jsonify({'status': 'Ошибка при получении статуса Nginx'})
    return jsonify({'status': stdout.strip()})

@bp.route('/network_info')
@login_required  # Защита API
def network_info():
    info = get_network_info()
    return jsonify(info)
