from flask import Blueprint

hospital_bp = Blueprint('hospital_bp', __name__, url_prefix='/hospital')


@hospital_bp.route('/')
def hello():
    return 'Hello, hospital!'
