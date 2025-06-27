from openc2lib.types.base import ArrayOf
from openc2lib.profiles.rcli.data.process import Process
from openc2lib.core.target import target
from openc2lib.profiles.rcli.profile import Profile  # Assuming this exists

@target(name='processes', nsid=Profile.nsid)
class Processes(ArrayOf(Process)):
	""" OpenC2 processes

		Implements the `processes` target (Section 3.4.1.5).
		Just defines an `ArrayOf` `Feature`.
	"""

	def __init__(self, procs=[]):
		super().__init__(procs)
		self.validate(types=True, num_max=10)
