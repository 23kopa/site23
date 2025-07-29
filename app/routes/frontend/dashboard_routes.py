from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.services.card.dashboard_cards_service import get_dashboard_cards

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
@login_required
def dashboard():
    cards = get_dashboard_cards(current_user)
    center_cards = [c for c in cards if c.get('position') == 'center']
    grid_cards = [c for c in cards if c.get('position') != 'center']
    return render_template(
        'pages/dashboard.html',
        cards=cards,
        user=current_user,
        center_cards=center_cards,
        grid_cards=grid_cards,
        columns=3
    )
