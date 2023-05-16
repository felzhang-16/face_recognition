# -*- coding: utf-8 -*-
import pytest
from src.user_data import UserData
from pathlib import Path


valid_original_paths = [Path.joinpath(Path.cwd(), "test", "data", "original_path")]
invalid_original_paths = [Path.joinpath(Path.cwd(), "test", "data", "invalid_path")]
not_empty_path = [Path.joinpath(Path.cwd(), "test", "data", "invalid_destination_path")]

valid_destination_paths = [Path.joinpath(Path.cwd(), "test", "data", "destination_path")]
invalid_destination_paths = [Path.joinpath(Path.cwd(), "test", "data", "invalid_destination_path")]
valid_compared = [{"name": "name_1", "image": Path.joinpath(Path.cwd(), "test", "data", "pics", "valid_pic.jpg")}]
invalid_compared = [{"name": "name_1", "image": Path.joinpath(Path.cwd(), "test", "data", "pics", "invalid_pic")}]


@pytest.mark.parametrize("path", valid_original_paths)
def test_valid_path(path):
    assert UserData.is_path_valid(path) == True


@pytest.mark.parametrize("path", invalid_original_paths)
def test_invalid_path(path):
    assert UserData.is_path_valid(path) == False


@pytest.mark.parametrize("path", not_empty_path)
def test_not_empty_path(path):
    assert UserData.is_path_empty(path) == False


@pytest.mark.parametrize("path", valid_destination_paths)
def test_empty_path(path):
    assert UserData.is_path_empty(path) == True


@pytest.mark.parametrize("path", valid_original_paths)
def test_set_original_path_success(path):
    user_data = UserData()
    result = user_data.set_original_path(path)
    assert result == True
    assert user_data.original_path == path


@pytest.mark.parametrize("path", invalid_original_paths)
def test_set_original_path_fail(path):
    user_data = UserData()
    result = user_data.set_original_path(path)
    assert result == False
    assert user_data.original_path is None


@pytest.mark.parametrize("path", valid_destination_paths)
def test_set_destination_path_success(path):
    user_data = UserData()
    result = user_data.set_destination_path(path)
    assert result == True
    assert user_data.destination_path == path


@pytest.mark.parametrize("path", invalid_destination_paths)
def test_set_destination_path_fail(path):
    user_data = UserData()
    result = user_data.set_destination_path(path)
    assert result == False
    assert user_data.destination_path is None


@pytest.mark.parametrize("compared", valid_compared)
def test_set_compared_success(compared):
    user_data = UserData()
    result = user_data.set_compared(compared)
    assert result is True
    assert user_data.compared == {compared["name"]: compared["image"]}


@pytest.mark.parametrize("compared", invalid_compared)
def test_set_compared_fail(compared):
    user_data = UserData()
    result = user_data.set_compared(compared)
    assert result == False
    assert user_data.compared is None
