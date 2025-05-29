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
import mycompany_dots
import mycompany_with_underscore
import example
import esm
import digits
import digits_and_chars


# Parameters to get good and bad samples of json messages
command_path_good = "../../openc2-json-schema/tests/commands/good"
command_path_bad = "../../openc2-json-schema/tests/commands/bad"


class JSONDump(logging.Filter):
	def filter(self, record):
		return  record.getMessage().startswith("HTTP Request Content") or record.getMessage().startswith("HTTP Response Content") 


def check_command(cmd):
	assert cmd is not None


# WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING 
# 
# The command in openc2-json-schema/src/test/resources/commands/good/deny_uri_actuator_multiple.json
# does not conform to the language specification, since the actuator is defined as "Choice", hence
# it cannot contain multiple values.
# I removed the x-esm actuator and renamed the file to deny_uri.json; I moved the original file to 
# the "bad" examples. 
#
# The command in openc2-json-schema/src/test/resources/commands/good/allow_ipv6net_wikipedia8_prefix2.json
# uses an IPv6 address as ipv6net. The standard refers to RFC 8200, but that RFC does not state anything
# about IPv6 addresses/networks. The standard also says that if the prefix is omitted, the IPv6-Net
# refers to a single host address. This is perfectly aligned with the general understanding that a
# network address must have all bits zeroed in the host part (and it is also compliant with the python
# ipaddress package. Based on these considerations, I changed the IP address to "2001:db8:a::/64" and
# moved the original file to the "bad" examples.
# The same happened for openc2-json-schema/src/test/resources/commands/good/allow_ipv6net_prefix.json.
# Fixed the same way as the previous file, by setting the address to "3ffe:1900:4545:3:0:0:0:0/64".
# Done again for openc2-json-schema/src/test/resources/commands/good/allow_ipv4net_cidr.json.
# Fixed address to: "127.0.0.0/8"
#
# The command in openc2-json-schema/src/test/resources/commands/good/query_features_ext_target.json
# (and maybe other files) uses a uncommon definition for a sort of extension to features. It
# defines the new x-acme:feature target as a map, containing the standard-style feature target
# definition: "'target': {'x-acme:features': {'features': ['versions', 'profiles', 'schema']}}"
# This does not look aligned with the definition in the Language Specification, but since it is
# an extension I did not change it and provided the implementation according to this definition.
# 
# >>>>>>>>>>>>>> Keep in mind to redo this if you update the repository. <<<<<<<<<<<<<<<<<<<<<<<<
#
# WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING 



@pytest.mark.parametrize("cmd", load_json(command_path_good) )
@pytest.mark.dependency(name="test_decoding")
def test_decoding(cmd):
	""" Test 'good' commands can be successfully decoded by lycam """
	print("Command json: ", cmd)
	c = openc2.parse(cmd)
	assert type(c) == openc2.v10.Command

@pytest.mark.parametrize("cmd", load_json(command_path_good) )
@pytest.mark.dependency(name="test_encoding", depends=["test_decoding"])
def test_encoding(cmd):
	""" Test 'good' commands can be successfully encoded by otupy

		The test decodes 'good' commands, and then create again the json. Finally, the original
		and created json are compared. A number of fixes are applied to account for different
		representations of the values (e.g., lowercase/uppercase).
	"""
	print("Command json: ", cmd)
	oc2_cmd = openc2.parse(cmd)
	print("Lycan data: ", oc2_cmd)
	bar = json.loads(oc2_cmd.serialize())
	print("Re-encoded Command json: ", bar)

	assert cmd == bar


@pytest.mark.parametrize("cmd_file", load_files(command_path_bad) )
def test_decoding_invalid(cmd_file):
	""" Check invalid commands raise exceptions when decoded """
	print("Command file: ", cmd_file)
	# It may also raises while loading the files, since they may be empty
	with open(cmd_file, 'r') as fcmd:
		try:
			cmd = json.load(fcmd) 
		except json.decoder.JSONDecodeError:
			cmd = ""
		with pytest.raises( Exception ):
			print("Command json: ", cmd)
			openc2.parse(cmd)
		

