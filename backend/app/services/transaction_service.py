from app.repositories.transaction_repo import get_transactions_by_wallet

def get_wallet_transactions(db, wallet_id: int):
    return get_transactions_by_wallet(db, wallet_id)
