from fastapi import APIRouter

from api.routes import user, category, transaction, wallet

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(category.router, prefix="/category", tags=["category"])
api_router.include_router(transaction.router, prefix="/transaction", tags=["transaction"])
api_router.include_router(wallet.router, prefix="/wallet", tags=["wallet"])