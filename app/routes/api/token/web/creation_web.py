from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.services.token_engines.web_token import generate_web_token
from app import csrf

bp = Blueprint('token_create', __name__)

@bp.route('/create_web_token', methods=['POST'])
@login_required
@csrf.exempt
def create_web_token():
    email = request.form.get('email')
    alert_message = request.form.get('alert_message')
    if not email:
        return jsonify({'error': 'Email обязателен'}), 400

    token_url = generate_web_token(current_user.id, email, alert_message)
    return jsonify({'url': token_url})
