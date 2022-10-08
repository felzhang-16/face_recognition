from src.processor import Picture, KnownPicture


CHENGZI_FACE_1 = r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\test\data\2.jpg'
CHENGZI_FACE_2 = r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\test\data\8_3.jpg'
KNOWN_PIC_CHENGZI = {'chengzi': r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\chengzi\8_3.jpg'}
DEST_PATH = r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\test\data\destination'


def test_face_recognition_is_correct():
    pic = Picture(CHENGZI_FACE_1)
    pic.face_locations()
    pic.face_encodings()
    assert pic._image.any(), 'pic image should has content'
    assert len(pic.locations) == 1, 'length of pic location should be 1'
    assert len(pic.encodings) == 1, 'length of pic encodings should be 1'


def test_face_recognition_correct_with_known_picture():
    pic = KnownPicture(KNOWN_PIC_CHENGZI['chengzi'], 'chengzi')
    pic.face_locations()
    pic.face_encodings()
    assert pic.person_name == 'chengzi'
    assert pic._image.any(), 'pic image should has content'
    assert len(pic.locations) == 1, 'length of pic location should be 1'
    assert len(pic.encodings) == 1, 'length of pic encodings should be 1'


def test_face_compare_success():
    pic = Picture(CHENGZI_FACE_1)
    pic.face_locations()
    pic.face_encodings()

    known_pic = KnownPicture(KNOWN_PIC_CHENGZI['chengzi'], 'chengzi')
    known_pic.face_locations()
    known_pic.face_encodings()

    pic.compare_face(known_pic)
    assert pic._compared_results[0] == known_pic, 'pic compare should success'
