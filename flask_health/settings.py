import os

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI',
                                    'postgresql://postgres:newpassword@localhost:5432/flask_health_db')
