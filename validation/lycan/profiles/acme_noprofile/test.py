import openc2
import sys
import uuid

sys.path.insert(0, "profiles/")

import acme_noprofile

id=acme_noprofile.UuidProperty().clean(uuid.uuid4())
argp=acme_noprofile.AcmeProperty(firewall_status="active")
act=acme_noprofile.AcmeActuator(asset_id=id, endpoint_id="iptables1")
t=acme_noprofile.FeaturesTarget(features=["versions", "profiles"])
p2=acme_noprofile.AcmeProperty(container_id="E57C0116-D291-4AF3-BEF9-0F5B604A2C85")
t2=acme_noprofile.ContainerTarget(container=p2)

arg = acme_noprofile.AcmeArgs(**{"":argp})

cmd = openc2.v10.Command(action="query", target=t, args=arg, actuator=act)
print(cmd)
cmd2 = openc2.v10.Command(action="start", target=t2, args=arg, actuator=act)
print(cmd2)
