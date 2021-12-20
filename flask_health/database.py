import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

os.environ['db_url'] = 'postgresql://postgres:pgnulp@localhost:5432/flask_health_db'
SQLALCHEMY_DATABASE_URI = os.environ['db_url']  # ubuntu psql users

engine = create_engine(SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker)

Base = declarative_base()


def init_db():
    import flask_health.patient.models
    import flask_health.hospital.models
    Base.metadata.create_all(bind=engine)


def drop_tables():
    import flask_health.patient.models
    import flask_health.hospital.models
    Base.metadata.drop_all(bind=engine)
