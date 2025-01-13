import pytest
import os
import logging
import ipaddress
import json
import json_schema_validation
import openc2

from helpers import load_json, load_files, send_raw_command

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
command_path_good = "openc2-json-schema/tests/commands/good"
command_path_bad = "openc2-json-schema/tests/commands/bad"


def test_decoding():
	""" Test 'good' commands can be successfully decoded by lycam """
	for cmd in load_json(command_path_good):
		print("Command json: ", cmd)
		c = openc2.parse(cmd)
		print(type(c))
#print("Decoded as: ", c)
		bar=json.loads(c.serialize())
		print(type(bar))
		print("Re-encoded as: ", bar)
		

test_decoding()
