# app/services/tokens_services/web_token.py

import uuid
from flask import request
from app.models.tokens import Token
from app import db

def generate_web_token(user_id: int) -> str:
    token_uid = str(uuid.uuid4())
    
    # http://localhost:5000/trigger/<token_uid>
    base_url = request.host_url.rstrip('/')
    trigger_url = f"{base_url}/trigger/{token_uid}"

    token = Token(
        token_type='web',
        token_uid=token_uid,
        user_id=user_id,
        email=None,
        alert_message=None,
        token_metadata={'trigger_url': trigger_url}
    )
    db.session.add(token)
    db.session.commit()

    return trigger_url
