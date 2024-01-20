from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional


class ProductReview(Document):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = "product_review"
