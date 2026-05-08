from fastapi import APIRouter
from api.endpoints import order

api_router = APIRouter()
api_router.include_router(order.router, prefix="/orders", tags=["orders"])
