from flask import Blueprint

patient_bp = Blueprint('patient_bp', __name__)


@patient_bp.route('/patient', methods=['GET'])
def home():
    return 'Hello, patient!'
