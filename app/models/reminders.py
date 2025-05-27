from app import db

class Reminder(db.Model):
    __tablename__ = 'reminders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String(200))

    # Обратная связь с User — тоже строкой
    user = db.relationship("User", back_populates="reminders")
