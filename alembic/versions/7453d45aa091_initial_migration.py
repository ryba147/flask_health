"""Initial migration

Revision ID: 7453d45aa091
Revises: 
Create Date: 2022-01-04 22:19:12.092070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7453d45aa091'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Hospital',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('private', 'government', name='hospitaltypeenum'), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('address', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Patient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('gender', sa.Enum('male', 'female', name='genderenum'), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('phone_num', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('MedicalCard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('medical_conditions', sa.String(), nullable=True),
    sa.Column('allergies_reactions', sa.String(), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('blood_type', sa.Enum('O', 'A', 'B', 'AB', name='bloodtypeenum'), nullable=True),
    sa.Column('rh_factor', sa.Enum('positive', 'negative', name='rhesusfactorenum'), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['Patient.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('patient_id')
    )
    op.create_table('PatientHospital',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('hospital_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hospital_id'], ['Hospital.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['Patient.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('patient_id', 'hospital_id', name='PatientHospital_patient_id_hospital_id_uc')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('PatientHospital')
    op.drop_table('MedicalCard')
    op.drop_table('Patient')
    op.drop_table('Hospital')
    # ### end Alembic commands ###