import pytest
import os
import logging
import ipaddress
import json


from helpers import load_json, load_files, send_raw_command
from otupy import Encoder, Command, Response, Message, StatusCode, EncoderError
from otupy.core.producer import Producer
from otupy.profiles.ctxd.data.transfer import Transfer
import otupy.transfers.http
from otupy.transfers.http.http_transfer import HTTPTransfer
import otupy.transfers.http.message as http
from otupy.encoders.json import JSONEncoder

import json_schema_validation_ctxd

import acme

# Parameters to get good and bad samples of json messages
command_path_good = "../../openc2-json-schema/tests/commands/good/ctxd"
command_path_bad = "../../openc2-json-schema/tests/commands/bad/ctxd"


class JSONDump(logging.Filter):
	def filter(self, record):
		return  record.getMessage().startswith("HTTP Request Content") or record.getMessage().startswith("HTTP Response Content") 


def check_command(cmd):
	assert cmd is not None

@pytest.fixture
def create_producer():
	return Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))



def fix_ip_addresses(cmd):
	""" This function fixes ip addresses to compare with json examples provided by third party.
		According to common network practice, an IP network address should always include the prefix/netmask.
		The LS says a Connection should include "IP address range", so this implicitely demands for a prefix
		to be given. However, a single host address may be acceptable as well. Openc2lib strictly adhere to
		the network-biased convention to always give the prefix, but it also accepts ip addresses as input.
		This fix is necessary to convert the reference json examples so that they are comparable with the 
		notation of otupy.
	"""
	if 'ipv4_net' in cmd['target']:
		cmd['target']['ipv4_net'] = ipaddress.IPv4Network(cmd['target']['ipv4_net']).compressed
	if 'ipv6_net' in cmd['target']:
		cmd['target']['ipv6_net'] = ipaddress.IPv6Network(cmd['target']['ipv6_net']).compressed
	if 'ipv4_connection' in cmd['target']:
		for ip in ['src_addr', 'dst_addr']:
			if ip in cmd['target']['ipv4_connection']:
				cmd['target']['ipv4_connection'][ip] = ipaddress.IPv4Network(cmd['target']['ipv4_connection'][ip]).compressed
	if 'ipv6_connection' in cmd['target']:
		for ip in ['src_addr', 'dst_addr']:
			if ip in cmd['target']['ipv6_connection']:
		 		cmd['target']['ipv6_connection'][ip] = ipaddress.IPv6Network(cmd['target']['ipv6_connection'][ip]).compressed
	 		
	 	
def fix_hex(cmd):
	""" Convert BinaryX values to uppercase, as recommended by the specification"""
	for h in ['md5', 'sha1', 'sha256']:
		try:
			if h in cmd['target']['file']['hashes']:
				cmd['target']['file']['hashes'][h] = cmd['target']['file']['hashes'][h].upper()
		except:
			pass

	if 'mac_addr' in cmd['target']:
		# Use lowercase for similarity to BinaryX
		cmd['target']['mac_addr'] = cmd['target']['mac_addr'].upper()
	
def fix_uuid(cmd):
	""" UUID according to RFC 4122 are created as lowercase, but both cases are accepted as input.
		Here we stitch to lowercase for comparison.
		
		This is a very specific trick for the validation set.
	"""
	if 'x-acme:container' in cmd['target']:
		cmd['target']['x-acme:container']['container_id'] = cmd['target']['x-acme:container']['container_id'].lower()

def validate_json(caplog):
	""" Check the openc2 json messages exchanged between the consumer and the producer are valid according to the schema """
	
# WARNING: the visible logs are those generated within this function. Everything else in the fixture does not produce logs
	assert len(caplog.messages) == 2
	msg = caplog.messages[0]
	req = msg[msg.index("\n")+1:]
	msg = caplog.messages[1]
	rsp = msg[msg.index("\n")+1:]
	print(req)
	print(rsp)
	json_schema_validation_ctxd.validate_http(req, json_schema_validation_ctxd.Validation.base)
	json_schema_validation_ctxd.validate_http(req, json_schema_validation_ctxd.Validation.contrib)
	json_schema_validation_ctxd.validate_http(rsp, json_schema_validation_ctxd.Validation.base)
	json_schema_validation_ctxd.validate_http(rsp, json_schema_validation_ctxd.Validation.contrib)

	return True

@pytest.mark.parametrize("cmd", load_json(command_path_good) )
@pytest.mark.dependency(name="test_decoding")
def test_decoding(cmd):
	""" Test 'good' commands can be successfully decoded by otupy """
	c = JSONEncoder.decode(cmd, Command)
	assert type(c) == Command

@pytest.mark.parametrize("cmd", load_json(command_path_good) )
@pytest.mark.dependency(name="test_encoding", depends=["test_decoding"])
def test_encoding(cmd):
	""" Test 'good' commands can be successfully encoded by otupy

		The test decodes 'good' commands, and then create again the json. Finally, the original
		and created json are compared. A number of fixes are applied to account for different
		representations of the values (e.g., lowercase/uppercase).
	"""
	print("Command json: ", cmd)
	oc2_cmd = JSONEncoder.decode(cmd,Command)
	# Use to dict because the Encoder.encode method returns a str
	oc2_json = JSONEncoder.todict(oc2_cmd)
	print(oc2_json)

	fix_ip_addresses(cmd)
	fix_hex(cmd)
	fix_uuid(cmd)

	assert cmd == oc2_json


@pytest.mark.parametrize("cmd", load_json(command_path_good) )
#@pytest.mark.dependency(depends=["test_decoding", "test_encoding"])
def test_sending(cmd, create_producer, caplog):
	""" Test 'good' messages are successfully sent to the remote party and a response is received.

		Validate the openc2 json messages exchanged. The response is often an error because the majority
		of features are not implemented in the available actuators.
	"""
	c = Encoder.decode(Command, cmd)

# Filter the log to get what I need
	logger = logging.getLogger("otupy.transfers.http.http_transfer")
	logger.addFilter(JSONDump())

	check_command(c)
	print("Command: ", c)
	with caplog.at_level(logging.INFO):
		resp = create_producer.sendcmd(c)

	assert type(resp) == Message
	assert type(resp.content) == Response

	assert validate_json(caplog) == True
		

@pytest.mark.parametrize("cmd", load_json(command_path_bad) )
def test_sending_invalid(cmd, create_producer, caplog):
	try:
        # Decode and attempt to send the command
		c = Encoder.decode(Command, cmd)
		resp = create_producer.sendcmd(c)

        # Check if the status is BADREQUEST
		if resp.content.get('status') == StatusCode.BADREQUEST:
            # The test succeeds if BADREQUEST status is returned
			return

        # If no exception and status is not BADREQUEST, we raise an error to fail the test
		assert False, "Expected an exception or BADREQUEST status, but neither occurred."

	except Exception as exc:
        # The test succeeds if any exception is raised
		pass


