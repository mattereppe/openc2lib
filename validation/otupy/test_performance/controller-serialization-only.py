#!../../../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import sys
import time
import json

import otupy as oc2

from otupy.encoders.json import JSONEncoder

import otupy.profiles.slpf as slpf
import otupy.profiles.dumb as dumb

from helpers import load_files

import sys
sys.path.insert(0, "../profiles/")

import acme
import mycompany
import mycompany_with_underscore
import example
import esm
import digits
import digits_and_chars

command_path_good = "openc2-commands-good"
response_path_good = "openc2-responses-good"
NUM_TESTS = 100

def main():

	cmd_files = load_files(command_path_good)
	rsp_files = load_files(response_path_good)

	for i in range(1, NUM_TESTS+1):
		print("Running test #", i)
		for c in cmd_files:

			with open(c) as f:
				cmd_txt=f.read()
			print("Decoding started at time: ", time.time())
			cmd = JSONEncoder.decode(cmd_txt, oc2.Command)
			print("Decoding ended at time: ", time.time())

			print("Encoding started at time: ", time.time())
			JSONEncoder.encode(cmd)
			print("Encoding ended at time: ", time.time())
	
		for r in rsp_files:

			with open(r) as f:
				rsp_txt=f.read()
			print("Decoding started at time: ", time.time())
			rsp = JSONEncoder.decode(rsp_txt, oc2.Response)
			print("Decoding ended at time: ", time.time())

			print("Encoding started at time: ", time.time())
			JSONEncoder.encode(rsp)
			print("Encoding ended at time: ", time.time())
	


if __name__ == '__main__':
	main()
