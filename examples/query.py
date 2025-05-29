#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#

import uuid 

import otupy 
from otupy.encoders.json import JSONEncoder

# Define custom target
@otupy.target(name='container', nsid='x-acme')
class AcmeContainer(otupy.Map):
	fieldtypes = {'container_id': uuid.UUID}

# Define custom actuator
@otupy.actuator(nsid='x-acme')
class AcmeActuator(otupy.Map):
	fieldtypes = {'endpoint_id': str, 'asset_id': str}
	nsid = 'x-acme'

def main():
	u=uuid.UUID("E57C0116-D291-4AF3-BEF9-0F5B604A2C85")
	t=AcmeContainer(container_id=u)

	act=AcmeActuator(asset_id='0123456789abcdef0123456789abcdef', endpoint_id="iptables1")
	cmd = otupy.Command(action=otupy.Actions.query, target=t, actuator=act)

	d = JSONEncoder.encode(cmd)


	print(d)

if __name__ == '__main__':
	main()
