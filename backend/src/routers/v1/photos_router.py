from fastapi import APIRouter, UploadFile, File, HTTPException
from src.services.photo_service import LoadPhotos
import pathlib
import shutil
import tempfile

router = APIRouter()

@router.post("/", summary="Upload a selfie to get your photos")
async def upload_selfie(file: UploadFile = File(...)):
    """
    Accepts an uploaded image file, runs face search, and returns matching photos.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")

    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=pathlib.Path(file.filename).suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = pathlib.Path(tmp.name)

    try:
        load_photos = LoadPhotos()
        photos = load_photos.search_and_load(str(tmp_path))
    finally:
        tmp_path.unlink(missing_ok=True)  # Clean up temp file

    return {"photos": photos}
