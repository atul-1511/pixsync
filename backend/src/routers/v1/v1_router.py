from fastapi import APIRouter

# import each versioned router
from src.routers.v1.photos_router import router as photos_router
# bundle them all under /v1
v1_router = APIRouter(prefix="/v1")

v1_router.include_router(photos_router, prefix="/photos", tags=["photos"])
