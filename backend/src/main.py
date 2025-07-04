from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# import the single v1_router
from backend.src.routers.v1.v1_router import v1_router

app = FastAPI(title="pixsync API")

# serve static images
app.mount(
    "/static/photos",
    StaticFiles(directory=Path(__file__).parent.parent / "photos"),
    name="photos",
)

# now mount **all** v1 endpoints in one go
app.include_router(v1_router)
