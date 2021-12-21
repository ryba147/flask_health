from flask import Blueprint

from flask_health.database import db_session
from flask_health.hospital.models import Hospital
from flask_health.hospital.schemas import HospitalSchema

hospital_bp = Blueprint('hospital_bp', __name__, url_prefix='/hospital')


@hospital_bp.route('/')
def hello():
    h = db_session.query(Hospital).all()

    patient_schema = HospitalSchema(many=True)
    res = patient_schema.dumps(h)

    return res
