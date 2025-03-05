from openc2lib.types.base import Choice
from openc2lib.core.register import Register

#ATTENTION!! THIS IS NOT THE DEFINITION OF THE CTXD SPECIFICATION 
class NetworkType(Choice):

	register = Register({'ethernet': str, '802.11': str, '802.15': str, 'zigbee': str, 'vlan': str, 'vpn': str, 'lorawan': str, 'wan': str})

	def __init__(self, type):
		if(isinstance(type, NetworkType)):
			super().__init__(type.obj)
		else:
			super().__init__(type)