from ast import arg
from bdb import set_trace
from multiprocessing import pool, Manager, cpu_count, Process
import time
import face_recognition
import pdb


class ClassA():
    def __init__(self, img) -> None:
        self._img = img
        self._done = 10


def generate_mg_list():
    MG_LIST = Manager().list()
    im5 = r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\chengzi\12_andr_good.jpg'
    for i in range(2):
        obj = ClassA(im5)
        print(f'==== id of obj is {id(obj)}')
        MG_LIST.append(obj)
    return MG_LIST


def multi_processors_pic(item):
    im_load = face_recognition.load_image_file(item._img)
    im_face_location = face_recognition.face_locations(im_load)
    im_face_encoding = face_recognition.face_encodings(im_load, im_face_location)
    item._done = 20
    # print(f'==== id of im is {id(item)}')


def func_multi_process_pool(mg_list):
    num_workers = cpu_count()
    the_pool = pool.Pool(num_workers)

    for i in mg_list:
        the_pool.apply_async(multi_processors_pic, args=(i,))
    the_pool.close()
    the_pool.join()
    return mg_list


# if __name__ == '__main__':
#     # t1 = time.time()
#     # mg_list = generate_mg_list()
#     # mg_list = func_multi_process_pool(mg_list)
#     # # pdb.set_trace()
#     # for item in mg_list:
#     #     print(f'==== id of item is {id(item)}')
#     # print(f'==== the end of time is {time.time()-t1}')
#     with Manager() as manager:
#         mg_list = manager.list()
#         im5 = r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\chengzi\12_andr_good.jpg'
#         for i in range(1):
#             obj = ClassA(im5)
#             print(f'==== id of obj is {id(obj)}')
#             mg_list.append(obj)
#         the_pool = pool.Pool(cpu_count())
#         for item in mg_list:
#             the_pool.apply_async(multi_processors_pic, args=(item, ))
#         the_pool.close()
#         the_pool.join()
#         for item in mg_list:
#             print(f'==== item._done is {item._done}')

class ClassA():
    def __init__(self, a) -> None:
        self.a = a
        self._done = None

def f1(l):
    l[0][0] = 1111
    print(f'==== l is {l}')


def f2(l):
    for i in range(20):
        print('==== item.a is ')
        for item in l:
            print(f'{item.a}+{item._done}', end=' ')
        print()
        time.sleep(2)

if __name__ == '__main__':
    l = Manager().list([[0,1], 1, 2])
    print(f'==== outside l is {l}')
    the_pool = pool.Pool(cpu_count())
    the_pool.apply_async(f1, args=(l,))
    # the_pool.apply_async(f2, args=(l,))
    the_pool.close()
    the_pool.join()
    print(f'==== outside l is {l}')
