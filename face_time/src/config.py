import pathlib
from enum import Enum
from typing import TypedDict

class UIOpenMode(Enum):
    NONE = None
    CHROME = "chrome"
    USER_DEFAULT = "user_default"


FRONTEND_FOLDER = pathlib.Path.joinpath(pathlib.Path(__file__).parent.parent, "web")


CONFIG_TYPE = TypedDict("CONFIG_TYPE", {"sourceDir": str, "destinationDir": str, "compare": dict[str, str]})
