from http import HTTPStatus

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from flask_health.database import db_session
from flask_health.patient.models import Patient, MedicalCard
from flask_health.patient.schemas import PatientSchema, MedicalCardSchema

patient_bp = Blueprint('patient_bp', __name__, url_prefix='/patient')


@patient_bp.route('/', methods=['GET'])
def get_list():
    # query params filters. filter_by. 2-3
    patients = Patient.get_all()
    patient_schema = PatientSchema(many=True)
    res = patient_schema.dump(patients)
    return jsonify(res)


@patient_bp.route('/<int:patient_id>/', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.get_by_id(patient_id)

    if patient is None:
        return {'message': 'Patient not found'}, HTTPStatus.NOT_FOUND

    patient_schema = PatientSchema()
    res = patient_schema.dump(patient)
    return res, HTTPStatus.OK


@patient_bp.route('/', methods=['POST'])
def add_patient():
    json_data = request.get_json(silent=False)

    try:
        PatientSchema().load(json_data)
        patient = Patient.add(json_data)
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST

    patient_schema = PatientSchema()
    res = patient_schema.dump(patient)

    return res, HTTPStatus.CREATED


@patient_bp.route('/<int:patient_id>/', methods=['PUT'])
def update_patient(patient_id):

    if not Patient.get_by_id(patient_id):
        return {'message': 'Patient not found'}, HTTPStatus.NOT_FOUND

    json_data = request.get_json(silent=False)

    try:
        PatientSchema().load(json_data)
        patient = Patient.update(patient_id, json_data)
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST

    patient_schema = PatientSchema()
    res = patient_schema.dump(patient)

    return res, HTTPStatus.OK


@patient_bp.route('/<int:patient_id>/', methods=['DELETE'])
def delete_patient(patient_id):
    patient = Patient.get_by_id(patient_id)

    if patient is None:
        return {'message': 'Patient not found'}, HTTPStatus.NOT_FOUND

    Patient.delete(patient)

    return HTTPStatus.NO_CONTENT  # 204


@patient_bp.route('/medical_card/', methods=['GET'])
def patient_medical_card():
    mc = db_session.query(MedicalCard).first()

    mc_schema = MedicalCardSchema()
    res = mc_schema.dumps(mc)

    return res
