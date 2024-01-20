from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ProductReviewBase(BaseModel):
    name: str
    product: str
    rating: float
    review: str


class ProductReviewCreate(ProductReviewBase):
    pass


class ProductReviewUpdate(ProductReviewBase):
    pass
