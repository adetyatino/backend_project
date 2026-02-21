from sqlalchemy.orm import Session
from app.models.wallet.wallet import Wallet
from app.models.transaction import Transaction



def transfer(db: Session, sender_id, receiver_id, amount):

    sender = db.query(Wallet).filter_by(user_id=sender_id).with_for_update().first()
    receiver = db.query(Wallet).filter_by(user_id=receiver_id).with_for_update().first()

    if sender.balance < amount:
        raise Exception("Insufficient funds")

    sender.balance -= amount
    receiver.balance += amount

    tx = Transaction(
        sender_wallet_id=sender.id,
        receiver_wallet_id=receiver.id,
        amount=amount,
        status="success",
    )

    db.add(tx)
    db.commit()
    db.refresh(tx)

    return tx
