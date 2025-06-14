import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from models.database import engine
from models.users import User
from models.products import Product, ProductImage

from routers.users import router as user_router
from routers.products import router as product_router

# from starlette_admin.contrib.sqla import Admin, ModelView
from logging_config import setup_logging


setup_logging()

app = FastAPI(root_path="/backend")

allowed_origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # max_age=600 # for cache
)

allowed_host = ["localhost", "127.0.0.1", "13.204.87.41", "ashrafilights.aiworld.solutions"]

app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_host)


# admin = Admin(engine, title="AL QUDSIYAH")

# admin.add_view(ModelView(User))
# admin.add_view(ModelView(Product))
# admin.add_view(ModelView(ProductImage))

# admin.mount_to(app)

app.include_router(user_router)
app.include_router(product_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)

