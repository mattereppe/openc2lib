from openc2lib.types.base import Map
from openc2lib.types.data import Hashes

class File(Map):
	""" OpenC2 File

		Implements the `file` target (Section 3.4.1.6). 
		Properties of a file. A "File" Target MUST contain at least one property.

	"""
	fields = {'name': str, 'path': str, 'hashes': Hashes}
	"""
		Internal class members are just provided as reference for valid fields and to map their name
		to the expected type. They shall not be instantiated or used directly.
		`name`: The name of the file as defined in the file system 
		`path`: The absolute path to the location of the file in the file system 
		`hashes`: One or more cryptographic hash codes of the file contents 
	"""

	def __init__(self, file: dict):
		super().__init__(file)
		# Explicit control on each field is carried out to manage the possibility of wrong
		# inputs or inputs defined by extensions
		for x in self.keys():
			if x in self.fields:
				return
		raise ValueError("A 'File' Target MUST contain at least one property.")
