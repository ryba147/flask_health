from sqlalchemy import Integer, Column, String, Enum
from sqlalchemy.orm import relationship

from flask_health.constants import HospitalTypeEnum
from flask_health.database import Base


class Hospital(Base):
    __tablename__ = 'Hospital'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(HospitalTypeEnum))
    name = Column(String(128))
    description = Column(String)
    address = Column(String(512))
    patients = relationship('Patient', secondary='PatientHospital', backref='hospitals')
