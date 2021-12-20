# where should this file be located?
# flask_health/flask_health or flask_health/ ?

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pgnulp@localhost:5432/flask_health_db'

engine = create_engine(SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker)

Base = declarative_base()


def init_db():
    import flask_health.patient.models
    Base.metadata.create_all(bind=engine)
