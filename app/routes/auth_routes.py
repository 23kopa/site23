from flask import Blueprint, request, render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.users import User
from app import db

bp = Blueprint('auth_routes', __name__)


# ! Идентификация
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('dashboard.dashboard'))  # Перенаправление на защищённую страницу
        else:
            return render_template('auth/login.html', error='Неверный логин или пароль')

    return render_template('auth/login.html')


# ! Регистрация
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Проверка на дублирование
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return 'Пользователь с таким логином или email уже существует'

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('auth/register.html')

