from marshmallow import Schema, fields


class PatientSchema(Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    gender = fields.Str()
    email = fields.Str()
    phone_num = fields.Str()
    # hospitals = fields.Nested(HospitalSchema, many=True)
