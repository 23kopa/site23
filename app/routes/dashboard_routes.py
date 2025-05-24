from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
@login_required  # Автоматически перенаправит на страницу логина, если пользователь не авторизован
def dashboard():
    # current_user — объект пользователя, который загрузился из базы
    return render_template('pages/dashboard.html', username=current_user.username, columns=2)
