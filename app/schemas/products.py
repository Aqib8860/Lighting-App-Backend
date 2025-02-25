from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    is_available: bool
    image: str
    category: str
    description: str


class ProductsList(BaseModel):
    id: int | None = None
    name: str | None = None
    price: float | None = None
    is_available: bool | None = None
    image: str | None = None
    category: str | None = None
    description: str | None = None


