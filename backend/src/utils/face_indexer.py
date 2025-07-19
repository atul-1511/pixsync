import os
import sqlite3
import faiss
import numpy as np
import json
from pathlib import Path
from tqdm import tqdm
from src.utils.face_processor import FaceProcessor
# from faces import get_face_app, extract_embeddings

class FaceIndexer:
    def __init__(self, img_dir, index_path='src/database/faces.index', meta_db='src/database/faces.sqlite'):
        self.img_dir = Path(img_dir)
        if not self.img_dir.exists():
            raise ValueError(f"Image directory not found: {self.img_dir}")

        self.index_path = index_path
        self.meta_db = meta_db
        self.dim = 512
        self.app = FaceProcessor()
        self.index = faiss.IndexFlatIP(self.dim)

    def valid_image(self, fname):
        exts = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
        return Path(fname).suffix.lower() in exts

    def gather_image_paths(self):
        return [str(p) for p in self.img_dir.rglob('*') if p.is_file() and self.valid_image(p)]

    def setup_database(self):
        conn = sqlite3.connect(self.meta_db)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS faces (
                        id INTEGER PRIMARY KEY,
                        img_path TEXT NOT NULL,
                        bbox TEXT NOT NULL
                      )""")
        return conn, cur

    def index_faces(self):
        img_paths = self.gather_image_paths()
        print(f"Found {len(img_paths)} images")

        conn, cur = self.setup_database()
        face_id = 0

        for path in tqdm(img_paths, desc="Indexing"):
            vecs, bboxes = self.app.extract_embeddings(path)
            if len(vecs) == 0:
                continue
            self.index.add(vecs)
            for box in bboxes:
                cur.execute("INSERT INTO faces (id, img_path, bbox) VALUES (?,?,?)",
                            (face_id, path, json.dumps(box)))
                face_id += 1

        conn.commit()
        conn.close()

        faiss.write_index(self.index, self.index_path)
        print(f"Finished. Indexed {face_id} faces.")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Ingest images into Faiss + SQLite")
    parser.add_argument('--img_dir', required=True, help="Folder containing photos")
    parser.add_argument('--index_path', default='src/database/faces.index', help="Output Faiss index")
    parser.add_argument('--meta_db', default='src/database/faces.sqlite', help="SQLite metadata DB")
    args = parser.parse_args()

    indexer = FaceIndexer(args.img_dir, args.index_path, args.meta_db)
    indexer.index_faces()
