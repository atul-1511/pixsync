import cv2
import numpy as np
from insightface.app import FaceAnalysis
import os


os.environ['INSIGHTFACE_HOME'] = '/models'

class FaceProcessor:
    def __init__(self, model_name='buffalo_l', device='CPUExecutionProvider', det_size=(640, 640)):
        """Initializes the FaceProcessor with an InsightFace model."""
        self.app = FaceAnalysis(name=model_name, providers=[device])
        self.app.prepare(ctx_id=-1, det_size=det_size)

    def extract_embeddings(self, img_path):
        """
        Detect faces in an image and return their 512‑D embeddings and bounding boxes.

        Parameters
        ----------
        img_path : str
            Path to the image on disk.

        Returns
        -------
        vecs : np.ndarray, shape=(n_faces, 512)
            L2‑normalized feature vectors.
        bboxes : list[list[int]]
            Each bbox is [x1, y1, x2, y2].
        """
        img = cv2.imread(img_path)
        if img is None:
            raise FileNotFoundError(f"Cannot load image: {img_path}")

        faces = self.app.get(img)
        vecs, bboxes = [], []

        for face in faces:
            vecs.append(face.normed_embedding)
            bboxes.append(face.bbox.astype(int).tolist())

        if vecs:
            return np.vstack(vecs).astype('float32'), bboxes
        return np.empty((0, 512), dtype='float32'), []
