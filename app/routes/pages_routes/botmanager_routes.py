from flask import Blueprint, render_template
from flask_login import login_required
from app.services.card_services.botmanager_cards_service import get_botmanager_cards

bp = Blueprint('botmanager', __name__)

@bp.route('/bot')
@login_required
def botmanager():
    cards = get_botmanager_cards()
    center_cards = [c for c in cards if c.get('position') == 'center']
    grid_cards = [c for c in cards if c.get('position') != 'center']
    return render_template(
        'pages/botmanager.html',
        title='Панель управления',
        center_cards=center_cards,
        grid_cards=grid_cards,
        columns=3
    )
