from sqlalchemy.orm import Session
from models.products import Product
from schemas.products import ProductCreate


async def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name, price=product.price,
        is_available=product.is_available,
        image=product.image,
        category=product.category,
        description=product.description
    )
    
    db.add(db_product)    
    db.commit()
    db.refresh(db_product)
    
    return db_product

async def get_all_products(db: Session):
    return db.query(Product).all()

