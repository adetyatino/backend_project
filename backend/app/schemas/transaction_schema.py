from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime

class TransactionResponse(BaseModel):
    reference_no: str
    type: str
    amount: Decimal
    status: str
    created_at: datetime
