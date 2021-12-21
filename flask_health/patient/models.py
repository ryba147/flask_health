from sqlalchemy import Integer, Column, String, Enum, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from flask_health.database import Base


class PatientHospital(Base):
    __tablename__ = 'PatientHospital'

    # unique (patient_id, hospital_id)
    # https://newbedev.com/sqlalchemy-unique-across-multiple-columns
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('Patient.id'), nullable=False, unique=True)  # trouble
    hospital_id = Column(Integer, ForeignKey('Hospital.id'), nullable=False, unique=True)


class Patient(Base):
    __tablename__ = 'Patient'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    gender = Column(Enum('female', 'male', name='gender_enum', create_type=False))
    email = Column(String(64))
    phone_num = Column(String(32))

    # hospitals = relationship('Hospital', secondary=PatientHospital, backref='patients')

    # medical_card_id = relationship('MedicalCard', backref=backref('MedicalCard', uselist=False))  # ??????? or fk

    def __repr__(self):
        return f'<User(name={self.first_name}, last_name={self.last_name})>'


class MedicalCard(Base):
    __tablename__ = 'MedicalCard'

    id = Column(Integer, primary_key=True)
    medical_conditions = Column(String)
    allergies_reactions = Column(String)
    birth_date = Column(DateTime)
    height = Column(Float)  # conversion ?
    weight = Column(Float)
    blood_type = Column(Enum('female', 'male', name='gender_enum', create_type=False))
    rh_factor = Column(Enum('negative', 'positive', name='rhesus_enum', create_type=False))
