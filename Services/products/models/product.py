from sqlalchemy import Column, Integer, String
from core.database import Base

class Product(Base):
    __tablename__ = "tbl_product"
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(45), nullable=False)
    Price= Column(Integer, nullable=False)
    Stock = Column(Integer, nullable=False)
    

    