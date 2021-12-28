from typing import Optional, Dict, List

from sqlalchemy import Integer, Column, String, Enum, Float, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import relationship, backref

from flask_health.constants import GenderEnum, BloodTypeEnum, RhesusFactorEnum
from flask_health.database import Base, db_session
from flask_health.patient.schemas import PatientSchema, MedicalCardSchema


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

    @classmethod
    def add(cls, json_data: Dict) -> Optional['Patient']:
        patient = Patient(**json_data)
        try:
            db_session.add(patient)
            db_session.commit()
        except DatabaseError:
            db_session.rollback()
            raise

        return patient

    @classmethod
    def delete(cls, patient) -> None:
        try:
            db_session.delete(patient)
            db_session.commit()
        except DatabaseError:
            db_session.rollback()
            raise

    @classmethod
    def update(cls, id: int, json_data: Dict) -> Optional['Patient']:
        db_session.query(cls).filter_by(id=id).update(json_data)
        db_session.commit()

        res = cls.get_by_id(id)

        return res

    @classmethod
    def get_all(cls) -> List[PatientSchema]:
        return db_session.query(cls).all()

    @classmethod
    def get_by_id(cls, id: int) -> Optional['Patient']:
        return db_session.query(cls).filter_by(id=id).one_or_none()


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
    patient_id = Column(Integer, ForeignKey('Patient.id'), nullable=False, unique=True)
    patient = relationship('Patient', backref=backref('MedicalCard',
                                                      uselist=False))  # works even without backref. medical_card.patient
    medical_conditions = Column(String)
    allergies_reactions = Column(String)
    birth_date = Column(DateTime)
    height = Column(Float)
    weight = Column(Float)
    blood_type = Column(Enum(BloodTypeEnum))  # create_type in psql
    rh_factor = Column(Enum(RhesusFactorEnum))

    def __repr__(self):
        return f'<MedicalCard(patient_id={self.patient_id}, patient={self.patient})>'

    @classmethod
    def get_by_patient_id(cls, patient_id: int) -> Optional['MedicalCard']:
        return db_session.query(cls).filter_by(patient_id=patient_id).one_or_none()

    @classmethod
    def add(cls, json_data: Dict) -> Optional['MedicalCard']:
        medical_card = MedicalCard(**json_data)
        try:
            db_session.add(medical_card)
            db_session.commit()
        except DatabaseError:
            db_session.rollback()
            raise

        return medical_card

    @classmethod
    def delete(cls, medical_card) -> None:
        try:
            db_session.delete(medical_card)
            db_session.commit()
        except DatabaseError:
            db_session.rollback()
            raise
