#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import logging
import sys
import sqlite3
import otupy as oc2

from otupy.encoders.json import JSONEncoder
from otupy.transfers.http import HTTPTransfer
from otupy.actuators.iptables_actuator import IptablesActuator
import otupy.profiles.slpf as slpf

#logging.basicConfig(filename='consumer.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger('openc2')

def init_db():
    conn = sqlite3.connect('openc2_commands.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS commands (rule_number INTEGER PRIMARY KEY, command TEXT)''')
    conn.commit()
    conn.close()

init_db()

def main():

# Instantiate the list of available actuators, using a dictionary which key
# is the assed_id of the actuator.
	actuators = {}
	actuators[(slpf.Profile.nsid,'iptables')]=IptablesActuator()

	c = oc2.Consumer("testconsumer", actuators, JSONEncoder(), HTTPTransfer("172.17.0.11", 8080))


	c.run()


if __name__ == "__main__":
	main()
