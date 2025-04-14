from otupy.types.base import Map
from otupy.types.data import Hashes
from otupy.core.target import target

@target('file')
class File(Map):
	""" OpenC2 File

		Implements the `file` target (Section 3.4.1.6). 
		Properties of a file. A "File" Target MUST contain at least one property.

	"""
	fieldtypes = {'name': str, 'path': str, 'hashes': Hashes}
	"""
		Internal class members are just provided as reference for valid fields and to map their name
		to the expected type. They shall not be instantiated or used directly.
		`name`: The name of the file as defined in the file system 
		`path`: The absolute path to the location of the file in the file system 
		`hashes`: One or more cryptographic hash codes of the file contents 
	"""

	def __init__(self, *args, **kwargs):
		""" Initialize the `File`

			This object can be initialized both with a dictionary and with keyword arguments. For valid
			fields that can be used, see `File`. 
			Keyword arguments take precedence over non-keyword arguments.
			Non-keyword arguments must precede keyword arguments.
			:param args: Dictionary of key/value pairs. 
			:param kwargs: Keyword arguments.
		"""
		super().__init__(*args, **kwargs)
		# Explicit control on each field is carried out to manage the possibility of wrong
		# inputs or inputs defined by extensions
		try: 
			self.validate_fields()
		except ValueError:
			raise ValueError("A 'File' Target MUST contain at least one property.")
		# TypeError exception is not caught and passed upwards unaltered
