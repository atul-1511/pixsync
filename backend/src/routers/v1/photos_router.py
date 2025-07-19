from fastapi import APIRouter
from src.services.photo_service import LoadPhotos
import pathlib

router = APIRouter()

@router.get("/", summary="Get up to 10 photos")
async def get_photos():
    """
    Returns JSON:
    {
      "photos": [
        { "id": 1, "url": "/static/photos/foo.jpg", "title": "foo" },
        …
      ]
    }-
    """

    SELFIE_PATH = pathlib.Path('src/selfie.jpg') 

    load_photos = LoadPhotos()
    photos = load_photos.search_and_load(SELFIE_PATH)
    return {"photos": photos}
