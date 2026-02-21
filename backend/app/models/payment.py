from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    bill_type = Column(String(100))
    amount = Column(Numeric(18,2))
    status = Column(String(20), default="success")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
