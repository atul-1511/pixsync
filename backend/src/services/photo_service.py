from pathlib import Path
from typing import List, Dict

# adjust this to wherever you mount your photos in your container
PHOTO_DIR = Path(__file__).parent.parent.parent / "photos"

def load_photos(limit: int = 10) -> List[Dict]:
    """
    Scan PHOTO_DIR for up to `limit` image files and
    return a list of dicts with {id, url, filename}.
    """
    photos = []
    for idx, path in enumerate(sorted(PHOTO_DIR.iterdir())):
        if idx >= limit:
            break
        if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif"}:
            photos.append({
                "id": idx + 1,
                "url": f"/static/photos/{path.name}",
                "title": path.stem
            })
    return photos
