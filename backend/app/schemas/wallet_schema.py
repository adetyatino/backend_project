from pydantic import BaseModel
from decimal import Decimal

class WalletResponse(BaseModel):
    id: int
    balance: Decimal
    frozen_balance: Decimal
