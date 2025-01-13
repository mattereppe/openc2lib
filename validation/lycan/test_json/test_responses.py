import pytest
import os
import ipaddress
import json
import json_schema_validation
import openc2

from helpers import load_json, load_files

import sys
sys.path.insert(0, "../profiles/")

import acme
import mycompany
import mycompany_with_underscore
import example
import esm
import digits
import digits_and_chars


# Parameters to get good and bad samples of json messages
response_path_good = "../../openc2-json-schema/tests/responses/good"
response_path_bad = "../../openc2-json-schema/tests/responses/bad"

# WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING 
# 
# The response in good/query_features_all.json does not conform to the definition 3.4.2.17 Version
# that says the Version is Major.Minor version number. This file uses: "1.0-draft-2019-02". 
# I removed the trailing "-draft-2019-02" e put the original file in the bad examples.


@pytest.mark.parametrize("rsp", load_json(response_path_good) )
@pytest.mark.dependency(name="test_decoding")
def test_decoding(rsp):
	print("Response json: ", rsp)
	c = openc2.parse(rsp)
	assert type(c) == openc2.v10.Response

@pytest.mark.parametrize("rsp", load_json(response_path_good) )
@pytest.mark.dependency(name="test_encoding", depends=["test_decoding"])
def test_encoding(rsp):
	print("Response json: ", rsp)
	oc2_rsp = openc2.parse(rsp)

	bar = json.loads(oc2_rsp.serialize())
	print("Re-encoded Command json: ", bar)

	assert rsp == bar

@pytest.mark.parametrize("rsp_file", load_files(response_path_bad) )
def test_decoding_invalid(rsp_file):
	""" Check invalid commands raise exceptions when decoded """
	print("Response file: ", rsp_file)
	# It may also raises while loading the files, since they may be empty
	with open(rsp_file, 'r') as frsp:
		# There is one empty file that raises this exception
		try:
			rsp = json.load(frsp) 
		except json.decoder.JSONDecodeError:
			rsp = ""

		print("Response json: ", rsp)
		with pytest.raises( Exception ):
			print("Response json: ", rsp)
			openc2.parse(rsp)
		

