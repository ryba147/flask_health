from flask import Flask
from flask_health.patient.routes import patient_bp
from flask_health.hospital.routes import hospital_bp
from flask_health.routes import common_bp

app = Flask(__name__)  # print(app.config)
# app.config['SECRET_KEY'] = 'super-secret'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.register_blueprint(patient_bp)
app.register_blueprint(hospital_bp)
app.register_blueprint(common_bp)

from flask_health.database import db_session
from flask_health.database import init_db  # for docker to init database

init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
