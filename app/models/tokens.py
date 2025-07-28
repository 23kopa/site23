from app import db
from datetime import datetime

class Token(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True)
    token_type = db.Column(db.String(20))  # 'web', 'dns', 'word', ...
    token_uid = db.Column(db.String(128), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(256))
    alert_message = db.Column(db.String(512))
    triggered_at = db.Column(db.DateTime)
    token_metadata = db.Column(db.JSON)

    user = db.relationship("User", back_populates="tokens")
