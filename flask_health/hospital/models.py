from typing import Optional, List, Dict

from sqlalchemy import Integer, Column, String, Enum
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from flask_health.constants import HospitalTypeEnum
from flask_health.database import Base, db_session
from flask_health.hospital.schemas import HospitalSchema


class Hospital(Base):
    __tablename__ = 'Hospital'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(HospitalTypeEnum))
    name = Column(String(128))
    description = Column(String)
    address = Column(String(512))
    patients = relationship('Patient', secondary='PatientHospital', backref='hospitals')

    def __repr__(self):
        return f'<Hospital(name={self.name}, description={self.description})>'

    @classmethod
    def add_from_json(cls, json_data: Dict) -> Optional['Hospital']:
        hospital = Hospital(**json_data)
        try:
            db_session.add(hospital)
            db_session.commit()
        except IntegrityError:
            db_session.rollback()

        return hospital
        # pass a dict, create an object. if error return None

    @classmethod
    def delete(cls, hospital):  # ->
        try:
            db_session.delete(hospital)
            db_session.commit()
        except IntegrityError:  # rollback and raise
            db_session.rollback()
            # rollback and raise. global exception handler

    @classmethod
    def update(cls, id: int, json_data: Dict) -> Optional['Hospital']:  # int from typing ??
        # hospital.type = json_data.get('type', hospital.type)
        # hospital.name = json_data.get('name', hospital.name)
        # hospital.description = json_data.get('description', hospital.description)
        # hospital.address = json_data.get('address', hospital.address)

        db_session.query(cls).filter_by(id=id).update(dict(json_data))
        db_session.commit()

        res = cls.get_by_id(id)

        return res

    @classmethod
    def get_all(cls) -> List[HospitalSchema]:
        return db_session.query(cls).all()

    @classmethod
    def get_by_id(cls, id: int) -> Optional['Hospital']:  # UUID?
        return db_session.query(cls).filter_by(id=id).one_or_none()
