# -*- coding: utf-8 -*-
import pytest
import sys
from importlib import reload
from user_data import UserData, ERROR_INVALID_PATH, ERROR_NOT_EMPTY_PATH, ERROR_INVALID_KNOWN_PERSON


valid_paths = [r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\chengzi',
               r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\destination']
invalid_paths = [r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\not_exist_path',
                 r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\test\testcase\test_comm_def.py',
                 r'C:\1_WorkSpace\这不是路径']
valid_for_destination_paths = [r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\test\data\destination_path']
invalid_for_destination_paths = [r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\test\data\invalid_destination_path']
valid_known_persons = [r'chengzi C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\chengzi\8_3.jpg C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\chengzi\2.jpg']
invalid_known_persons = [r'chengzi']


@pytest.mark.parametrize("valid_path", valid_paths)
def test_valid_path_success(valid_path):
    USER_DATA = UserData()
    assert USER_DATA.validate_path(valid_path) is None


@pytest.mark.parametrize("invalid_path", invalid_paths)
def test_valid_path_fail(invalid_path):
    USER_DATA = UserData()
    assert ERROR_INVALID_PATH == USER_DATA.validate_path(invalid_path)


@pytest.mark.parametrize("valid_path", valid_paths)
def test_set_original_path_success(valid_path):
    USER_DATA = UserData()
    result = USER_DATA.set_original_path(valid_path)
    assert result is None
    assert USER_DATA.original_path == valid_path


@pytest.mark.parametrize("invalid_path", invalid_paths)
def test_set_original_path_fail(invalid_path):
    USER_DATA = UserData()
    result = USER_DATA.set_original_path(invalid_path)
    assert result == ERROR_INVALID_PATH
    assert USER_DATA.original_path is None


@pytest.mark.parametrize("valid_path", valid_for_destination_paths)
def test_set_destination_path_success(valid_path):
    USER_DATA = UserData()
    result = USER_DATA.set_destination_path(valid_path)
    assert result is None
    assert USER_DATA.destination_path == valid_path


@pytest.mark.parametrize("invalid_path", invalid_for_destination_paths)
def test_set_destination_path_empty(invalid_path):
    USER_DATA = UserData()
    result = USER_DATA.set_destination_path(invalid_path)
    assert result == ERROR_NOT_EMPTY_PATH
    assert USER_DATA.destination_path is None


@pytest.mark.parametrize("invalid_path", invalid_paths)
def test_set_destination_path_invalid(invalid_path):
    USER_DATA = UserData()
    result = USER_DATA.set_destination_path(invalid_path)
    assert result == ERROR_INVALID_PATH
    assert USER_DATA.destination_path is None


@pytest.mark.parametrize("known_person", valid_known_persons)
def test_set_known_person_success(known_person):
    USER_DATA = UserData()
    result = USER_DATA.set_known_person(known_person)
    assert result is None
    assert USER_DATA.known_person == {'chengzi': [r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\chengzi\8_3.jpg', r'C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\data\chengzi\2.jpg']}


@pytest.mark.parametrize("known_person", invalid_known_persons)
def test_set_known_person_fail(known_person):
    USER_DATA = UserData()
    result = USER_DATA.set_known_person(known_person)
    assert result == ERROR_INVALID_KNOWN_PERSON
    assert USER_DATA.known_person is None
