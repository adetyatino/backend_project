# app/modules/transfers/routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.transfer_service import transfer

router = APIRouter()

@router.post("/")
def transfer_money(sender_wallet_id: int, receiver_wallet_id: int, amount: float, db: Session = Depends(get_db)):
    transfer(db, sender_wallet_id, receiver_wallet_id, amount)
    return {"message": "Transfer successful"}
