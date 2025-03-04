from fastapi import FastAPI
from app.routers import category, products, auth


app = FastAPI()
#  uvicorn app.main:app --reload


@app.get('/')
async def welcome() -> dict:
    return {"message": "My e-commerce app"}

app.include_router(category.router)
app.include_router(products.router)
app.include_router(auth.router)
