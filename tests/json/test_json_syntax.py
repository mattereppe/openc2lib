import pytest
import logging
from openc2lib import *

import json_schema_validation

import openc2lib.profiles.slpf as slpf
from openc2lib.transfers.http import HTTPTransfer
from openc2lib.encoders.json import  JSONEncoder


class JSONDump(logging.Filter):
	def filter(self, record):
		return  record.getMessage().startswith("HTTP Request Content") or record.getMessage().startswith("HTTP Response Content") 


def check_command(cmd):
	assert cmd is not None


def test_query_feature(create_producer, query_feature, caplog):
	
# Filter the log to get what I need
	logger = logging.getLogger("openc2lib.transfers.http.http_transfer")
	logger.addFilter(JSONDump())

	check_command(query_feature)
	with caplog.at_level(logging.INFO):
		create_producer.sendcmd(query_feature)

# WARNING: the visible logs are those generated within this function. Everything else in the fixture does not produce logs
#	assert "Sending" in caplog.text
#	assert ("openc2lib.transfers.http.http_transfer", logging.INFO, "Sending to http://127.0.0.1:8080/.well-known/openc2") in caplog.record_tuples
	assert len(caplog.messages) == 2
	msg = caplog.messages[0]
	req = msg[msg.index("\n")+1:]
	msg = caplog.messages[1]
	rsp = msg[msg.index("\n")+1:]
	print(req)
	print(rsp)
	json_schema_validation.validate_http(req, json_schema_validation.Validation.base)
	json_schema_validation.validate_http(req, json_schema_validation.Validation.contrib)
	json_schema_validation.validate_http(rsp, json_schema_validation.Validation.base)
	json_schema_validation.validate_http(rsp, json_schema_validation.Validation.contrib)

@pytest.mark.parametrize("cmd", ["query"])
#@pytest.mark.parametrize("cmd", ["scan", "query", "allow"])
def test_parameter(create_producer, cmd):
	assert cmd == "query"	
	
		

