from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from beanie import PydanticObjectId


class ProductReviewBase(BaseModel):
    name: str
    product: str
    rating: float
    review: str


class ProductReviewCreate(ProductReviewBase):
    pass


class ProductReviewUpdate(ProductReviewBase):
    pass


class ProductReviewRead(ProductReviewBase):
    id: PydanticObjectId
    date: datetime

    class Config:
        orm_mode = True
