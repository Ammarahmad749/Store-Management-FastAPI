from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.main import main_router

app = FastAPI(
    title="Store Management FastAPI",
    description="Store Management FastAPI.",
    version='v0.1.0',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(main_router)
