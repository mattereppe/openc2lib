from typing import Self

from openc2lib.types.base import Map
from openc2lib.types.targets import File

class Process(Map):
	""" OpenC2 Process

		Implements the `process` target (Section 3.4.1.15). 
		Common properties of an instance of a computer program as executed on an operating system.

	"""
	fields = {'pid': int, 'name': str, 'cwd': str, 'executable': File, 'parent': Self, 'command_line': str}
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

	def __init__(self, process: dict):
		super().__init__(process)
		# Explicit control on each field is carried out to manage the possibility of wrong
		# inputs or inputs defined by extensions
		for x in self.keys():
			if x in self.fields:
				return
		raise ValueError("A 'Process' Target MUST contain at least one property.")
