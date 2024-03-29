from face_time.src.processor import Picture, KnownPicture
from common.config import KNOWN_PERSION_1, PERSON_1


def test_face_recognition_is_correct():
    pic = Picture(PERSON_1)
    pic.face_locations()
    pic.face_encodings()
    assert pic._image.any(), "pic image should has content"
    assert len(pic.locations) == 1, "length of pic location should be 1"
    assert len(pic.encodings) == 1, "length of pic encodings should be 1"


def test_face_recognition_correct_with_known_picture():
    pic = KnownPicture(KNOWN_PERSION_1["name"], KNOWN_PERSION_1["image"])
    pic.face_locations()
    pic.face_encodings()
    assert pic.person_name == KNOWN_PERSION_1["name"]
    assert pic._image.any(), "pic image should has content"
    assert len(pic.locations) == 1, "length of pic location should be 1"
    assert len(pic.encodings) == 1, "length of pic encodings should be 1"


def test_face_compare_success():
    pic = Picture(PERSON_1)
    pic.face_locations()
    pic.face_encodings()

    known_pic = KnownPicture(KNOWN_PERSION_1["name"], KNOWN_PERSION_1["image"])
    known_pic.face_locations()
    known_pic.face_encodings()

    pic.compare_face(known_pic)
    assert pic._compared_results[0] == known_pic, "pic compare should success"
