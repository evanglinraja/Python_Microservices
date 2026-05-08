from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.order import OrderCreate, OrderResponse
from curd.order import get_all_order, create_order, get_order_by_id, update_order, delete_order
from dependencies.db import get_db

router = APIRouter()

@router.get("/", response_model=list[OrderResponse])
def read_all(db: Session = Depends(get_db)):
    return get_all_order(db)

@router.post("/", response_model=OrderResponse)
def create(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)

@router.get("/{order_id}", response_model=OrderResponse)
def read(order_id: int, db: Session = Depends(get_db)):
    order = get_order_by_id(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=OrderResponse)
def update(order_id: int, order: OrderCreate, db: Session = Depends(get_db)):
    updated = update_order(db, order_id, order)
    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated

@router.delete("/{order_id}")
def delete(order_id: int, db: Session = Depends(get_db)):
    deleted = delete_order(db, order_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"detail": "Order deleted successfully"}