from sqlalchemy import Integer, Column, String, Enum, Float, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref

from flask_health.constants import GenderEnum, BloodTypeEnum, RhesusFactorEnum
from flask_health.database import Base


class Patient(Base):
    __tablename__ = 'Patient'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    gender = Column(Enum(GenderEnum))
    email = Column(String(64))
    phone_num = Column(String(32))

    # hospitals = relationship('Hospital', secondary='PatientHospital', backref='patients')

    def __repr__(self):
        return f'<User(name={self.first_name}, last_name={self.last_name})>'


class PatientHospital(Base):
    __tablename__ = 'PatientHospital'
    __table_args__ = (
        UniqueConstraint('patient_id', 'hospital_id', name='PatientHospital_patient_id_hospital_id_uc'),
    )

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('Patient.id'), nullable=False)  # nullable=True only when CREATE TABLE
    hospital_id = Column(Integer, ForeignKey('Hospital.id'), nullable=False)


class MedicalCard(Base):
    __tablename__ = 'MedicalCard'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('Patient.id'), nullable=False, unique=True)  # unique!
    # works even without backref. medical_card.patient
    patient = relationship('Patient', backref=backref('MedicalCard', uselist=False))
    medical_conditions = Column(String)
    allergies_reactions = Column(String)
    birth_date = Column(DateTime)
    height = Column(Float)
    weight = Column(Float)
    blood_type = Column(Enum(BloodTypeEnum))  # create_type in psql
    rh_factor = Column(Enum(RhesusFactorEnum))
