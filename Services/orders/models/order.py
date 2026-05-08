from sqlalchemy import Column, Integer
from core.database import Base

class Order(Base):
    __tablename__ = "tbl_order"

    Id = Column(Integer, primary_key=True, index=True)
    ProductId = Column(Integer, nullable=False)
    Quantity = Column(Integer, nullable=False)
    TotalPrice = Column(Integer, nullable=False)