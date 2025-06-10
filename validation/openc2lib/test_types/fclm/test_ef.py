import pytest
import parametrize_from_file
from openc2lib.profiles.fclm.data.ef import EF  # Update this import to the correct path

@parametrize_from_file("parameters/test_ef.yml")
def test_good_ef(good_ef):
    obj = EF(good_ef)
    assert isinstance(obj, EF)
    assert isinstance(obj, str)

@parametrize_from_file("parameters/test_ef.yml")
def test_bad_ef(bad_ef):
    with pytest.raises((TypeError, ValueError)):
        EF(bad_ef)
