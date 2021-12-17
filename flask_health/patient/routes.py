from flask import Blueprint

patient_bp = Blueprint('patient_bp', __name__)


@patient_bp.route('/patient')
def home():
    return 'Hello, patient!'
