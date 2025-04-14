import pytest
import json
import sys
import requests

import os
sys.path.insert(0, "profiles/")

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


