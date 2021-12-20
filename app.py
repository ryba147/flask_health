from flask import Flask
from flask_health.patient.routes import patient_bp
from flask_health.hospital.routes import hospital_bp

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'super-secret'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.register_blueprint(patient_bp)
app.register_blueprint(hospital_bp)

# ???
from flask_health.database import db_session


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# db = SQLAlchemy(app)
