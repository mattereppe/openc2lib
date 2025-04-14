import logging
import pytest
import os
import ipaddress
import json
import json_schema_validation

from helpers import load_json, load_files
from otupy import Encoder, Response, StatusCode, Command, Producer
import otupy.profiles.slpf
from otupy.transfers.http import HTTPTransfer
from otupy.encoders.json import JSONEncoder

import json_schema_validation

import acme
import mycompany
import mycompany_with_underscore
import example
import esm
import digits
import digits_and_chars


# Parameters to get good and bad samples of json messages
response_path_good = "openc2-json-schema/tests/responses/good"
response_path_bad = "openc2-json-schema/tests/responses/bad"

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

with open("openc2-json-schema/tests/commands/good/slpf_example_delete_rulenumber.json", 'r') as f:
	cmd_json =  json.load(f)
	cmd = Encoder.decode(Command, cmd_json)

	producer = Producer("OpenC2_Producer",
	                     JSONEncoder(),
                        HTTPTransfer("127.0.0.1",
                                     8080,
                                     endpoint="/.well-known/openc2"))
	resp = producer.sendcmd(cmd)

#with open("openc2-json-schema/tests/responses/bad/status_asdouble.json", 'r') as f:
#	rsp =  json.load(f)
#print("status: ", rsp['status'])
#c = Encoder.decode(Response, rsp)

#files = load_files(response_path_bad)

#for f in files:
#	print("File: ", f)
#	with open(f, 'r') as frsp:
#		rsp = json.load(frsp)
#		print("Response json: ", rsp)
#		Encoder.decode(Response, rsp)


#print("Response: ", c)
#print("Response encoded: ", JSONEncoder.encode(c))
