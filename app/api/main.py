from fastapi import APIRouter

from api.routes import user, category

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(category.router, prefix="/category", tags=["category"])