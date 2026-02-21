revision = "03_create_transactions"
down_revision = "02_create_wallets"

def upgrade():
    op.create_table(
        "transactions",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("reference_no", sa.String(50), unique=True),
        sa.Column("sender_wallet_id", postgresql.UUID(as_uuid=True)),
        sa.Column("receiver_wallet_id", postgresql.UUID(as_uuid=True)),
        sa.Column("amount", sa.Numeric(18, 2), nullable=False),
        sa.Column("fee", sa.Numeric(18, 2), default=0),
        sa.Column("type", sa.String(30)),
        sa.Column("status", sa.String(20), default="pending"),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["sender_wallet_id"], ["wallets.id"]),
        sa.ForeignKeyConstraint(["receiver_wallet_id"], ["wallets.id"]),
    )

    op.create_index("idx_tx_sender", "transactions", ["sender_wallet_id"])
    op.create_index("idx_tx_receiver", "transactions", ["receiver_wallet_id"])
    op.create_index("idx_tx_reference", "transactions", ["reference_no"])


def downgrade():
    op.drop_table("transactions")
