from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.String(length=64), primary_key=True),
        sa.Column("phone", sa.String(length=20), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=True),
        sa.Column("full_name", sa.String(length=120), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index("ix_users_phone", "users", ["phone"], unique=True)

    op.create_table(
        "vehicles",
        sa.Column("id", sa.String(length=64), primary_key=True),
        sa.Column("registration_number", sa.String(length=20), nullable=False),
        sa.Column("make", sa.String(length=100), nullable=False),
        sa.Column("model", sa.String(length=100), nullable=False),
        sa.Column("fuel_type", sa.String(length=40), nullable=False),
        sa.Column("owner_count", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("insurance_status", sa.String(length=40), nullable=False, server_default="unknown"),
        sa.Column("challan_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("trust_score", sa.Integer(), nullable=False, server_default="50"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index("ix_vehicles_registration_number", "vehicles", ["registration_number"], unique=True)

    op.create_table(
        "reports",
        sa.Column("id", sa.String(length=64), primary_key=True),
        sa.Column("user_id", sa.String(length=64), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("vehicle_id", sa.String(length=64), sa.ForeignKey("vehicles.id"), nullable=False),
        sa.Column("registration_number", sa.String(length=20), nullable=False),
        sa.Column("trust_score", sa.Integer(), nullable=False, server_default="50"),
        sa.Column("payment_status", sa.String(length=20), nullable=False, server_default="unpaid"),
        sa.Column("recommendation", sa.String(length=255), nullable=True),
        sa.Column("risk_signals", sa.JSON(), nullable=True),
        sa.Column("pdf_url", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

    op.create_table(
        "payments",
        sa.Column("id", sa.String(length=64), primary_key=True),
        sa.Column("report_id", sa.String(length=64), sa.ForeignKey("reports.id"), nullable=False),
        sa.Column("user_id", sa.String(length=64), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("gateway", sa.String(length=30), nullable=False, server_default="mock"),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.Column("currency", sa.String(length=10), nullable=False, server_default="INR"),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="created"),
        sa.Column("gateway_order_id", sa.String(length=100), nullable=True),
        sa.Column("gateway_payment_id", sa.String(length=100), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

    op.create_table(
        "otp_codes",
        sa.Column("id", sa.String(length=64), primary_key=True),
        sa.Column("phone", sa.String(length=20), nullable=False),
        sa.Column("code", sa.String(length=10), nullable=False),
        sa.Column("is_used", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

def downgrade():
    op.drop_table("otp_codes")
    op.drop_table("payments")
    op.drop_table("reports")
    op.drop_index("ix_vehicles_registration_number", table_name="vehicles")
    op.drop_table("vehicles")
    op.drop_index("ix_users_phone", table_name="users")
    op.drop_table("users")
