from pydantic import BaseModel

class ProductBase(BaseModel):
    Name: str
    Price: int
    Stock: int
    
class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    Id: int
    
    model_config = {
        "from_attributes": True
    }
    