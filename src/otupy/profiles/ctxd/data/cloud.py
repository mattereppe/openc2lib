import otupy.types.base


class Cloud(otupy.types.base.Record):
	"""Cloud
    it is the description of the service - Cloud
	"""
	description: str = None
	""" Generic description of the cloud service """
	id: str = None
	""" ID of the Container """
	name: str = None
	""" Name of the cloud provider """
	type: str = None
	""" type of the cloud service"""


	def __init__(self, description = None, id = None, name = None, type = None):
		if isinstance(description, Cloud):
			self.description = description.description
			self.id = description.id
			self.name = description.name
			self.type = description.type
		else:
			self.description = description if description is not None else None
			self.id = id if id is not None else None
			self.name = name if name is not None else None
			self.type = type if type is not None else None
		self.validate_fields()

	def __repr__(self):
		return (f"Cloud(description={self.description}, id={self.id}, "
	             f"name={self.name}, type={self.type})")
	
	def __str__(self):
		return f"Cloud(" \
	            f"description={self.description}, " \
	            f"id={self.id}, " \
	            f"name={self.name}, " \
	            f"type={self.type})"

	def validate_fields(self):
		if self.description is not None and not isinstance(self.description, str):
			raise TypeError(f"Expected 'description' to be of type {str}, but got {type(self.description)}")
		if self.id is not None and not isinstance(self.id, str):
			raise TypeError(f"Expected 'id' to be of type {str}, but got {type(self.id)}")		
		if self.name is not None and not isinstance(self.name, str):
			raise TypeError(f"Expected 'name' to be of type {str}, but got {type(self.name)}")
		if self.type is not None and not isinstance(self.type, str):
			raise TypeError(f"Expected 'type' to be of type {str}, but got {type(self.type)}")
