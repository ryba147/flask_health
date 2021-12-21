from flask import Blueprint

from flask_health.database import db_session
from flask_health.patient.models import Patient
from flask_health.patient.schemas import PatientSchema

patient_bp = Blueprint('patient_bp', __name__, url_prefix='/patient')


@patient_bp.route('/', methods=['GET'])
def home():
    p = db_session.query(Patient).all()

    patient_schema = PatientSchema(many=True)
    res = patient_schema.dumps(p)

    return res
