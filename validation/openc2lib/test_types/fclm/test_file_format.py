import pytest
import parametrize_from_file
from openc2lib.profiles.fclm.data.file_format import FileFormat


@parametrize_from_file("parameters/test_file_format.yml", key="valid_formats")
def test_valid_file_formats(format_name, expected_value):
    file_format = FileFormat[format_name]
    assert file_format.name == format_name
    assert file_format.value == expected_value


@parametrize_from_file("parameters/test_file_format.yml", key="invalid_formats")
def test_invalid_file_formats(format_name):
    with pytest.raises(KeyError):
        FileFormat[format_name]
