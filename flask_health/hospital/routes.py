from http import HTTPStatus

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from flask_health.hospital.models import Hospital
from flask_health.hospital.schemas import HospitalSchema

hospital_bp = Blueprint('hospital_bp', __name__, url_prefix='/hospital')


@hospital_bp.route('/', methods=['GET'])
def get_list():
    hospitals = Hospital.get_all()
    hospital_schema = HospitalSchema(many=True)
    res = hospital_schema.dump(hospitals)
    return jsonify(res)


@hospital_bp.route('/<int:hospital_id>/', methods=['GET'])
def get_hospital(hospital_id):
    hospital = Hospital.get_by_id(hospital_id)

    if hospital is None:
        return {'message': 'Hospital not found'}, HTTPStatus.NOT_FOUND

    hospital_schema = HospitalSchema()
    res = hospital_schema.dump(hospital)
    return res, HTTPStatus.OK


@hospital_bp.route('/', methods=['POST'])
def add_hospital():
    json_data = request.get_json(silent=False)

    try:
        HospitalSchema().load(json_data)
        hospital = Hospital.add(json_data)
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST

    hospital_schema = HospitalSchema()
    res = hospital_schema.dump(hospital)

    return res, HTTPStatus.CREATED


@hospital_bp.route('/<int:hospital_id>/', methods=['PUT'])
def update_hospital(hospital_id):

    if not Hospital.get_by_id(hospital_id):
        return {'message': 'Hospital not found'}, HTTPStatus.NOT_FOUND

    json_data = request.get_json(silent=False)

    try:
        HospitalSchema().load(json_data)  # Validation
        hospital = Hospital.update(hospital_id, json_data)
    except ValidationError as err:
        return err.messages, HTTPStatus.BAD_REQUEST

    hospital_schema = HospitalSchema()
    res = hospital_schema.dump(hospital)

    return res, HTTPStatus.OK


@hospital_bp.route('/<int:hospital_id>/', methods=['DELETE'])
def delete_hospital(hospital_id):
    hospital = Hospital.get_by_id(hospital_id)

    if hospital is None:
        return {'message': 'Hospital not found'}, HTTPStatus.NOT_FOUND

    Hospital.delete(hospital)

    return {}, HTTPStatus.NO_CONTENT
