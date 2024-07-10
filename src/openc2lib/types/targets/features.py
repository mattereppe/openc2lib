from openc2lib.types.base import ArrayOf
from openc2lib.types.data import Feature
from openc2lib.core.target import target

@target('features')
class Features(ArrayOf(Feature)):
	""" OpenC2 Features

		Implements the `features` target (Section 3.4.1.5).
		Just defines an `ArrayOf` `Feature`.
	"""

	def __init__(self, feats=[]):
		super().__init__(feats)
		self.validate(types=True, num_max=10)

