from openc2lib.types.data.hostname import Hostname
from openc2lib.types.data.idn_hostname import IDNHostname
from openc2lib.types.base.map	import Map

class Device(Map):
	""" Identify network device.
		
		Properties:
		- hostname: A hostname that can be used to connect to this device over a network.
		- idn_hostname: An internationalized hostname that can be used to connect to this device over a network.
		- device_id: An identifier that refers to this device within an inventory or management system.

		A "Device" Target MUST contain at least one property.
	"""
	fieldtypes = {'hostname': Hostname, 'idn_hostname': IDNHostname, 'device_id': str}
