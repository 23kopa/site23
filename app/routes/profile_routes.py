from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from app.models.users import User
from app import db
import os

bp = Blueprint('profile', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'app/static/images/avatars'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/account')
@login_required
def account():
    user = current_user
    return render_template('auth/profile.html', user=user, page_name='profile')

@bp.route('/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = current_user

    if request.method == 'POST':
        new_username = request.form['username']
        new_email = request.form['email']
        new_password = request.form['password']
        avatar_file = request.files.get('avatar')

        if new_username != user.username and User.query.filter_by(username=new_username).first():
            return "Логин уже занят"
        if new_email != user.email and User.query.filter_by(email=new_email).first():
            return "Email уже занят"

        user.username = new_username
        user.email = new_email
        if new_password:
            user.password = generate_password_hash(new_password)

        if avatar_file and avatar_file.filename != '' and allowed_file(avatar_file.filename):
            filename = secure_filename(avatar_file.filename)
            ext = filename.rsplit('.', 1)[1].lower()
            new_avatar_filename = f"user_{user.id}.{ext}"
            avatar_path = os.path.join(UPLOAD_FOLDER, new_avatar_filename)
            avatar_file.save(avatar_path)
            user.avatar = new_avatar_filename

        db.session.commit()
        return redirect(url_for('profile.account'))

    return render_template('auth/edit.html', user=user, page_name='edit')
