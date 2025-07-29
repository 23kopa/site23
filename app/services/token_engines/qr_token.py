import hashlib
import uuid
import qrcode
import io
import base64
from flask import request
from app.models.tokens import Token
from app import db

def generate_token_uid() -> str:
    random_bytes = uuid.uuid4().bytes + uuid.uuid4().bytes
    return hashlib.sha1(random_bytes).hexdigest()

def generate_qr_token(user_id: int) -> dict:
    token_uid = generate_token_uid()
    base_url = request.host_url.rstrip('/')
    trigger_url = f"{base_url}/trigger/{token_uid}"

    # Сохраняем токен в БД
    token = Token(
        token_type='qr',
        token_uid=token_uid,
        user_id=user_id,
        email=None,
        alert_message=None,
        token_metadata={'trigger_url': trigger_url}
    )
    db.session.add(token)
    db.session.commit()

    # Генерируем QR-код
    img = qrcode.make(trigger_url)
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return {
        "url": trigger_url,
        "qr_base64": qr_base64
    }
