revision = "02_create_wallets"
down_revision = "01_create_users"

def upgrade():
    op.create_table(
        "wallets",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("balance", sa.Numeric(18, 2), default=0),
        sa.Column("currency", sa.String(10), default="IDR"),
        sa.Column("status", sa.String(20), default="active"),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    )

    op.create_index("idx_wallet_user", "wallets", ["user_id"])


def downgrade():
    op.drop_table("wallets")
