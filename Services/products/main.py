from fastapi import FastAPI
from core.database import engine
from models import product
from api.router import api_router

product.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Product API")
app.include_router(api_router,prefix="/api")