# app/routes/pages_routes/trigger_routes.py
from flask import Blueprint, request
from app.models.tokens import Token
from app import db
from datetime import datetime

bp = Blueprint('token_trigger', __name__)

@bp.route("/trigger/<token_uid>")
def trigger(token_uid):
    token = db.session.query(Token).filter_by(token_uid=token_uid).first()
    if not token:
        return "Not found", 404

    token.triggered_at = datetime.utcnow()
    db.session.commit()

    # Логирование можно расширить:
    print("Trigger from:", request.remote_addr, request.headers.get("User-Agent"))

    return "", 204
