import otupy.types.base


class IOT(otupy.types.base.Record):
	"""IOT
    it is the description of the service - IOT
	"""
	description: str = None
	""" Identifier of IOT function """
	name: str = None
	""" Name of the IOT service provider """
	type: str = None
	""" type of the IOT device"""


	def __init__(self, description = None, name = None, type = None):
		if isinstance(description, IOT):
			self.description = description.description
			self.name = description.name
			self.type = description.type
		else:
			self.description = description if description is not None else None
			self.name = name if name is not None else None
			self.type = type if type is not None else None
		self.validate_fields()

	def __repr__(self):
		return (f"IOT(description={self.description}, "
	             f"name={self.name}, type={self.type})")
	
	def __str__(self):
		return f"Cloud(" \
	            f"description={self.description}, " \
	            f"name={self.hostname}, " \
	            f"type={self.type})"
	
	def validate_fields(self):
		if self.description is not None and not isinstance(self.description, str):
			raise TypeError(f"Expected 'description' to be of type {str}, but got {type(self.description)}")		
		if self.name is not None and not isinstance(self.name, str):
			raise TypeError(f"Expected 'name' to be of type {str}, but got {type(self.name)}")
		if self.type is not None and not isinstance(self.type, str):
			raise TypeError(f"Expected 'type' to be of type {str}, but got {type(self.type)}")

