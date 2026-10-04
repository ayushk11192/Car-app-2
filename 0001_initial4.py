"""initial schema

Revision ID: 0001_initial
Revises:
Create Date: 2026-04-17 00:00:00
"""

from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("phone", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("google_id", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_users_id", "users", ["id"])
    op.create_index("ix_users_phone", "users", ["phone"])

    op.create_table(
        "vehicles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("registration_number", sa.String(), nullable=False),
        sa.Column("chassis_number", sa.String(), nullable=True),
        sa.Column("engine_number", sa.String(), nullable=True),
        sa.Column("make", sa.String(), nullable=True),
        sa.Column("model", sa.String(), nullable=True),
        sa.Column("variant", sa.String(), nullable=True),
        sa.Column("fuel_type", sa.String(), nullable=True),
        sa.Column("registration_date", sa.Date(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    op.create_index("ix_vehicles_id", "vehicles", ["id"])
    op.create_index("ix_vehicles_registration_number", "vehicles", ["registration_number"])

    op.create_table(
        "reports",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("vehicle_id", sa.Integer(), nullable=False),
        sa.Column("trust_score", sa.Integer(), nullable=False),
        sa.Column("overall_status", sa.String(), nullable=False),
        sa.Column("report_data", sa.JSON(), nullable=False),
        sa.Column("pdf_url", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.ForeignKeyConstraint(["vehicle_id"], ["vehicles.id"]),
    )
    op.create_index("ix_reports_id", "reports", ["id"])

    op.create_table(
        "payments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("report_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("currency", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("transaction_id", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.ForeignKeyConstraint(["report_id"], ["reports.id"]),
    )
    op.create_index("ix_payments_id", "payments", ["id"])

    op.create_table(
        "otp_tokens",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("phone", sa.String(), nullable=False),
        sa.Column("otp_hash", sa.String(), nullable=False),
        sa.Column("is_used", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("expires_at", sa.DateTime(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    op.create_index("ix_otp_tokens_id", "otp_tokens", ["id"])
    op.create_index("ix_otp_tokens_phone", "otp_tokens", ["phone"])


def downgrade() -> None:
    op.drop_index("ix_otp_tokens_phone", table_name="otp_tokens")
    op.drop_index("ix_otp_tokens_id", table_name="otp_tokens")
    op.drop_table("otp_tokens")
    op.drop_index("ix_payments_id", table_name="payments")
    op.drop_table("payments")
    op.drop_index("ix_reports_id", table_name="reports")
    op.drop_table("reports")
    op.drop_index("ix_vehicles_registration_number", table_name="vehicles")
    op.drop_index("ix_vehicles_id", table_name="vehicles")
    op.drop_table("vehicles")
    op.drop_index("ix_users_phone", table_name="users")
    op.drop_index("ix_users_id", table_name="users")
    op.drop_table("users")
