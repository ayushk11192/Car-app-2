"""initial"""

from alembic import op
import sqlalchemy as sa

revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('phone', sa.String(length=20), nullable=False), sa.Column('name', sa.String(length=100), nullable=True))
    op.create_table('vehicles', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('registration_number', sa.String(length=20)), sa.Column('make', sa.String(length=100)), sa.Column('model', sa.String(length=100)), sa.Column('fuel_type', sa.String(length=50)))
    op.create_table('reports', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('user_id', sa.Integer()), sa.Column('vehicle_id', sa.Integer()), sa.Column('status', sa.String(length=20)), sa.Column('trust_score', sa.Integer()), sa.Column('payload', sa.JSON()))
    op.create_table('payments', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('report_id', sa.Integer()), sa.Column('status', sa.String(length=20)), sa.Column('gateway_order_id', sa.String(length=100), nullable=True))


def downgrade():
    op.drop_table('payments')
    op.drop_table('reports')
    op.drop_table('vehicles')
    op.drop_table('users')
