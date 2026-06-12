from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Product
from ..schemas import ProductCreate
from ..kafka_producer import publish_event

router = APIRouter()


@router.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):

    new_product = Product(**product.dict())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    publish_event("PRODUCT_CREATED", {
        "id": new_product.id,
        "name": new_product.name,
        "price": new_product.price
    })

    return new_product


@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.id == product_id).first()