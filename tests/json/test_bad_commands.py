import pytest
import logging
import json
import jsonschema

import json_schema_validation

from helpers import load_files


# Parameters to get good and bad samples of json messages
command_path_bad = "openc2-json-schema/tests/commands/bad"
@pytest.mark.skip(reason="Not relevant to the validation of openc2lib")
@pytest.mark.parametrize("fcmd", load_files(command_path_bad) )
def test_schema_base(fcmd):
	""" Test if json encodings is a valid schema """
	print("file ", fcmd)
	with open(fcmd, 'r') as f:
		try:
			cmd = json.load(f) 
		except:
			assert True
			cmd = ''

	print("Command json: ", cmd)

	with pytest.raises(jsonschema.exceptions.ValidationError):
		json_schema_validation.validate_openc2(cmd, json_schema_validation.Validation.command, json_schema_validation.Validation.base)
		
@pytest.mark.skip(reason="Not relevant to the validation of openc2lib")
@pytest.mark.parametrize("fcmd", load_files(command_path_bad) )
def test_schema_contrib(fcmd):
	""" Test if json encodings is a valid schema """
	print("file ", fcmd)
	with open(fcmd, 'r') as f:
		try:
			cmd = json.load(f) 
		except:
			assert True
			cmd = ''

	print("Command json: ", cmd)

	with pytest.raises(jsonschema.exceptions.ValidationError):
		json_schema_validation.validate_openc2(cmd, json_schema_validation.Validation.command, json_schema_validation.Validation.contrib)
		
