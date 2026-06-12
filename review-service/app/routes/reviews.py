from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Review
from ..schemas import ReviewCreate

router = APIRouter()


@router.post("/reviews")
def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):

    new_review = Review(
        user_id=review.user_id,
        product_id=review.product_id,
        rating=review.rating,
        comment=review.comment
    )

    db.add(new_review)

    db.commit()

    db.refresh(new_review)

    return new_review


@router.get("/reviews")
def get_reviews(
    db: Session = Depends(get_db)
):
    return db.query(Review).all()


@router.get("/reviews/{product_id}")
def get_product_reviews(
    product_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Review).filter(
        Review.product_id == product_id
    ).all()