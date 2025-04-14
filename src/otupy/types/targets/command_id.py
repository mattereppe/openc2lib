import re

from otupy.types.base import Record
from otupy.core.target import target

@target('command')
class CommandID:
	""" OpenC2 Command-ID

		Implements the `command` target (Section 3.4.2.16). 
		A reference to a previously issued Command.
		A valid Command-ID shall not contain spaces.
	"""

	def __init__(self, cmdid):
		self.set(cmdid)

	def set(self, cmdid):
		""" Sets the value """
		if re.search("^\S{0,36}$",cmdid) is None:
			raise ValueError("Invalid Command-ID")
		self._cmdid = cmdid

	def get(cmdid):
		""" Returns the value """
		return self._cmdid

	def __str__(self):
		return self._cmdid
