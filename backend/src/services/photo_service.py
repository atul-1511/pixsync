from pathlib import Path
from typing import List, Dict
import pathlib

from src.services.face_search import FaceSearch

class LoadPhotos:
    # just for url/title generation
    PHOTO_DIR = pathlib.Path('/Users/59423/Downloads/JPEG 02/')

    def __init__(self, index_path = 'src/database/faces.index', meta_db = 'src/database/faces.sqlite', top_k = 64, threshold = 0.33):
        # wrap your untouched FaceSearch
        self.face_search = FaceSearch(
            index_path=index_path,
            meta_db=meta_db,
            top_k=top_k,
            threshold=threshold
        )

    def search_and_load(self, query_img: str) -> List[Dict]:
        """
        1. Run FaceSearch.search(query_img) → list of image‐path strings
        2. Extract just the filename from each path
        3. Sort them (for consistent ordering)
        4. Build and return [{id, url, title}]
        """
        # 1) get the raw matches
        raw_matches = self.face_search.search(query_img)

        # 2) filenames only, dedup & sort
        filenames = sorted({ Path(p).name for p in raw_matches })

        # 3) map to load_photos style output
        return [
            {
                "id":   idx + 1,
                "url":  f"/static/photos/{fn}",
                "title": Path(fn).stem
            }
            for idx, fn in enumerate(filenames)
        ]
