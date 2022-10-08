import os
import time
from multiprocessing import pool, cpu_count

from src.picture import Picture, KnownPicture
from src.video import Video
from src.comm_def import user_data, KNOWN_PERSON
from src.comm_log import logger
import dearpygui.dearpygui as dpg


VIDEOS = []
KNOWN_PICTURES = []


def collect_picture(origin_pics):
    for root, _, files in os.walk(user_data.origin_path):
        for file in files:
            file_path = os.path.join(root, file)
            if Picture.is_picture(file_path):
                pic = Picture(origin_path=file_path)
                origin_pics.append(pic)


def handle_known_picture():
    logger.debug('handle_known_picture begin')
    for name, path in KNOWN_PERSON.items():
        if KnownPicture.is_picture(path):
            known = KnownPicture(path, name)
            known.face_locations()
            known.face_encodings()
            KNOWN_PICTURES.append(known)


def handle_one_picture(pic, known_pics, mp_done_pics):
    pic.face_locations()
    pic.face_encodings()
    for know_pic in known_pics:
        pic.compare_face(know_pic)
    pic.copy_picture(user_data.destination_path)
    mp_done_pics.append(pic)


def display_process_rate(mp_origin_pics, mp_done_pics):
    process_rate = 0.0
    while process_rate < 1.0:
        process_rate = len(mp_done_pics) / len(mp_origin_pics)
        print(f'progress is {process_rate}')
        dpg.set_value("progress", process_rate)
        time.sleep(5)


def process_pictures_with_mp(mp_origin_pics, mp_done_pics):
    mp_pool = pool.Pool(cpu_count())
    for pic in mp_origin_pics:
        mp_pool.apply_async(handle_one_picture, args=(pic, KNOWN_PICTURES, mp_done_pics))
    display_process_rate(mp_origin_pics, mp_done_pics)
    mp_pool.close()
    mp_pool.join()


def process_video():
    logger.debug('process_video begin')
    for root, _, files in os.walk(user_data.origin_path):
        for file in files:
            file_path = os.path.join(root, file)
            if Video.is_video(file_path):
                VIDEOS.append(Video(origin_path=file_path))

    for know_picture in KNOWN_PICTURES:
        for video in VIDEOS:
            with video as v:
                v.compare_face(know_picture)
                v.copy_video(user_data.destination_path)

    logger.debug('process_video end')


def main():
    handle_known_picture()
    collect_picture()


if __name__ == '__main__':
    time1 = time.time()
    main()
    print(f'==== spend time is {time.time() - time1}')
