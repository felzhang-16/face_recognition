import pytest
from pathlib import Path


@pytest.fixture
def valid_destination_path():
    _path = Path.joinpath(Path.cwd(), "test", "data", "destination_path")
    _path.mkdir(exist_ok=True)
    yield _path
    # clean destination path
