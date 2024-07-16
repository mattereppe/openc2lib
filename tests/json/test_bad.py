import pytest
import logging
import json

import json_schema_validation
from commands import load_files


# Parameters to get good and bad samples of json messages
command_path_bad = "openc2-json-schema/tests/commands/bad"
@pytest.mark.parametrize("fcmd", load_files(command_path_bad) )
def test_encoding(fcmd):
	print("file ", fcmd)
	with open(fcmd, 'r') as f:
		try:
			cmd = json.load(f) 
		except:
			assert False

	print("Command json: ", cmd)

	with pytest.raises(Exception):
		json_schema_validation.validate_openc2(cmd, json_schema_validation.Validation.command, json_schema_validation.Validation.base)
		json_schema_validation.validate_openc2(cmd, json_schema_validation.Validation.command, json_schema_validation.Validation.contrib)
		
