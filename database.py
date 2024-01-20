from beanie import init_beanie
import motor.motor_asyncio
from config import APP_SETTINGS


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017/productreviews"
    )

    await init_beanie(database=APP_SETTINGS.DB_NAME, document_models=[])