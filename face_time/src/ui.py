import eel
import os

from face_time.src.config import FRONTEND_FOLDER, UIOpenMode
from face_time.src.logger import Logger, add_logger_handler, log_to_ui_output
from face_time.src.processor import set_user_data, collect_and_process_pics
from face_time.src import dialogs
from face_time.src.config import CONFIG_TYPE


eel.init(FRONTEND_FOLDER)


@eel.expose
def does_file_exist(file_path: str) -> bool:
    return os.path.isfile(file_path)


@eel.expose
def does_folder_exist(path: str) -> bool:
    return os.path.isdir(path)


@eel.expose
def does_folder_empty(path: str) -> bool:
    if os.path.isdir(path):
        if not os.listdir(path):
            return True
    return False


@eel.expose
def ask_folder() -> str | None:
    return dialogs.ask_folder()


@eel.expose
def ask_file(file_type) -> str | None:
    return dialogs.ask_file(file_type)


@eel.expose
def initialise() -> None:
    add_logger_handler(Logger, log_to_ui_output)


@eel.expose
def start_recognition(configuration: CONFIG_TYPE) -> None:
    Logger.info(" - ")
    Logger.info(f"源路径: {configuration['sourceDir']}")
    Logger.info(f"目标路径: {configuration['destinationDir']}")
    Logger.info(f"对照组: 姓名：{configuration['compare']['name']}, 照片：{configuration['compare']['image']}")
    user_data = set_user_data(configuration)
    if not all([user_data.original_path, user_data.destination_path, user_data.compared]):
        Logger.error("设置user_data失败, 结束程序")
        eel.setRecognizingComplete(False)
    else:
        Logger.info("运行程序")
        collect_and_process_pics(user_data)
        Logger.info("程序运行结束")
        eel.setRecognizingComplete(True)


def start_web_app(mode: UIOpenMode) -> None:
    try:
        eel.start("index.html", size=(650, 672), mode=mode.value)
    except (SystemExit, KeyboardInterrupt):
        pass


if __name__ == "__main__":
    start_web_app(UIOpenMode.CHROME)
