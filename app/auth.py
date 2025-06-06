from starlette.requests import Request
from starlette_admin.auth import AdminUser, AuthProvider
from passlib.context import CryptContext
import os

# Dummy admin credentials (replace with DB user or env var in production)
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "$2b$12$aTestHash")  # hashed 'admin123'

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# To hash a real password (run this once in Python):
# from passlib.context import CryptContext
# print(CryptContext(schemes=["bcrypt"]).hash("backend-admin@9354"))


from starlette_admin.auth import AuthProvider

class MyAuthProvider(AuthProvider):
    async def login(self, request, username, password, form, config, **kwargs):
        if username == "admin" and password == "backend-admin":
            request.session["user"] = username
            return True
        return False

    async def logout(self, request):
        request.session.clear()
        return True

    async def get_user(self, request):
        return request.session.get("user")
    
    