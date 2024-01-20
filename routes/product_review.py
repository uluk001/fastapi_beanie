from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from services.product_review.product_review_schema import (
    ProductReviewCreate,
    ProductReviewUpdate,
    ProductReviewRead,
)
from services.product_review.product_review_crud import (
    create_product_review,
    get_all_product_reviews,
)


router = APIRouter()


@router.post("/", response_model=ProductReviewRead, status_code=201)
async def create_product_review_route(product_review: ProductReviewCreate) -> ProductReviewRead:
    return await create_product_review(product_review)


@router.get("/", response_model=List[ProductReviewRead])
async def get_all_product_reviews_route() -> List[ProductReviewRead]:
    return await get_all_product_reviews()
