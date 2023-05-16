from pathlib import Path
import face_recognition
import shutil
import numpy
from typing import Any


class BasePicture:
    def __init__(self, original_path: Path, image: numpy.ndarray = numpy.ndarray(0)) -> None:
        self._original_path = original_path
        self._locations: list[tuple[int, Any, Any, int]] = []
        self._encodings: list[numpy.ndarray] = []
        self._image = image if image.any() else self._load_image()

    def _load_image(self) -> numpy.ndarray:
        img = face_recognition.load_image_file(self._original_path)
        return img

    def face_locations(self) -> None:
        self._locations = face_recognition.face_locations(self._image)

    def face_encodings(self) -> None:
        self._encodings = face_recognition.face_encodings(self._image, self._locations)

    @property
    def locations(self) -> list:
        return self._locations

    @property
    def encodings(self):
        return self._encodings

    @staticmethod
    def is_picture(file: Path) -> bool:
        if ".jpg" in file.suffix.lower():
            return True
        else:
            return False


class KnownPicture(BasePicture):
    def __init__(self, person_name: str, original_path: Path) -> None:
        super().__init__(original_path=original_path)
        self._person_name = person_name

    @property
    def person_name(self):
        return self._person_name


class Picture(BasePicture):
    def __init__(self, original_path: Path, image: numpy.ndarray = numpy.ndarray(0)) -> None:
        super().__init__(original_path=original_path, image=image)
        self._compared_results: list[KnownPicture] = []

    def compare_face(self, known_picture: KnownPicture):
        for encoding in self._encodings:
            result = face_recognition.compare_faces(known_picture.encodings, encoding)
            if result[0]:
                self._compared_results.append(known_picture)

    def copy_picture(self, destination: Path):
        for known_picture in self._compared_results:
            dst_path = Path.joinpath(destination, f"{known_picture.person_name}_picture")
            dst_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(self._original_path, dst_path)
