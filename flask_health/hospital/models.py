from typing import Optional, List, Dict

from sqlalchemy import Integer, Column, String, Enum
from sqlalchemy.exc import DatabaseError
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
    def add(cls, json_data: Dict) -> Optional['Hospital']:
        hospital = Hospital(**json_data)
        try:
            db_session.add(hospital)
            db_session.commit()
        except DatabaseError:
            db_session.rollback()
            raise

        return hospital

    @classmethod
    def delete(cls, hospital) -> None:
        try:
            db_session.delete(hospital)
            db_session.commit()
        except DatabaseError:
            db_session.rollback()
            raise

    @classmethod
    def update(cls, id: int, json_data: Dict) -> Optional['Hospital']:

        db_session.query(cls).filter_by(id=id).update(json_data)
        db_session.commit()

        res = cls.get_by_id(id)

        return res

    @classmethod
    def get_all(cls) -> List[HospitalSchema]:
        return db_session.query(cls).all()

    @classmethod
    def get_by_id(cls, id: int) -> Optional['Hospital']:
        return db_session.query(cls).filter_by(id=id).one_or_none()
