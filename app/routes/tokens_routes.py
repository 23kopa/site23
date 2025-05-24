from flask import Blueprint, render_template
from flask_login import login_required, current_user

bp = Blueprint('tokens', __name__)

@bp.route('/tokens')
@login_required
def tokens():
    username = current_user.username
    return render_template('pages/tokens.html', username=username, columns=4)
