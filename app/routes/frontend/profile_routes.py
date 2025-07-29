# app/routes/pages_routes/account_routes.py
from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
from app.services.card.profile_cards_service import get_profile_cards

bp = Blueprint('profile', __name__)

@bp.route('/profile')
@login_required
def profile():
    cards = get_profile_cards(current_user)
    center_cards = [c for c in cards if c.get('position') == 'center']
    grid_cards = [c for c in cards if c.get('position') != 'center']
    return render_template(
        'auth/profile.html',
        cards=cards,
        user=current_user,
        center_cards=center_cards,
        grid_cards=grid_cards,
        columns=3
    )

