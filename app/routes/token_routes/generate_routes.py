from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.services.tokens_services.web_token import generate_web_token
from app import csrf
from flask import request, jsonify
from app.models.tokens import Token
from app import db

bp = Blueprint('token_generate', __name__)

@bp.route('/create_webbug_token', methods=['POST'])
@login_required
@csrf.exempt
def create_webbug_token():
    email = request.form.get('email')
    alert_message = request.form.get('alert_message')

    token_url = generate_web_token(current_user.id)

    # Обновим запись: добавим email и alert_message
    token_uid = token_url.rstrip('/').split('/')[-1]
    token = Token.query.filter_by(token_uid=token_uid).first()
    if not token:
        return jsonify({'error': 'Ошибка при создании токена.'}), 400

    token.email = email
    token.alert_message = alert_message
    db.session.commit()

    return jsonify({'url': token_url})

