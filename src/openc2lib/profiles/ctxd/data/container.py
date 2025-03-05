import openc2lib.types.base
from openc2lib.profiles.ctxd.data.os import OS

class Container(openc2lib.types.base.Record):
	"""Container
    it is the description of the service - Container
	"""
	description: str = None
	""" Generic description of the Container """
	id: str = None
	""" ID of the Container """
	hostname: str = None
	""" Hostname of the Container"""
	runtime: str = None
	""" Hostname managing the Container"""
	os: OS = None
	""" Operating System of the Container """

	def __init__(self, description = None, id = None, hostname = None, runtime = None, os = None):
		if isinstance(description, Container):
			self.description = description.description
			self.id = description.id
			self.hostname = description.hostname
			self.runtime = description.runtime
			self.os = description.os
		else:
			self.description = str(description) if description is not None else None
			self.id = str(id) if id is not None else None
			self.hostname = str(hostname) if hostname is not None else None
			self.runtime = str(runtime) if runtime is not None else None
			self.os = os if os is not None else None
		self.validate_fields()

	def __repr__(self):
		return (f"Container(description={self.description}, id={self.id}, "
	             f"hostname={self.hostname}, runtime={self.runtime},os={self.os})")
	
	def __str__(self):
		return f"Container(" \
	            f"description={self.description}, " \
	            f"id={self.id}, " \
	            f"hostname={self.hostname}, " \
				f"runtime={self.runtime}, " \
	            f"os={self.os})"
	
	def validate_fields(self):
		if self.description is not None and not isinstance(self.description, str):
			raise TypeError(f"Expected 'description' to be of type {str}, but got {type(self.description)}")
		if self.id is not None and not isinstance(self.id, str):
			raise TypeError(f"Expected 'id' to be of type {str}, but got {type(self.id)}")		
		if self.hostname is not None and not isinstance(self.hostname, str):
			raise TypeError(f"Expected 'hostname' to be of type {str}, but got {type(self.hostname)}")
		if self.runtime is not None and not isinstance(self.runtime, str):
			raise TypeError(f"Expected 'runtime' to be of type {str}, but got {type(self.runtime)}")	
		if self.os is not None and not isinstance(self.os, OS):
			raise TypeError(f"Expected 'os' to be of type {OS}, but got {type(self.os)}")

