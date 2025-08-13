from flask import Blueprint, jsonify, request
from app.services.token_engines.web_token import generate_web_token
from flask_login import current_user
from app import csrf
from uuid import uuid4

bp = Blueprint('token_create', __name__)

@bp.route('/create_web_token', methods=['POST'])
@csrf.exempt
def create_web_token():
    email = request.form.get('email')
    alert_message = request.form.get('alert_message')
    if not email:
        return jsonify({'error': 'Email обязателен'}), 400

    user_id = getattr(current_user, 'id', str(uuid4()))
    token_url = generate_web_token(user_id, email, alert_message)
    return jsonify({'url': token_url})
