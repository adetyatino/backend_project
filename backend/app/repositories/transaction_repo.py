from sqlalchemy.orm import Session
from app.models.transaction import Transaction

def get_transactions_by_wallet(db: Session, wallet_id: int):
    return db.query(Transaction)\
        .filter(Transaction.wallet_id == wallet_id)\
        .order_by(Transaction.created_at.desc())\
        .all()
