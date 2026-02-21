from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.wallet_service import get_wallet_balance

router = APIRouter()

@router.get("/{wallet_id}")
def get_wallet(wallet_id: int, db: Session = Depends(get_db)):
    return get_wallet_balance(db, wallet_id)
