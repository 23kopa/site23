from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.services.content.pages.home_content import get_home_header, get_feature_cards, get_testimonial

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
    return redirect(url_for('home.homepage'))


@bp.route('/home')
def homepage():
    header = get_home_header()
    feature_cards = get_feature_cards()
    testimonial = get_testimonial()
    return render_template(
        'pages/home.html',
        title='Панель управления',
        header=header,
        feature_cards=feature_cards,
        testimonial=testimonial,
        user=current_user
    )
