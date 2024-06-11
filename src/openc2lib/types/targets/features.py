import openc2lib.types.base

class Features(openc2lib.types.base.ArrayOf(openc2lib.types.data.Feature)):
	""" OpenC2 Features

		Implements the Features target (Section 3.4.1.5).
		Just defines an `ArrayOf` `Feature`.
	"""
# TODO: implmement control on the max number of elements
	pass

