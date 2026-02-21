from sqlalchemy.orm import Session
from app.models.wallet import Wallet
from app.models.transaction import Transaction
from app.utils.reference_generator import generate_reference

def transfer(db: Session, sender_id: int, receiver_id: int, amount: float):

    with db.begin():

        sender = db.query(Wallet)\
            .filter(Wallet.id == sender_id)\
            .with_for_update()\
            .first()

        receiver = db.query(Wallet)\
            .filter(Wallet.id == receiver_id)\
            .with_for_update()\
            .first()

        if sender.balance < amount:
            raise Exception("Insufficient balance")

        sender.balance -= amount
        receiver.balance += amount

        ref = generate_reference()

        db.add(Transaction(
            reference_no=ref,
            wallet_id=sender.id,
            type="debit",
            amount=amount
        ))

        db.add(Transaction(
            reference_no=ref,
            wallet_id=receiver.id,
            type="credit",
            amount=amount
        ))

