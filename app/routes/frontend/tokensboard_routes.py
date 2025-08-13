from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.services.content.components.cards.tokens_cards import get_tokens_cards
from app.services.content.components.modals.tokens_modals import get_tokens_modals

bp = Blueprint('tokensboard', __name__)


@bp.route('/tokensboard')
def tokens_dashboard():
    cards = get_tokens_cards()
    modals = get_tokens_modals()

    # Объединяем карточки с модалками
    for card in cards:
        modal_data = modals.get(card['id'])
        if modal_data:
            card.update(modal_data)

    grid_cards = [c for c in cards if c.get('position') != 'center']

    return render_template(
        'pages/tokens.html',
        title='Панель управления',
        grid_cards=grid_cards,
        columns=3,
        user=current_user
    )
