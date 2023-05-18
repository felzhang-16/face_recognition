import face_time
from face_time.src.picture import Picture
import cv2
import os
from pathlib import Path
import shutil


class Video:
    def __init__(self, original_path) -> None:
        self._original_path = original_path
        self._compared_results: list = []

    def __enter__(self):
        self._video = cv2.VideoCapture(self._original_path)
        return self

    def __exit__(self, *args, **kwargs):
        self._video.release()
        cv2.destroyAllWindows()

    def compare_face(self, known_picture):
        while True:
            ret, frame = self._video.read()
            if not ret:
                break
            rgb_frame = frame[:, :, ::-1]
            pic = Picture(image=rgb_frame)
            for encoding in pic.encodings:
                result = face_time.compare_faces(known_picture.encodings, encoding, tolerance=0.4)
                if result[0]:
                    self._compared_results.append(known_picture)

    def copy_video(self, destination):
        for known_picture in self._compared_results:
            path = os.path.join(destination, f"{known_picture.person_name}_video")
            Path(path).mkdir(parents=True, exist_ok=True)
            shutil.copy(self._original_path, path)

    @staticmethod
    def is_video(file):
        if ".mp4" in file.lower():
            return True
        else:
            return False
