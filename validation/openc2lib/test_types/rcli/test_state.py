import pytest
import parametrize_from_file
from openc2lib.profiles.rcli.data.state import State

# Test valid states, mapping from a YAML file
@parametrize_from_file("parameters/test_state.yml", key="valid_states")
def test_valid_state(state_name, expected_value):
    state = State[state_name]  # Access the Enum using the state name
    assert state.name == state_name
    assert state.value == expected_value

# Test invalid states, expecting a ValueError when an invalid state is accessed
@parametrize_from_file("parameters/test_state.yml", key="invalid_states")
def test_invalid_state(state_name):
    with pytest.raises(KeyError):
        State[state_name]  # This should raise a KeyError for invalid states

