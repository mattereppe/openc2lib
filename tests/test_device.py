#!../.oc2-env/bin/python3
# Test the actifact target

import hashlib
import logging
import sys

import otupy as oc2
from otupy.transfers.http import HTTPTransfer
from otupy.encoders.json import  JSONEncoder
import otupy.profiles.dumb as dumb

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

p = oc2.Producer("producer.example.net", JSONEncoder(), HTTPTransfer("127.0.0.1", 8080))
pf = dumb.dumb({'hostname':'mockup', 'named_group':'testing', 'asset_id':'dumb'})

d = oc2.Device(
		hostname="host.domain.com",
		idn_hostname="host.domain.com",
		device_id="myhost-123"
		)
cmd = oc2.Command(oc2.Actions.scan, d, actuator = pf)

resp = p.sendcmd(cmd)
print(resp)
