import pytest
from pathlib import Path
import shutil


@pytest.fixture
def valid_destination_path():
    path = Path.joinpath(Path.cwd(), "test", "data", "destination_path")
    path.mkdir(exist_ok=True)
    yield path
    shutil.rmtree(path)
