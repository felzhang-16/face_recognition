# ORIGIN_PATH = r'/mnt/c/1_WorkSpace/4_Tmp_for_myself/face_recognition/data/chengzi'
# DESTINATION_PATH = r'/mnt/c/1_WorkSpace/4_Tmp_for_myself/face_recognition/data/destination'
# KNOWN_PERSON = {'chengzi': r'/mnt/c/1_WorkSpace/4_Tmp_for_myself/face_recognition/data/chengzi/8_3.jpg',
#                 'wanwan': r'/mnt/c/1_WorkSpace/4_Tmp_for_myself/face_recognition/data/wanwan/7_andr_good.jpg'}

ORIGIN_PATH = r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\chengzi'
DESTINATION_PATH = r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\destination'
KNOWN_PERSON = {'chengzi': r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\chengzi\8_3.jpg'}
                # 'wanwan': r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\wanwan\7_andr_good.jpg'}


class UserData():
    def __init__(self) -> None:
        self._origin_path = None
        self._destination_path = None

    @property
    def origin_path(self):
        return self._origin_path

    @origin_path.setter
    def origin_path(self, value):
        self._origin_path = value

    @property
    def destination_path(self):
        return self._destination_path

    @destination_path.setter
    def destination_path(self, value):
        self._destination_path = value

    def validate(self):
        # validate if self._origin_path and self._destination_path is valid
        pass


user_data = UserData()
