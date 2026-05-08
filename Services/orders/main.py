from fastapi import FastAPI
from core.database import engine
from models import order
from api.router import api_router

order.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Order API")
app.include_router(api_router,prefix="/api")