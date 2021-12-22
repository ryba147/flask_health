from flask import Blueprint

from flask_health.database import db_session
from flask_health.patient.models import Patient, MedicalCard
from flask_health.patient.schemas import PatientSchema, MedicalCardSchema

patient_bp = Blueprint('patient_bp', __name__, url_prefix='/patient')


@patient_bp.route('/', methods=['GET'])
def home():
    p = db_session.query(Patient).all()

    patient_schema = PatientSchema(many=True)
    res = patient_schema.dumps(p)

    return res


@patient_bp.route('/medical_card')
def patient_medical_card():
    mc = db_session.query(MedicalCard).first()

    mc_schema = MedicalCardSchema()
    res = mc_schema.dumps(mc)

    return res
