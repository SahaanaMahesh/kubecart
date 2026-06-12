from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    product_id = Column(Integer)

    quantity = Column(Integer)

    status = Column(
        String,
        default="PLACED"
    )