from flask import *

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')