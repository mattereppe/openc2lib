import pytest
import parametrize_from_file
from openc2lib.profiles.nfm.data.iface_type import IfaceType  # update path if needed

@parametrize_from_file("parameters/test_iface_type.yml", key="valid_iface_types")
def test_valid_iface_types(name, expected_value):
    iface_type = IfaceType[name]
    assert iface_type.name == name
    assert iface_type.value == expected_value

@parametrize_from_file("parameters/test_iface_type.yml", key="invalid_iface_types")
def test_invalid_iface_types(name):
    with pytest.raises(KeyError):
        IfaceType[name]
