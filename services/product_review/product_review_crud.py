from .product_review_schema import (
    ProductReviewCreate,
    ProductReviewUpdate,
    ProductReviewRead,
)
from models.product_review import ProductReview


async def get_all_product_reviews() -> list[ProductReview]:
    return await ProductReview.all().to_list()


async def get_product_review_by_id(id: str) -> ProductReview:
    return await ProductReview.get(id)


async def create_product_review(product_review: ProductReviewCreate) -> ProductReview:
    product_review = ProductReview(**product_review.model_dump())
    await product_review.insert()
    return product_review
