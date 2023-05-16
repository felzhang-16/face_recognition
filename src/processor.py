import os
from multiprocessing import Manager, managers, pool, cpu_count
from pathlib import Path

from src.config import CONFIG_TYPE
from src.picture import Picture, KnownPicture
from src.video import Video
from src.user_data import UserData


VIDEOS = []
KNOWN_PICTURES = []


def set_user_data(configuration: CONFIG_TYPE) -> UserData:
    user_data = UserData()
    user_data.set_original_path(configuration["sourceDir"])
    user_data.set_destination_path(configuration["destinationDir"])
    user_data.set_known_person(configuration["compare"])
    return user_data


def collect_picture(original_pics: managers.ListProxy, pics_original_path: Path) -> None:
    for root, _, files in os.walk(pics_original_path):
        for file in files:
            file_path = Path.joinpath(Path(root), file)
            if Picture.is_picture(file_path):
                pic = Picture(original_path=file_path)
                original_pics.append(pic)


def handle_known_picture(known_person: dict[str, list[Path]]) -> None:
    for name, paths in known_person.items():
        for path in paths:
            pic = KnownPicture(name, path)
            pic.face_locations()
            pic.face_encodings()
            KNOWN_PICTURES.append(pic)


def handle_one_picture(
    pic: Picture, known_pics: list[KnownPicture], mp_done_pics: managers.ListProxy, pics_destination_path: Path
) -> None:
    pic.face_locations()
    pic.face_encodings()
    for know_pic in known_pics:
        pic.compare_face(know_pic)
    pic.copy_picture(pics_destination_path)
    mp_done_pics.append(pic)


def handle_pictures_with_mp(
    mp_original_pics: managers.ListProxy, mp_done_pics: managers.ListProxy, pics_destination_path: Path
) -> None:
    mp_pool = pool.Pool(cpu_count())
    for pic in mp_original_pics:
        mp_pool.apply_async(handle_one_picture, args=(pic, KNOWN_PICTURES, mp_done_pics, pics_destination_path))
    mp_pool.close()
    mp_pool.join()


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
    with Manager() as manager:
        mp_original_pics = manager.list()
        mp_done_pics = manager.list()
        handle_known_picture(user_data.known_person)
        collect_picture(mp_original_pics, user_data.original_path)
        handle_pictures_with_mp(mp_original_pics, mp_done_pics, user_data.destination_path)
