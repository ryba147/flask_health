from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from patient.views import patient_bp

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.register_blueprint(patient_bp, url_prefix='/patient')

db = SQLAlchemy(app)

from flask_health import routes
