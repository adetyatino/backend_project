from sqlalchemy.orm import Session
from app.models.wallet import Wallet

def get_wallet(db: Session, wallet_id: int):
    return db.query(Wallet).filter(Wallet.id == wallet_id).first()
