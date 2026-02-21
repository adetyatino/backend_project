def create_account(db, user_id):
    account = Account(
        user_id=user_id,
        account_number=generate_account_number()
    )
    db.add(account)
    db.flush()

    wallet = Wallet(account_id=account.id, balance=0)
    db.add(wallet)

    db.commit()
    db.refresh(account)
    return account
