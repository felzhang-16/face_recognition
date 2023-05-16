# -*- coding: utf-8 -*-
import os
from pathlib import Path
from src.logger import Logger
from src.picture import BasePicture


class UserData:
    def __init__(self) -> None:
        self._original_path: Path | None = None
        self._destination_path: Path | None = None
        self._compared: dict[str, list[Path]] | None = None

    @staticmethod
    def is_path_valid(path: str) -> bool:
        if not os.path.isdir(path):
            return False
        return True

    @staticmethod
    def is_path_empty(path: str) -> bool:
        if os.path.isdir(path):
            with os.scandir(path) as iter:
                if any(iter):
                    return False
                return True
        else:
            return False

    @property
    def original_path(self):
        return self._original_path

    def set_original_path(self, path: str) -> bool:
        if not self.is_path_valid(path):
            Logger.error("源路径非法，请重新输入")
            return False
        else:
            self._original_path = Path(path)
            return True

    @property
    def destination_path(self):
        return self._destination_path

    def set_destination_path(self, path: str) -> bool:
        if not self.is_path_valid(path) or not self.is_path_empty(path):
            Logger.error("目标路径非法或不为空，请重新输入")
            return False
        else:
            self._destination_path = Path(path)
            return True

    @property
    def compared(self):
        return self._compared

    def set_compared(self, compared: dict[str, str]) -> bool:
        if not BasePicture.is_picture(Path(compared["image"])):
            Logger.error("对照组非法，请重新输入")
            return False
        else:
            self._compared = {compared["name"]: Path(compared["image"])}
            return True


USER_DATA = UserData()
