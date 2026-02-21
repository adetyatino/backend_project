from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    reference_no = Column(String(50), index=True)
    wallet_id = Column(Integer)
    type = Column(String(10))  # debit / credit
    amount = Column(Numeric(18,2))
    status = Column(String(20), default="success")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

