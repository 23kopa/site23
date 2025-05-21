from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from app.models.users import User
from app import db
import os

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    return render_template('pages/dashboard.html', username=session['username'])

