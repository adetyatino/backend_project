from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "01_create_users"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("full_name", sa.String(150), nullable=False),
        sa.Column("email", sa.String(150), nullable=False, unique=True),
        sa.Column("phone", sa.String(20), nullable=False, unique=True),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column("transaction_pin_hash", sa.String(255)),
        sa.Column("is_verified", sa.Boolean(), default=False),
        sa.Column("kyc_status", sa.String(20), default="pending"),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now()),
    )

    op.create_index("idx_users_email", "users", ["email"])
    op.create_index("idx_users_phone", "users", ["phone"])


def downgrade():
    op.drop_table("users")
