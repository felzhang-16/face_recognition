import os
from pathlib import Path
import face_recognition
import shutil
import numpy


class BasePicture():
    def __init__(self, origin_path=None, image=numpy.ndarray(0)) -> None:
        self._origin_path = origin_path
        self._locations = []
        self._encodings = []
        self._image = image if image.any() else self._load_image()

    def _load_image(self):
        img = face_recognition.load_image_file(self._origin_path)
        return img

    def face_locations(self):
        self._locations = face_recognition.face_locations(self._image)

    def face_encodings(self):
        self._encodings = face_recognition.face_encodings(self._image, self._locations)

    @property
    def locations(self):
        return self._locations

    @property
    def encodings(self):
        return self._encodings

    @staticmethod
    def is_picture(file):
        if '.jpg' in file.lower():
            return True
        else:
            return False


class Picture(BasePicture):
    def __init__(self, origin_path=None, image=numpy.ndarray(0)) -> None:
        super().__init__(origin_path=origin_path, image=image)
        self._compared_results = []

    def compare_face(self, known_picture):
        for encoding in self._encodings:
             result = face_recognition.compare_faces(known_picture.encodings, encoding, tolerance=0.3)
             if result[0]:
                 self._compared_results.append(known_picture)

    def copy_picture(self, destination):
        for known_picture in self._compared_results:
            path = os.path.join(destination, f'{known_picture.person_name}_picture')
            Path(path).mkdir(parents=True, exist_ok=True)
            shutil.copy(self._origin_path, path)


class KnownPicture(BasePicture):
    def __init__(self, origin_path, person_name) -> None:
        super().__init__(origin_path=origin_path)
        self._person_name = person_name

    @property
    def person_name(self):
        return self._person_name

    def face_encodings(self):
        super().face_encodings()
        if len(self._encodings) != 1:
            self._update_process_result('fail', f'one face should in KnownPicture, but have {len(self._encodings)}')

    def _validate_picture_quality(self):
        pass
