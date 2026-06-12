from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    product_id = Column(Integer)

    rating = Column(Integer)

    comment = Column(String)