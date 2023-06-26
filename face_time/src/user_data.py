# -*- coding: utf-8 -*-
from typing import Optional

import os
from pathlib import Path

from face_time.src.logger import Logger
from face_time.src.picture import BasePicture


class UserData:
    def __init__(self) -> None:
        self._original_path: Optional[Path] = None
        self._destination_path: Optional[Path] = None
        self._compared: dict[str, list[Path]] | None = None

    @staticmethod
    def is_path_valid(path: str) -> bool:
        Logger.debug(f"{path}")
        if not os.path.isdir(path):
            Logger.info(f"NOT valid path - {path}")
            return False
        return True

    @staticmethod
    def is_path_empty(path: str) -> bool:
        Logger.debug(f"{path}")
        if os.path.isdir(path):
            with os.scandir(path) as iter:
                if any(iter):
                    Logger.info(f"path NOT empty - {path}")
                    return False
                return True
        else:
            Logger.info(f"path NOT empty - {path}")
            return False

    @property
    def original_path(self):
        return self._original_path

    def set_original_path(self, path: str) -> bool:
        Logger.debug(f"{path}")
        if not self.is_path_valid(path):
            Logger.error(f"NOT valid original path - {path}")
            return False
        else:
            self._original_path = Path(path)
            return True

    @property
    def destination_path(self):
        return self._destination_path

    def set_destination_path(self, path: str) -> bool:
        Logger.debug(f"{path}")
        if not self.is_path_valid(path) or not self.is_path_empty(path):
            Logger.error(f"NOT valid destination path - {path}")
            return False
        else:
            self._destination_path = Path(path)
            return True

    @property
    def compared(self):
        return self._compared

    def set_compared(self, compared: dict[str, str]) -> bool:
        Logger.debug(f"{compared}")
        if not BasePicture.is_picture(Path(compared["image"])):
            Logger.error("NOT valid compared")
            return False
        else:
            self._compared = {compared["name"]: [Path(compared["image"])]}
            return True


USER_DATA = UserData()
