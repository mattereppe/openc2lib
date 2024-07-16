import json
import enum

from jsonschema import validate

json_schema_cmd='openc2-json-schema/schemas/command.json'
json_schema_rsp='openc2-json-schema/schemas/response.json'
json_schema_contrib = 'openc2-json-schema/schemas/contrib/oc2ls-v1.0-wd14_update.json'
json_schema_http = 'openc2-http-json-schema/message.json'

class Validation(enum.Enum):
	command  = 1
	response = 2
	base     = 1024
	contrib  = 1025

def detect_duplicated_keys(json):
	d = {}
	for k,v in json:
		if k in d:
			raise KeyError("Duplicated key: " + str(k))
		else:
			d[k] = v
	return d

def validate_http(msg, schema_type=None):
	""" Validate json message in HTTP body

		Validate the `msg` inside an HTTP body. If `schema_type` is provided, performs the validation of the 
		OpenC2 command/response; otherwise, only validation of HTTP-specific message encoding is performed.

		The `schema_type` used for validation of the OpenC2 command/response can be the `base` schema defined by the author of 
		[openc2-json-schema](https://github.com/bberliner/openc2-json-schema/tree/master) or the `contrib`
		provided by additional contributors to the same project. The `contrib` schema includes more controls
		than the `base` schema.

		:param msg: The json encoding of either a `Command` or `Response` message.
		:param schema_type: The type of schema to use: `Validation.base` or `Validation.contrib`. `None` means no validation of OpenC2 command/response is performed (default).
		:return: True if validation succeds, an `Exception` otherwise.
	"""
	with open(json_schema_http, 'r') as f:
		schema = json.loads(f.read())

	content = json.loads(msg, object_pairs_hook=detect_duplicated_keys)
	try:
		validate(instance=content, schema=schema)
	except Exception as e:
		print("Error while validating: ", content)
		print(e)
		assert False
	
	if schema_type:
		if list(content["body"]["openc2"].keys())[0] == "request":
			validate_openc2(content["body"]["openc2"]["request"], Validation.command, schema_type)
		elif list(content["body"]["openc2"].keys())[0] == "response":
			validate_openc2(content["body"]["openc2"]["response"], Validation.response, schema_type)
		else:
			raise ValueError("Unable to validate OpenC2 " + list(content["body"]["openc2"].keys())[0])
	
def validate_openc2(msg, msg_type, schema_type):
	""" Validate json command/response

		Validate  `msg` of `msg_type` (either `command` or `response`) with `schema_type`.
		The `schema_type` used for validation can be the `base` schema defined by the author of 
		[openc2-json-schema](https://github.com/bberliner/openc2-json-schema/tree/master) or the `contrib`
		provided by additional contributors to the same project. The `contrib` schema includes more controls
		than the `base` schema.

		:param msg: The json encoding of either a `Command` or `Response` message.
		:param msg_type: The type of message:  `Validation.command` or `Validation.response`.
		:param schema_type: The type of schema to use: `Validation.base` or `Validation.contrib`.
		:return: True if validation succeds, an `Exception` otherwise.
	"""

	if schema_type == Validation.base:
		if msg_type == Validation.command:
			schema_file = json_schema_cmd
		else:
			schema_file = json_schema_rsp
	elif schema_type == Validation.contrib:
		schema_file = json_schema_contrib
	else:
		raise ValueError("Invalid schema")
		
	print("Validation schema: ", schema_file)
	print("Validation type: ", schema_type)
	print("Validation msg: ", msg)
	with open(schema_file,'r') as f:
		schema = json.loads(f.read())
	
	validate(instance=msg, schema=schema)






if __name__ == "__main__":
#validate_cmd(json.loads(command))
#	validate_cmd_contrib()
	validate_http(http, validate_cmd)
