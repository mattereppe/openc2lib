import pytest
import json
import sys
import requests

import os
sys.path.insert(0, "profiles/")

#import acme
#import mycompany
#import mycompany_with_underscore
#import example
#import esm
#import digits
#import digits_and_chars
#import otupy.profiles.slpf


#def create_command(string = None, file= None):
#	""" Create an otupy command from a json string or file. 
#		
#		It expects the command in a string; alternatively, the file containing the json can be given by
#		specifying its keyword. If both are given, the string is used. """
#	print(file)
#	if string:
#		cmd_dict = json.loads(string)
#	elif file:
#		with open(file, 'r') as f:
#			cmd_dict = json.load(f)
#	else:
#		raise TypeError("Json string or file must be given!")
#
#	print(cmd_dict)
#	return  Encoder.decode(Command, cmd_dict)

def load_files(cmd_path):
	""" Load all files with json commads """
	# There should be no dirs in the folder I'm looking for commands, but I filter out directories just to be sure
	cmds_files = [
    os.path.join(cmd_path,f) for f in os.listdir(cmd_path) if os.path.isfile(os.path.join(cmd_path, f))
	]

# use this if you want to debug a single file
#	cmds_files = [ "openc2-json-schema/src/test/resources/commands/bad/action_notarget.json" ]

	return cmds_files

def load_json(path):
	""" Load an otupy command/response from a json string or file. 
		
		It expects the command in a string; alternatively, the file containing the json can be given by
		specifying its keyword. If both are given, the string is used. """

	files = load_files(path)
# use this if you want to debug a single file
#cmds_files = [ "openc2-json-schema/src/test/resources/commands/bad/action_notarget.json" ]

	lst = []
	for f in files:
		print("Processing file ", f)

		with open(f, 'r') as j:
			lst.append(  json.load(j) )

	return lst

def send_raw_command(url, oc2hdrs, oc2data):
	""" This function emulates a faulty producer that sends invalid openc2 messages (only the body in http) """
	print("Message body: ", oc2data)
	return requests.post(url, data=oc2data, headers=oc2hdrs, verify=False)

