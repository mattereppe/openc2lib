import pytest
import parametrize_from_file
from openc2lib.profiles.nfm.data.ie import IE  # Update this import to the correct path

@parametrize_from_file("parameters/test_ie.yml")
def test_good_ie(good_ie):
    obj = IE(good_ie)
    assert isinstance(obj, IE)
    assert isinstance(obj, str)

@parametrize_from_file("parameters/test_ie.yml")
def test_bad_ie(bad_ie):
    with pytest.raises((TypeError, ValueError)):
        IE(bad_ie)
