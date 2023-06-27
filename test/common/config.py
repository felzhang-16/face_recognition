from pathlib import Path


PERSON_1 = Path.joinpath(Path.cwd(), "test", "data", "pics", "person_1.jpg")
KNOWN_PERSION_1 = {
    "name": "name_1",
    "image": Path.joinpath(Path.cwd(), "test", "data", "pics", "valid_pic.jpg"),
}

VALID_ORIGINAL_PATHS = [Path.joinpath(Path.cwd(), "test", "data", "original_path")]
INVALID_ORIGINAL_PATHS = [Path.joinpath(Path.cwd(), "test", "data", "invalid_path")]
NOT_EMPTY_PATH = [Path.joinpath(Path.cwd(), "test", "data", "invalid_destination_path")]
INVALID_DESTINATION_PATHS = [Path.joinpath(Path.cwd(), "test", "data", "invalid_destination_path")]
VALID_COMPARED = [
    {
        "name": "name_1",
        "image": Path.joinpath(Path.cwd(), "test", "data", "pics", "valid_pic.jpg"),
    }
]
INVALID_COMPARED = [
    {
        "name": "name_1",
        "image": Path.joinpath(Path.cwd(), "test", "data", "pics", "invalid_pic"),
    }
]
SOURCEDIR = Path.joinpath(Path.cwd(), "test", "data", "pics")
