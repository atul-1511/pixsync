import faiss
import sqlite3
import json
from pathlib import Path
from src.utils.face_processor import FaceProcessor

class FaceSearch:
    def __init__(self, index_path='src/database/faces.index', meta_db='src/database/faces.sqlite', top_k=64, threshold=0.33):
        self.index_path = Path(index_path)
        self.meta_db = Path(meta_db)
        self.top_k = top_k
        self.threshold = threshold
        self.index = faiss.read_index(str(self.index_path))
        self.conn = sqlite3.connect(self.meta_db)
        self.cur = self.conn.cursor()
        self.app = FaceProcessor()

    def search(self, query_img):
        vecs, _ = self.app.extract_embeddings(query_img)
        if vecs.shape[0] == 0:
            print("No faces found in query image.")
            return []

        sims, ids = self.index.search(vecs, self.top_k)
        matches = set()

        for sim_row, id_row in zip(sims, ids):
            for sim, idx in zip(sim_row, id_row):
                if idx == -1 or sim < self.threshold:
                    continue
                self.cur.execute("SELECT img_path FROM faces WHERE id=?", (int(idx),))
                row = self.cur.fetchone()
                if row:
                    matches.add(row[0])
        return sorted(matches)

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Search for a person in images")
    parser.add_argument('--index_path', default='faces.index')
    parser.add_argument('--meta_db', default='faces.sqlite')
    parser.add_argument('--query_img', required=True, help="Selfie / query image path")
    parser.add_argument('--top_k', type=int, default=64)
    parser.add_argument('--threshold', type=float, default=0.33)
    args = parser.parse_args()

    searcher = FaceSearch(
        index_path=args.index_path,
        meta_db=args.meta_db,
        top_k=args.top_k,
        threshold=args.threshold
    )
    result = searcher.search(args.query_img)
    print(f"Found {len(result)} matching images")
    for p in result:
        print(p)
    searcher.close()
