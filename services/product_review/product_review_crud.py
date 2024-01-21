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


async def update_product_review(
    id: str, product_review_data: ProductReviewUpdate
) -> ProductReview:
    product_review = await ProductReview.get(id)

    # Update fields in product_review with values from product_review_data
    for field, value in product_review_data.dict().items():
        setattr(product_review, field, value)

    await product_review.save()
    return product_review


async def delete_product_review(id: str) -> ProductReview:
    product_review = await ProductReview.get(id)
    await product_review.delete()
    return product_review
