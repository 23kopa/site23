from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.services.card_services.dashboard_cards_service import get_dashboard_cards

bp = Blueprint('main_routes', __name__)
@bp.route('/')
def home():
    return render_template('pages/welcome.html')
