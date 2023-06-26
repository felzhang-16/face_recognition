# -*- coding: utf-8 -*-
import pytest

from face_time.src.user_data import UserData
from common.config import (
    VALID_ORIGINAL_PATHS,
    INVALID_ORIGINAL_PATHS,
    NOT_EMPTY_PATH,
    INVALID_DESTINATION_PATHS,
    INVALID_COMPARED,
    VALID_COMPARED,
)


@pytest.mark.parametrize("path", VALID_ORIGINAL_PATHS)
def test_valid_path(path):
    assert UserData.is_path_valid(path) is True


@pytest.mark.parametrize("path", INVALID_ORIGINAL_PATHS)
def test_invalid_path(path):
    assert UserData.is_path_valid(path) is False


@pytest.mark.parametrize("path", NOT_EMPTY_PATH)
def test_not_empty_path(path):
    assert UserData.is_path_empty(path) is False


def test_empty_path(valid_destination_path):
    assert UserData.is_path_empty(valid_destination_path) is True


@pytest.mark.parametrize("path", VALID_ORIGINAL_PATHS)
def test_set_original_path_success(path):
    user_data = UserData()
    result = user_data.set_original_path(path)
    assert result is True
    assert user_data.original_path == path


@pytest.mark.parametrize("path", INVALID_ORIGINAL_PATHS)
def test_set_original_path_fail(path):
    user_data = UserData()
    result = user_data.set_original_path(path)
    assert result is False
    assert user_data.original_path is None


def test_set_destination_path_success(valid_destination_path):
    user_data = UserData()
    result = user_data.set_destination_path(valid_destination_path)
    assert result is True
    assert user_data.destination_path == valid_destination_path


@pytest.mark.parametrize("path", INVALID_DESTINATION_PATHS)
def test_set_destination_path_fail(path):
    user_data = UserData()
    result = user_data.set_destination_path(path)
    assert result is False
    assert user_data.destination_path is None


@pytest.mark.parametrize("compared", VALID_COMPARED)
def test_set_compared_success(compared):
    user_data = UserData()
    result = user_data.set_compared(compared)
    assert result is True
    assert user_data.compared == {compared["name"]: [compared["image"]]}


@pytest.mark.parametrize("compared", INVALID_COMPARED)
def test_set_compared_fail(compared):
    user_data = UserData()
    result = user_data.set_compared(compared)
    assert result is False
    assert user_data.compared is None
