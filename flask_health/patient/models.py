from sqlalchemy import Integer, Column, String, Enum

from flask_health.database import Base


# class GenderEnum(enum.Enum):
#     pass

# class methods?, dialects psql, init_db

class Patient(Base):
    __tablename__ = 'Patient'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    gender = Column(Enum("female", "male", name="gender_enum", create_type=False))
    email = Column(String(64))
    phone_num = Column(String(32))

    # medical_card =
    def __repr__(self):
        return f'<User(name={self.first_name}, last_name={self.last_name})>'
