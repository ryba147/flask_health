from flask import Flask
from flask_health.patient.routes import patient_bp

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'super-secret'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.register_blueprint(patient_bp)

# db = SQLAlchemy(app)
