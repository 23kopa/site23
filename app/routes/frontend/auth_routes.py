from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.services.card.login_cards_service import get_login_cards
from app.services.card.register_cards_service import get_register_cards
from app.models.users import User
from app import db

bp = Blueprint('auth', __name__)


# ! Идентификация
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash('Неправильный логин или пароль', 'danger')

    login_cards = get_login_cards()
    return render_template('auth/login.html', page_name='login', login_cards=login_cards)


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

        return redirect(url_for('auth.login'))

    register_cards = get_register_cards()
    return render_template('auth/register.html', page_name='register', register_cards=register_cards)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
