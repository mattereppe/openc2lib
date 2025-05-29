from otupy.types.data.hostname import Hostname
from otupy.types.data.idn_hostname import IDNHostname
from otupy.types.base.map	import Map
from otupy.core.target import target

@target('device')
class Device(Map):
	""" Identify network device.
		
		Properties:
		- hostname: A hostname that can be used to connect to this device over a network.
		- idn_hostname: An internationalized hostname that can be used to connect to this device over a network.
		- device_id: An identifier that refers to this device within an inventory or management system.

		A "Device" Target MUST contain at least one property.
	"""
	fieldtypes = {'hostname': Hostname, 'idn_hostname': IDNHostname, 'device_id': str}

	def __init__(self, *args, **kwargs):
		""" Initialize the `Device`

			This object can be initialized both with a dictionary and with keyword arguments. For valid
			fields that can be used, see `Device`. 
			Keyword arguments take precedence over non-keyword arguments.
			Non-keyword arguments must precede keyword arguments.
			:param args: Dictionary of key/value pairs. 
			:param kwargs: Keyword arguments.
		"""
		super().__init__(*args, **kwargs)
		try: 
			self.validate_fields()
		except ValueError:
			raise ValueError("A 'Device' Target MUST contain at least one property.")
		# TypeError exception is not caught and passed upwards unaltered


