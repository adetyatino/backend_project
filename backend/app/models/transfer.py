from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True)
    reference_no = Column(String(50), index=True)
    sender_wallet_id = Column(Integer, ForeignKey("wallets.id"))
    receiver_wallet_id = Column(Integer, ForeignKey("wallets.id"))
    amount = Column(Numeric(18,2))
    fee = Column(Numeric(18,2), default=0)
    status = Column(String(20), default="success")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
