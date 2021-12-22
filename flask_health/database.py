from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from flask_health.settings import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()


def init_db():
    import flask_health.patient.models
    import flask_health.hospital.models
    Base.metadata.create_all(bind=engine)


def drop_tables():
    import flask_health.patient.models
    import flask_health.hospital.models
    Base.metadata.drop_all(bind=engine)
