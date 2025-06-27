from openc2lib.types.base import ArrayOf
from openc2lib.types.targets import File
from openc2lib.core.target import target
from openc2lib.profiles.rcli.profile import Profile  # Assuming this exists

@target(name='files', nsid=Profile.nsid)
class Files(ArrayOf(File)):
	""" OpenC2 files

		Implements the `files` target (Section 3.4.1.5).
		Just defines an `ArrayOf` `File`.
	"""

	def __init__(self, files=[]):
		super().__init__(files)
		self.validate(types=True, num_max=10)
