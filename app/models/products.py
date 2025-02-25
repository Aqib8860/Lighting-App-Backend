from sqlalchemy import Column, Integer, String, Boolean, Text
from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    is_available = Column(Boolean, default=False)
    image = Column(String)
    category = Column(String, index=True)
    description = Column(Text)


