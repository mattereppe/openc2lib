import pytest
import os
import logging
import ipaddress
import json


from helpers import load_json, load_files, send_raw_command
from openc2lib import Encoder, Command, Response, Message, StatusCode, EncoderError, Feature
from openc2lib.core.producer import Producer
import openc2lib.transfers.http
from openc2lib.profiles.rcli.data.transfer import Transfer
from openc2lib.transfers.http.http_transfer import HTTPTransfer
import openc2lib.transfers.http.message as http
from openc2lib.encoders.json import JSONEncoder

import json_schema_validation_rcli

Feature.extend("clicommands",5)

# Parameters to get good and bad samples of json messages
command_path_good = "../../openc2-json-schema/tests/commands/good/rcli"
command_path_bad = "../../openc2-json-schema/tests/commands/bad/rcli"


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
		notation of openc2lib.
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
	#json_schema_validation_rcli.validate_http(req, json_schema_validation_rcli.Validation.base)
	json_schema_validation_rcli.validate_http(req, json_schema_validation_rcli.Validation.contrib)
	#json_schema_validation_rcli.validate_http(rsp, json_schema_validation_rcli.Validation.base)
	json_schema_validation_rcli.validate_http(rsp, json_schema_validation_rcli.Validation.contrib)

	return True

@pytest.mark.parametrize("cmd", load_json(command_path_good) )
@pytest.mark.dependency(name="test_decoding")
def test_decoding(cmd):
	""" Test 'good' commands can be successfully decoded by openc2lib """
	c = JSONEncoder.decode(cmd, Command)
	assert type(c) == Command

@pytest.mark.parametrize("cmd", load_json(command_path_good) )
@pytest.mark.dependency(name="test_encoding", depends=["test_decoding"])
def test_encoding(cmd):
	""" Test 'good' commands can be successfully encoded by openc2lib

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
	logger = logging.getLogger("openc2lib.transfers.http.http_transfer")
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

@pytest.mark.parametrize("file",  load_files(command_path_bad)  )
def test_response_to_invalid_commands(file, http_url, http_headers, http_body):
	""" Send invalid commands and check a BADREQUEST is returned

		Read invalid commands from file and send them to a Consumer. Commands are not encoded (because invalid).
		Check that a BADREQUEST status is returned.
	"""
	print("Command json: ", file)
	# It may also raises while loading the files, since they may be empty
	count = 0
	with open(file, 'r') as fcmd:
		try:
			cmd = json.load(fcmd) 
		except:
			# In the bad exampes, 1 file is empty. If more than one file cannot be read, something has changed!
			if fcmd.read() == '':
				cmd = {}	
			else:
				raise ValueError("Unable to read json")
		http_body['body']['openc2']['request'] = cmd
		response = send_raw_command(http_url, http_headers, json.dumps(http_body))

		assert response.status_code == 400

		msg = JSONEncoder.decode(response.text, http.Message)
		assert msg.body.getObj().getObj()['status'] == StatusCode.BADREQUEST
		



