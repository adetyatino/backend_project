from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class OTP(Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    code = Column(String(6))
    expires_at = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
