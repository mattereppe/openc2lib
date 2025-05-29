from typing import Self

from otupy.types.base import Map
from otupy.types.targets import File
from otupy.core.target import target

@target('process')
@Map.make_recursive
class Process(Map):
	""" OpenC2 Process

		Implements the `process` target (Section 3.4.1.15). 
		Common properties of an instance of a computer program as executed on an operating system.

	"""
	fieldtypes = {'pid': int, 'name': str, 'cwd': str, 'executable': File, 'parent': Self, 'command_line': str}
	"""
		Internal class members are just provided as reference for valid fields and to map their name
		to the expected type. They shall not be instantiated or used directly.
		`pid`: Process ID of the process 
		`name`: Name of the process 
		`cwd`: Current working directory of the process 
		`executable`: Executable that was executed to start the process 
		`parent`: Process that spawned this one 
		`command_line`: The full command line invocation used to start this process, including all arguments 
	"""

	def __init__(self, *args, **kwargs):
		""" Initialize the `Process`

			This object can be initialized both with a dictionary and with keyword arguments. For valid
			fields that can be used, see `Process`. 
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
			raise ValueError("A 'Process' Target MUST contain at least one property.")
		# TypeError exception is not caught and passed upwards unaltered
