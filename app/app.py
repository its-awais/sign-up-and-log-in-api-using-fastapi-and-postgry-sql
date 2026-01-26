from fastapi import FastAPI
from app.Router.auth import router
from app.core.core import lifespan

app = FastAPI(lifespan=lifespan);
app.include_router(router)

