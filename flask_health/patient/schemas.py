from marshmallow import Schema, fields


class PatientSchema(Schema):
    id = fields.Integer()  # dump_only=True
    first_name = fields.Str()
    last_name = fields.Str()
    gender = fields.Str()
    email = fields.Str()
    phone_num = fields.Str()
    # hospitals = fields.Nested(HospitalSchema, many=True)


class MedicalCardSchema(Schema):
    id = fields.Integer()
    patient_id = fields.Integer()
    medical_conditions = fields.Str()
    allergies_reactions = fields.Str()
    birth_date = fields.DateTime()
    height = fields.Float()
    weight = fields.Float()
    blood_type = fields.Str()
    rh_factor = fields.Str()
