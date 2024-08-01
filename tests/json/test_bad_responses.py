import pytest
import os
import ipaddress
import json
import jsonschema
import json_schema_validation

from helpers import load_files
from openc2lib import Encoder, Response, StatusCode
import openc2lib.profiles.slpf
import openc2lib.transfers.http
import openc2lib.transfers.http.message as http
from openc2lib.encoders.json import JSONEncoder

import json_schema_validation

import acme
import mycompany
import mycompany_with_underscore
import example
import esm
import digits
import digits_and_chars


# Parameters to get good and bad samples of json messages
response_path_bad = "openc2-json-schema/tests/responses/bad"

@pytest.mark.skip(reason="Not relevant to the validation of openc2lib")
@pytest.mark.parametrize("frsp", load_files(response_path_bad) )
def test_base(frsp):
	print("file ", frsp)
	with open(frsp, 'r') as f:
		try:
			rsp = json.load(f) 
		except:
			assert True
			rsp = ''

	print("Command json: ", rsp)

	with pytest.raises(jsonschema.exceptions.ValidationError):
		json_schema_validation.validate_openc2(rsp, json_schema_validation.Validation.response, json_schema_validation.Validation.base)
		
@pytest.mark.skip(reason="Not relevant to the validation of openc2lib")
@pytest.mark.parametrize("frsp", load_files(response_path_bad) )
def test_contrib(frsp):
	print("file ", frsp)
	with open(frsp, 'r') as f:
		try:
			rsp = json.load(f) 
		except:
			assert True
			rsp = ''

	print("Command json: ", rsp)

	with pytest.raises(jsonschema.exceptions.ValidationError):
		json_schema_validation.validate_openc2(rsp, json_schema_validation.Validation.response, json_schema_validation.Validation.contrib)
		
