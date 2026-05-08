from fastapi import APIRouter
from api.endpoints import product

api_router = APIRouter()
api_router.include_router(product.router, prefix="/products", tags=["Products"])