import uvicorn
from fastapi import FastAPI

from models.database import Base, engine
from models.user import User
from models.products import Product

from routers.user import router as user_router
from routers.products import router as product_router

from starlette_admin.contrib.sqla import Admin, ModelView

app = FastAPI()
# Create all tables
Base.metadata.create_all(bind=engine)

admin = Admin(engine, title="ASHRAFI LIGHTS")

admin.add_view(ModelView(User))
admin.add_view(ModelView(Product))

admin.mount_to(app)

app.include_router(user_router)
app.include_router(product_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)

