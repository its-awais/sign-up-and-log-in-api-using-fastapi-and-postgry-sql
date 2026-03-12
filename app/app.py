from fastapi import FastAPI
from app.Router.auth import router as signup_router
from app.Router.logIn import router as login_router
from app.Router.admin import router as admin_router
from app.core.core import lifespan

app = FastAPI(lifespan=lifespan);
app.include_router(signup_router)
app.include_router(login_router)
app.include_router(admin_router)
