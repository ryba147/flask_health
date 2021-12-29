from http import HTTPStatus

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from flask_health.patient.models import Patient, MedicalCard
from flask_health.patient.schemas import PatientSchema, MedicalCardSchema, QueryFiltersSchema

patient_bp = Blueprint('patient_bp', __name__, url_prefix='/patient')


@patient_bp.route('/', methods=['GET'])
def get_patient_list():
    filters = request.args

    # QueryFiltersSchema is it a correct name? check validate=OneOf([...]) in schemas.py
    try:
        QueryFiltersSchema().load(filters)
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST

    patients = Patient.get_all(filters)
    patient_schema = PatientSchema(many=True)
    res = patient_schema.dump(patients)
    return jsonify(res), HTTPStatus.OK


@patient_bp.route('/<int:patient_id>/', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.get_by_id(patient_id)

    if patient is None:
        return {'message': 'Patient not found'}, HTTPStatus.NOT_FOUND

    patient_schema = PatientSchema()
    res = patient_schema.dump(patient)
    return jsonify(res), HTTPStatus.OK


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

    return {}, HTTPStatus.NO_CONTENT  # 204


@patient_bp.route('/<int:patient_id>/medical_card/', methods=['GET'])
def get_patient_medical_card(patient_id):
    if Patient.get_by_id(patient_id) is None:
        return {'message': 'Patient not found'}, HTTPStatus.NOT_FOUND

    medical_card = MedicalCard.get_by_patient_id(patient_id)

    if medical_card is None:
        return {'message': f'Patient with id {patient_id} has no medical card'}, HTTPStatus.NOT_FOUND

    mc_schema = MedicalCardSchema()
    res = mc_schema.dumps(medical_card)

    return res, HTTPStatus.OK


@patient_bp.route('/<int:patient_id>/medical_card/', methods=['POST'])
def add_medical_card(patient_id):
    if MedicalCard.get_by_patient_id(patient_id):
        return {'message': 'Patient already has a medical card'}, HTTPStatus.BAD_REQUEST

    json_data = request.get_json(silent=False)
    json_data.update({"patient_id": patient_id})

    try:
        MedicalCardSchema().load(json_data)
        medical_card = MedicalCard.add(json_data)
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST

    mc_schema = MedicalCardSchema()
    res = mc_schema.dump(medical_card)

    return res, HTTPStatus.CREATED


@patient_bp.route('/<int:patient_id>/medical_card/', methods=['PUT'])
def update_medical_card(patient_id):
    if not MedicalCard.get_by_patient_id(patient_id):
        return {'message': 'Patient not found'}, HTTPStatus.NOT_FOUND

    json_data = request.get_json(silent=False)

    try:
        MedicalCardSchema().load(json_data)
        medical_card = MedicalCard.update(patient_id, json_data)
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST

    mc_schema = MedicalCardSchema()
    res = mc_schema.dump(medical_card)

    return res, HTTPStatus.OK


@patient_bp.route('/<int:patient_id>/medical_card/', methods=['DELETE'])
def delete_patient_medical_card(patient_id):
    medical_card = MedicalCard.get_by_patient_id(patient_id)

    if medical_card is None:
        return {'message': 'Medical card not found'}, HTTPStatus.NOT_FOUND

    MedicalCard.delete(medical_card)

    return {}, HTTPStatus.NO_CONTENT
