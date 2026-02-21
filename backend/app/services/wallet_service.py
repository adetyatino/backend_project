from app.repositories.wallet_repo import get_wallet
from app.core.exceptions import NotFoundException

def get_wallet_balance(db, wallet_id: int):
    wallet = get_wallet(db, wallet_id)
    if not wallet:
        raise NotFoundException("Wallet not found")
    return wallet
