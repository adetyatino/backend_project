from sqlalchemy import Column, Integer, ForeignKey, Numeric
from app.core.database import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    balance = Column(Numeric(18,2), default=0)
    frozen_balance = Column(Numeric(18,2), default=0)

