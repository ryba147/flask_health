from flask import Blueprint

hospital_bp = Blueprint('hospital_bp', __name__)


@hospital_bp.route('/hospital')
def hello():
    return 'Hello, hospital!'
