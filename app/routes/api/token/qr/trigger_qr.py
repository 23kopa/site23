from flask import Blueprint, request, jsonify
from app.models.tokens import Token
from app import db
from datetime import datetime
import requests
from flask_login import login_required  # добавьте, если нужно

bp = Blueprint('qr_trigger', __name__)

@bp.route("/trigger/<token_uid>")
def trigger(token_uid):
    token = db.session.query(Token).filter_by(token_uid=token_uid).first()
    if not token:
        return "Not found", 404

    token.triggered_at = datetime.utcnow()

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip and ',' in ip:
        ip = ip.split(',')[0].strip()

    if ip in ('127.0.0.1', '10.8.1.2', '192.168.0.100'):
        ip = '185.22.172.242'

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

    prev_meta = token.token_metadata if token.token_metadata else {}

    token.token_metadata = {
        **prev_meta,
        'ip': ip,
        'user_agent': user_agent,
        'geo_info': geo_info,
        'trigger_time': token.triggered_at.isoformat(),
        'trigger_url': prev_meta.get('trigger_url')
    }

    db.session.commit()

    print(f"Token triggered: {token_uid}")
    print(f"IP: {ip}")
    print(f"User-Agent: {user_agent}")
    print(f"Geo: {geo_info}")

    return f"""
        <h2>Token Triggered</h2>
        <p><strong>Trigger Time:</strong> {token.triggered_at}</p>
        <p><strong>IP:</strong> {ip}</p>
        <p><strong>User-Agent:</strong> {user_agent}</p>
        <h3>Geo Info:</h3>
        <pre>{geo_info}</pre>
    """

# Новый эндпоинт для получения информации о токене в JSON
@bp.route('/api/token_info/<token_uid>', methods=['GET'])
@login_required  # если нужен доступ только авторизованным
def token_info(token_uid):
    token = Token.query.filter_by(token_uid=token_uid).first()
    if not token:
        return jsonify({'error': 'Token not found'}), 404

    return jsonify({
        'token_uid': token.token_uid,
        'triggered_at': token.triggered_at.isoformat() if token.triggered_at else None,
        'token_metadata': token.token_metadata,
        'email': token.email,
        'alert_message': token.alert_message,
    })
