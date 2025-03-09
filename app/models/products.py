from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, Float
from sqlalchemy.orm import relationship

from .database import Base



class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)
    sale_price = Column(Float, default=0)
    original_price = Column(Float, default=0)
    is_available = Column(Boolean, default=False)
    category = Column(String, index=True, nullable=True)
    height = Column(Float, nullable=True)
    width = Column(Float, nullable=True)    
    length = Column(Float, nullable=True)
    description = Column(Text, nullable=True)
    slug = Column(String, index=True, nullable=True)
    quantity = Column(Integer, default=0)

    # Add this line to fix the error
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    bulbs = relationship("ProductBulb", back_populates="product", cascade="all, delete-orphan")

class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    image_url = Column(String, nullable=True)

    product = relationship("Product", back_populates="images")

    
class ProductBulb(Base):
    __tablename__ = "product_bulbs"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)
    free_with_product = Column(Boolean, default=False)
    is_available = Column(Boolean, default=False)
    image = Column(String, nullable=True)
    
    product = relationship("Product", back_populates="bulbs")
