from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('main/index.html')