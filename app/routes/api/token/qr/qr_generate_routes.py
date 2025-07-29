from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app import csrf, db
from app.models.tokens import Token
from app.services.tokens_services.qr_token import generate_qr_token

bp = Blueprint('qr_generate', __name__)

@bp.route('/create_qrcode_token', methods=['POST'])
@login_required
@csrf.exempt
def create_qrcode_token():
    email = request.form.get('email')
    alert_message = request.form.get('alert_message')

    data = generate_qr_token(current_user.id)
    token_uid = data['url'].rstrip('/').split('/')[-1]

    token = Token.query.filter_by(token_uid=token_uid).first()
    if not token:
        return jsonify({'error': 'Ошибка при создании токена.'}), 400

    token.email = email
    token.alert_message = alert_message
    db.session.commit()

    response = {
        'url': data['url'],
        'token_type': token.token_type
    }

    if token.token_type == 'qr':
        response['qr_image_url'] = f"data:image/png;base64,{data['qr_base64']}"

    return jsonify(response)
