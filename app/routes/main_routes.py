from flask import Blueprint, render_template, redirect, url_for, request, session, jsonify
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('pages/welcome.html')
