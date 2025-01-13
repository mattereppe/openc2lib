import openc2
import sys
import uuid

sys.path.insert(0, "profiles/")

import acme_specialchar1

id=acme_specialchar1.UuidProperty().clean(uuid.uuid4())
argp=acme_specialchar1.AcmeProperty(firewall_status="active")
act=acme_specialchar1.AcmeActuator(asset_id=id, endpoint_id="iptables1")
p2=acme_specialchar1.AcmeProperty(container_id="E57C0116-D291-4AF3-BEF9-0F5B604A2C85")
t2=acme_specialchar1.ContainerTarget(container=p2)

arg = acme_specialchar1.AcmeArgs(**{"x-acm&e":argp})

cmd = openc2.v10.Command(action="start", target=t2, args=arg, actuator=act)
print(cmd)
