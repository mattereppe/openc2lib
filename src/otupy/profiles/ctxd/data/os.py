import otupy.types.base


class OS(otupy.types.base.Record):
	"""OS
    Operating System
	"""
	name: str = None
	""" Name of the OS """
	version: str = None
	""" Version of the OS """
	family: str = None
	""" Family of the OS """
	type: str = None
	""" type of the OS """


	def __init__(self, name = None, version = None, family = None, type = None):
		self.name = str(name) if name is not None else None
		self.version = str(version) if version is not None else None
		self.family = str(family) if family is not None else None
		self.type = str(type) if type is not None else None

	def __repr__(self):
		return (f"OS(name={self.name}, "
	             f"version={self.version}, family={self.family}, type={self.type})")
	
	def __str__(self):
		return f"OS(" \
	            f"name={self.name}, " \
				f"version={self.version}, " \
	            f"family={self.family}, " \
	            f"type={self.type})"

