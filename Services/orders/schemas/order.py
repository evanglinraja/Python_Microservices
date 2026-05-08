from pydantic import BaseModel

class OrderBase(BaseModel):
    ProductId: int
    Quantity: int
    TotalPrice: int
    
class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    Id: int

    model_config={
        "from_attributes": True
    }
        