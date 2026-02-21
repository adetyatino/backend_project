from pydantic import BaseModel
from decimal import Decimal

class TransferRequest(BaseModel):
    sender_wallet_id: int
    receiver_wallet_id: int
    amount: Decimal
