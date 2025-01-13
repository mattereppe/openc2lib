#!../../../../lycan/.venv/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys

import openc2
import time

from helpers import load_json

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
	cmd_list = load_json(command_path_good) 
	rsp_list = load_json(response_path_good)
	for i in range(1, NUM_TESTS+1):
		print("Running test #", i)
		for c in cmd_list:
			cmd = openc2.parse(c)
	
			print("Encoding started at time: ", time.time())
			cmd.serialize()
			print("Encoding ended at time: ", time.time())

		for r in rsp_list:
			print("Decoding started at time: ", time.time())
			rsp = openc2.parse(r)
			print("Decoding ended at time: ", time.time())



if __name__ == '__main__':
	main()
