from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from ..database import get_db

from ..models import Order

from ..schemas import OrderCreate

from ..kafka_producer import publish_event

router = APIRouter()


@router.post("/orders")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):

    new_order = Order(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity
    )

    db.add(new_order)

    db.commit()

    db.refresh(new_order)

    publish_event(
        "ORDER_CREATED",
        {
            "id": new_order.id,
            "user_id": new_order.user_id,
            "product_id": new_order.product_id
        }
    )

    return new_order


@router.get("/orders")
def get_orders(
    db: Session = Depends(get_db)
):

    return db.query(Order).all()


@router.get("/orders/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Order).filter(
        Order.id == order_id
    ).first()