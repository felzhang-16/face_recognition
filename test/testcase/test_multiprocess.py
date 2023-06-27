import eel
from pathlib import Path
import os

from face_time.src.ui import start_recognition
from common.config import KNOWN_PERSION_1, SOURCEDIR


# mock eel attribute since eel does not start in pytest
def setRecognizingComplete(any):
    pass


def putMessageInOutput(any):
    pass


eel.setRecognizingComplete = setRecognizingComplete
eel.putMessageInOutput = putMessageInOutput
# end of mock


def test_face_recognition_multiprocess(valid_destination_path):
    configuration = {"sourceDir": SOURCEDIR, "destinationDir": valid_destination_path, "compare": KNOWN_PERSION_1}

    # add this logger handler if need log print
    # import logging
    # from face_time.src.logger import Logger
    # handler = logging.StreamHandler()
    # Logger.addHandler(handler)

    start_recognition(configuration)

    pictures_path = Path.joinpath(configuration["destinationDir"], f"{configuration['compare']['name']}_picture")
    assert pictures_path.is_dir() is True
    assert len(os.listdir(pictures_path)) == 3
