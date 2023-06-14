import os
from multiprocessing import Manager, managers, Pool, cpu_count, current_process
from pathlib import Path
import logging
from logging.handlers import QueueHandler
import queue
from typing import Any
from threading import Thread

import eel

from face_time.src.logger import Logger, logger_thread
from face_time.src.config import CONFIG_TYPE
from face_time.src.picture import Picture, KnownPicture
from face_time.src.video import Video
from face_time.src.user_data import UserData


VIDEOS = []
KNOWN_PICTURES = []


def set_user_data(configuration: CONFIG_TYPE) -> UserData:
    Logger.debug(f"{configuration}")
    user_data = UserData()
    user_data.set_original_path(configuration["sourceDir"])
    user_data.set_destination_path(configuration["destinationDir"])
    user_data.set_compared(configuration["compare"])
    return user_data


def collect_picture(original_pics: managers.ListProxy, pics_original_path: Path) -> None:
    Logger.debug(f"{pics_original_path}")
    for root, _, files in os.walk(pics_original_path):
        for file in files:
            file_path = Path.joinpath(Path(root), file)
            if Picture.is_picture(file_path):
                pic = Picture(original_path=file_path)
                original_pics.append(pic)


def handle_known_picture(compared: dict[str, list[Path]]) -> None:
    Logger.debug(f"{compared}")
    for name, paths in compared.items():
        for path in paths:
            pic = KnownPicture(name, path)
            pic.face_locations()
            pic.face_encodings()
            KNOWN_PICTURES.append(pic)


def handle_one_picture(
    pic: Picture,
    known_pics: list[KnownPicture],
    mp_done_pics: managers.ListProxy,
    pics_destination_path: Path,
    queue: queue.Queue[Any],
) -> None:
    # create logger for sub process, which name mush be "app"
    #     logger name is the same as main process logger
    Logger = logging.getLogger("app")
    Logger.addHandler(QueueHandler(queue))
    Logger.setLevel(logging.DEBUG)
    Logger.debug(f"{pic._original_path}")
    pic.face_locations()
    pic.face_encodings()
    for know_pic in known_pics:
        pic.compare_face(know_pic)
    pic.copy_picture(pics_destination_path)
    mp_done_pics.append(pic)


def handle_pictures_with_mp(
    mp_original_pics: managers.ListProxy, mp_done_pics: managers.ListProxy, pics_destination_path: Path, log_queue
) -> None:
    Logger.info("Main process start!")
    thread = Thread(target=logger_thread, args=(log_queue, eel.putMessageInOutput))
    thread.start()

    with Pool(cpu_count()) as pool:
        results = [
            pool.apply_async(
                handle_one_picture,
                args=(pic, KNOWN_PICTURES, mp_done_pics, pics_destination_path, log_queue),
            )
            for pic in mp_original_pics
        ]
        for result in results:
            result.wait()
        Logger.info("Main process done!")
        log_queue.put(None)
        pool.close()
        pool.join()
    thread.join()


def process_video():
    for root, _, files in os.walk(UserData.original_path):
        for file in files:
            file_path = os.path.join(root, file)
            if Video.is_video(file_path):
                VIDEOS.append(Video(original_path=file_path))

    for know_picture in KNOWN_PICTURES:
        for video in VIDEOS:
            with video as v:
                v.compare_face(know_picture)
                v.copy_video(UserData.destination_path)


def collect_and_process_pics(user_data: UserData) -> None:
    Logger.debug(f"{user_data}")
    handle_known_picture(user_data.compared)
    with Manager() as manager:
        log_queue = manager.Queue()
        mp_original_pics = manager.list()
        mp_done_pics = manager.list()
        collect_picture(mp_original_pics, user_data.original_path)
        handle_pictures_with_mp(mp_original_pics, mp_done_pics, user_data.destination_path, log_queue)
