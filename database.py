from beanie import init_beanie
import motor.motor_asyncio
from config import APP_SETTINGS
from models.product_review import ProductReview


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        APP_SETTINGS.MONGO_DB,
        uuidRepresentation="standard",
    )

    db = client[APP_SETTINGS.DB_NAME]

    await init_beanie(database=db, document_models=[
        ProductReview,
    ])