import openc2
import sys
import uuid
import json

sys.path.insert(0, "../profiles/")

import acme 

id=acme.UuidProperty().clean(uuid.uuid4())
id=acme.UuidProperty().clean('0123456789abcdef0123456789abcdef')
id='0123456789abcdef0123456789abcdef'
argp=acme.AcmeArgs(**{'x-acme': acme.AcmeProperty(firewall_status="active")})
act=acme.AcmeActuator(asset_id=id, endpoint_id="iptables1")
p1=acme.AcmeProperty(features=["versions", "profiles"])
t1=acme.FeaturesTarget(features=p1)
p2=acme.AcmeProperty(container_id="E57C0116-D291-4AF3-BEF9-0F5B604A2C85")
t2=acme.ContainerTarget(container=p2)

cmd = openc2.v10.Command(action="query", target=t1, args=argp, actuator=act)
print(cmd)
#cmd2 = openc2.v10.Command(action="start", target=t2, args=argp, actuator=act)
#print(cmd2)
#
#msg = cmd2.serialize()
#print("Serialized: ", msg)
#
#bar = openc2.parse(msg)
#print("De-serialized: ", bar)
#
#bar2= openc2.v10.Command(**json.loads(msg))
#print("De-serialized with command: ", bar2)

cmd3 = openc2.parse({'action': 'query', 'target': {'x-acme:features': {'features': ['versions', 'profiles', 'schema']}}})
print("Parsed: ", cmd3)
cmd4 = openc2.v10.Command(**{'action': 'query', 'target': {'x-acme:features': {'features': ['versions', 'profiles', 'schema']}}})
print("Instantiated: ", cmd4)
print("cmd3: ", (cmd3['target']))
print("t1: ", (t1))
print(cmd3['target']['features'])
t3=acme.FeaturesTarget(features=['ciccio', 'birillo'])
print("t3: ", (t3))
