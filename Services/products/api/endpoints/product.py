from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.product import ProductCreate, ProductResponse
from curd.product import get_all_products, create_product, get_product_by_id, update_product,delete_product
from dependencies.db import get_db

router = APIRouter()

@router.get("/", response_model=list[ProductResponse])
def read_all(db: Session = Depends(get_db)):
    return get_all_products(db)

@router.get("/{product_id}", response_model=ProductResponse)
def read(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=ProductResponse)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.put("/{product_id}", response_model=ProductResponse)
def update(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    updated = update_product(db, product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated
        
@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    deleted = delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully"}

