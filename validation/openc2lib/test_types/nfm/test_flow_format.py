import pytest
from openc2lib.types.base import Enumerated
from openc2lib.profiles.nfm.data.flow_format import FlowFormat
import parametrize_from_file

@parametrize_from_file("parameters/test_flow_format.yml")
def test_flow_format(flow_format, expected_value, expected_repr, expected_str, invalid_value):
    # Valid FlowFormat test cases
    if expected_value is not None:
        assert FlowFormat[flow_format].value == expected_value  # Compare with the value of the enum

# Test that the FlowFormat class inherits from Enumerated
def test_inheritance():
    assert issubclass(FlowFormat, Enumerated)
