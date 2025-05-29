import otupy.types.base
from otupy.profiles.ctxd.data.network_type import NetworkType


class Network(otupy.types.base.Record):
	"""Network
    it is the description of the service - Network
	"""
	description: str = None
	""" Generic description of the network """
	name: str = None
	""" Name of the network provider """
	type: NetworkType = None
	""" type of the network service"""


	def __init__(self, description = None, name = None, type = None):
		if isinstance(description, Network):
			self.description = description.description
			self.name = description.name
			self.type = description.type
		else:
			self.description = str(description) if description is not None else None
			self.name = str(name) if name is not None else None
			self.type = type if type is not None else None

	def __repr__(self):
		return (f"Network(description={self.description}, "
	             f"name={self.name}, type={self.type})")
	
	def __str__(self):
		return f"Network(" \
	            f"description={self.description}, " \
	            f"name={self.name}, " \
	            f"type={self.type})"

