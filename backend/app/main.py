from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.modules.auth.routes import router as auth_router
from app.modules.users.routes import router as user_router
from app.modules.accounts.routes import router as account_router
from app.modules.wallets.routes import router as wallet_router
from app.modules.transfers.routes import router as transfer_router
from app.modules.transactions.routes import router as transaction_router
from app.modules.investments.routes import router as investment_router
from app.modules.loans.routes import router as loan_router
from app.modules.notifications.routes import router as notification_router
from app.modules.payments.routes import router as payment_router

# ✅ BUAT APP DULU
app = FastAPI(title="Fintech Core Banking API")

# ✅ BARU TAMBAH MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # production ganti domain spesifik
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ INCLUDE ROUTER
app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(account_router, prefix="/api/accounts", tags=["Accounts"])
app.include_router(wallet_router, prefix="/api/wallets", tags=["Wallets"])
app.include_router(transfer_router, prefix="/api/transfers", tags=["Transfers"])
app.include_router(transaction_router, prefix="/api/transactions", tags=["Transactions"])
app.include_router(investment_router, prefix="/api/investments", tags=["Investments"])
app.include_router(loan_router, prefix="/api/loans", tags=["Loans"])
app.include_router(notification_router, prefix="/api/notifications", tags=["Notifications"])
app.include_router(payment_router, prefix="/api/payments", tags=["Payments"])
