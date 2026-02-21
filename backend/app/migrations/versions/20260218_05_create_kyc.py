revision = "05_create_kyc"
down_revision = "04_create_audit_logs"

def upgrade():
    op.create_table(
        "kyc",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("document_type", sa.String(50)),
        sa.Column("document_url", sa.String(255)),
        sa.Column("status", sa.String(20), default="pending"),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    )


def downgrade():
    op.drop_table("kyc")
