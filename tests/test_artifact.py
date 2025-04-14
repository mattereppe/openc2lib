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

#h = oc2.Hashes()
bcontent=b'My binary payload'
#h['md5']=oc2.Binaryx(hashlib.md5(bcontent).digest())
h = oc2.Hashes({'md5': oc2.Binaryx(hashlib.md5(bcontent).digest())})
print(h['md5'])
a = oc2.Artifact(
		mime_type='application/json', 
		payload=oc2.Payload(oc2.Binary(bcontent)),
#	payload=oc2.Binary(bcontent),
		hashes= h
		)
cmd = oc2.Command(oc2.Actions.copy, a, actuator = pf)

print(cmd)

#resp = p.sendcmd(cmd)
#print(resp)
