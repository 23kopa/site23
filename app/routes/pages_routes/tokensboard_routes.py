from flask import Blueprint, render_template
from flask_login import login_required
from app.services.card_services.tokens_cards_service import get_tokens_cards

bp = Blueprint('tokensboard', __name__)

@bp.route('/tokensboard')
@login_required
def tokens_dashboard():
    cards = get_tokens_cards()
    center_cards = [c for c in cards if c.get('position') == 'center']
    grid_cards = [c for c in cards if c.get('position') != 'center']
    return render_template(
        'pages/tokens.html',
        title='Панель управления',
        grid_cards=grid_cards,
        columns=3
    )