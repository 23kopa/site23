from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.services.content.pages.home_content import get_home_header, get_feature_cards, get_testimonial

from app.services.content.components.cards.tokens_cards import get_tokens_cards
from app.services.content.components.modals.tokens_modals import get_tokens_modals

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
    return redirect(url_for('home.homepage'))


@bp.route('/home')
def homepage():
    header = get_home_header()
    feature_cards = get_feature_cards()
    testimonial = get_testimonial()

    token_cards = get_tokens_cards()  # карточки для выбора токена
    modals_data = get_tokens_modals() # старые модалки

    # Объединяем карточки с модалками
    for card in token_cards:
        if card['id'] in modals_data:
            card.update(modals_data[card['id']])

    return render_template(
        'pages/home.html',
        title='Главная',
        header=header,
        feature_cards=feature_cards,
        testimonial=testimonial,
        token_select_cards=token_cards,  # карточки для выбора токена
        grid_cards=token_cards,          # чтобы старые модалки рендерились через блок modals
    )

