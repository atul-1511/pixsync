from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# import the single v1_router
from src.routers.v1.v1_router import v1_router

app = FastAPI(title="pixsync API")

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="pixsync API")

# Add this before mounting routers/static files
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3031"],  # or ["*"] for all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# serve static images
app.mount(
    "/static/photos",
    StaticFiles(directory=Path(__file__).parent / "photos"),
    name="photos",
)

# now mount **all** v1 endpoints in one go
app.include_router(v1_router)
