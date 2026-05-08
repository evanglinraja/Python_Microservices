from sqlalchemy.orm import Session
from models.order import Order
from schemas.order import OrderCreate

def get_all_order(db: Session):
    return db.query(Order).all()

def create_order(db: Session, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.Id == order_id).first()

def update_order(db: Session, order_id: int, order: OrderCreate):
    db_order = get_order_by_id(db, order_id)
    if not db_order:
        return None # Order not found
    for key, value in order.dict().items():
        setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = get_order_by_id(db, order_id)
    if not db_order:
        return None # Order not found
    db.delete(db_order)
    db.commit()
    return True
