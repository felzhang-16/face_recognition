from face_time.src.ui import start_recognition
from common.config import PERSON_1, KNOWN_PERSION_1


def test_face_recognition_multiprocess(valid_destination_path):
    configuration = {"sourceDir": PERSON_1, "destinationDir": valid_destination_path, "compare": KNOWN_PERSION_1}
    start_recognition(configuration)
