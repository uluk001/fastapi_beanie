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
    get_product_review_by_id,
    update_product_review,
    delete_product_review,
)


router = APIRouter()


@router.post("/", response_model=ProductReviewRead, status_code=201)
async def create_product_review_route(product_review: ProductReviewCreate) -> ProductReviewRead:
    return await create_product_review(product_review)


@router.get("/", response_model=List[ProductReviewRead])
async def get_all_product_reviews_route() -> List[ProductReviewRead]:
    return await get_all_product_reviews()


@router.get("/{id}", response_model=ProductReviewRead)
async def get_product_review_by_id_route(id: PydanticObjectId) -> ProductReviewRead:
    product_review = await get_product_review_by_id(id)
    if not product_review:
        raise HTTPException(status_code=404, detail="Product Review not found")
    return product_review


@router.put("/{id}", response_model=ProductReviewRead)
async def update_product_review_route(
    id: PydanticObjectId, product_review_data: ProductReviewUpdate
) -> ProductReviewRead:
    product_review = await update_product_review(id, product_review_data)
    if not product_review:
        raise HTTPException(status_code=404, detail="Product Review not found")
    return product_review


@router.delete("/{id}", response_model=ProductReviewRead)
async def delete_product_review_route(id: PydanticObjectId) -> ProductReviewRead:
    product_review = await delete_product_review(id)
    if not product_review:
        raise HTTPException(status_code=404, detail="Product Review not found")
    return product_review
