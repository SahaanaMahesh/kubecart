from fastapi import APIRouter

router = APIRouter()


@router.get("/recommendations")
def get_recommendations():

    return [
        {
            "product_id": 1,
            "product_name": "MacBook Air",
            "category": "Electronics"
        },
        {
            "product_id": 2,
            "product_name": "iPhone 15",
            "category": "Electronics"
        }
    ]