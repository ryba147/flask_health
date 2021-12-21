from marshmallow import Schema, fields

from flask_health.patient.schemas import PatientSchema


class HospitalSchema(Schema):
    id = fields.Integer(dump_only=True)
    type = fields.Str()
    name = fields.Str()
    description = fields.Str()
    address = fields.Str()
    patients = fields.Nested(PatientSchema, many=True)
