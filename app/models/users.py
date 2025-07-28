from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Лучше явно указывать имя таблицы

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    avatar = db.Column(db.String(120))
    
    role = db.Column(db.String(20), nullable=False, default='user')

    reminders = db.relationship('Reminder', back_populates='user', lazy='dynamic')

    tokens = db.relationship("Token", back_populates="user")

    @property
    def reminders_count(self):
        return self.reminders.count()
