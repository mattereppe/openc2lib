import openc2lib.types.base
from openc2lib.profiles.ctxd.data.os import OS
from openc2lib.types.data.hostname import Hostname

class VM(openc2lib.types.base.Record):
	"""VM
    it is the description of the service - Virtual Machine
	"""
	description: str = None
	""" Generic description of the VM """
	id: str = None
	""" ID of the VM """
	hostname: Hostname = None
	""" Hostname of the VM"""
	os: OS = None
	""" Operating System of the VM """

	def __init__(self, description:str = None, id:str = None, hostname:Hostname = None, os:OS = None):
		if(isinstance(description, VM)):
			self.description = description.description
			self.id = description.id
			self.hostname = description.hostname
			self.os = description.os
		else:
			self.description = description if description is not None else None
			self.id = id if id is not None else None
			self.hostname = hostname if hostname is not None else None
			self.os = os if os is not None else None
		self.validate_fields()

	def __repr__(self):
		return (f"VM(description='{self.description}', id={self.id}, "
	             f"hostname='{self.hostname}', os={self.os})")
	
	def __str__(self):
		return f"VM(" \
	            f"description={self.description}, " \
	            f"id={self.id}, " \
	            f"hostname={self.hostname}, " \
	            f"os={self.os})"

	def validate_fields(self):
		if self.description is not None and not (isinstance(self.description, str) or isinstance(self.description, VM)):
			raise TypeError(f"Expected 'description' to be of type str, but got {type(self.description)}")
		if self.id is not None and not isinstance(self.id, str):
			raise TypeError(f"Expected 'id' to be of type str, but got {type(self.id)}")
		if self.hostname is not None and not isinstance(self.hostname, Hostname):
			raise TypeError(f"Expected 'hostname' to be of type Hostname, but got {type(self.hostname)}")
		if self.os is not None and not isinstance(self.os, OS):
			raise TypeError(f"Expected 'os' to be of type {OS}, but got {type(self.os)}")