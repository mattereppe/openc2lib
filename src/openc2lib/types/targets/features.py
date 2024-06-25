import openc2lib.types.base
from openc2lib.core.target import target

@target('features')
class Features(openc2lib.types.base.ArrayOf(openc2lib.types.data.Feature)):
	""" OpenC2 Features

		Implements the `features` target (Section 3.4.1.5).
		Just defines an `ArrayOf` `Feature`.
	"""
# TODO: implmement control on the max number of elements
	pass

