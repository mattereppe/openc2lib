import pytest
import parametrize_from_file
from openc2lib.profiles.nfm.data.export_options import ExportOptions
from openc2lib.profiles.nfm.data.flow_format import FlowFormat  # Using the correct FlowFormat

@parametrize_from_file("parameters/test_export_options.yml")
def test_good_export_options(sampling, aggregate, buffer, timeout, format):
    # Convert format string to corresponding FlowFormat enum value
    flow_format = FlowFormat[format.lower()] if format.lower() in FlowFormat.__members__ else None
    
    # Create the ExportOptions object with provided valid parameters
    obj = ExportOptions(sampling=sampling, aggregate=aggregate, buffer=buffer, timeout=timeout, format=flow_format)
    
    # Assert the object is of type ExportOptions
    assert isinstance(obj, ExportOptions)

@parametrize_from_file("parameters/test_export_options.yml")
def test_bad_export_options(bad_sampling, bad_aggregate, bad_buffer, bad_timeout, bad_format):
    # Handling bad input transformations
    with pytest.raises(Exception):
        # Convert bad format string to corresponding FlowFormat enum value
        bad_flow_format = FlowFormat[bad_format.lower()] if bad_format.lower() in FlowFormat.__members__ else None
        
        # Attempt to create an ExportOptions object with possibly incorrect inputs
        ExportOptions(sampling=bad_sampling, aggregate=bad_aggregate, buffer=bad_buffer, timeout=bad_timeout, format=bad_flow_format)
