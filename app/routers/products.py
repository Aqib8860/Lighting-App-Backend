from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.database import SessionLocal
from schemas.products import ProductCreate, ProductsList
from crud.products import create_product, get_all_products

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/product/")
async def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return await create_product(db=db, product=product)


@router.get("/products-list/", response_model=list[ProductsList])
async def get_products_list(db: Session = Depends(get_db)):
    return await get_all_products(db=db)
