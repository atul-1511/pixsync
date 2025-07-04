from fastapi import APIRouter
from src.services.photo_service import load_photos

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
    }
    """
    photos = load_photos(limit=10)
    return {"photos": photos}
