import requests
from app.services.kv.redis_store import get_token, update_token
from flask import Blueprint, jsonify, request, render_template
from app.models.tokens import Token
from datetime import datetime
from flask_login import login_required

bp = Blueprint('token_trigger', __name__)

def process_token_trigger(token_uid):
    token_data = get_token(token_uid)
    if not token_data:
        return "Not found", 404

    triggered_at = datetime.utcnow()

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip and ',' in ip:
        ip = ip.split(',')[0].strip()
    if ip in ('127.0.0.1', '10.8.1.2', '172.20.10.3'):
        ip = '185.22.172.242'  # заглушка

    user_agent = request.headers.get("User-Agent")

    geo_info = {}
    try:
        r = requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,org,as,isp,query"
        )
        if r.status_code == 200 and r.json().get("status") == "success":
            geo_info = r.json()
    except Exception as e:
        print("Geo lookup failed:", e)

    prev_meta = token_data.get("token_metadata", {})
    update_token(token_uid, {
        "triggered_at": triggered_at.isoformat(),
        "token_metadata": {
            **prev_meta,
            'ip': ip,
            'user_agent': user_agent,
            'geo_info': geo_info,
            'trigger_time': triggered_at.isoformat(),
            'trigger_url': prev_meta.get('trigger_url')
        }
    })

    return render_template('base/trigger_gif.html', gif_url='/static/images/gif/spbgut.gif')

# Обработка нескольких маршрутов на один обработчик
@bp.route("/<token_uid>/img.gif")
@bp.route("/trigger/<token_uid>")
def trigger(token_uid):
    return process_token_trigger(token_uid)

# Эндпоинт для получения информации о токене в JSON
@bp.route('/api/token_info/<token_uid>', methods=['GET'])
@login_required
def token_info(token_uid):
    token_data = get_token(token_uid)
    if not token_data:
        return jsonify({'error': 'Token not found'}), 404

    return jsonify({
        'token_uid': token_uid,
        'triggered_at': token_data.get('triggered_at'),
        'token_metadata': token_data.get('token_metadata'),
        'email': token_data.get('email'),
        'alert_message': token_data.get('alert_message'),
    })


@bp.route('/view/<token_uid>')
def view_gif(token_uid):
    gif_url = '/static/images/gif/spbgut.gif'
    return render_template('full_screen_gif.html', gif_url=gif_url)
