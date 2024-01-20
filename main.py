from fastapi import FastAPI
from database import init_db
from routes import product_review


app = FastAPI()
app.include_router(product_review.router, tags=["Product Review"], prefix="/product_review")


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}