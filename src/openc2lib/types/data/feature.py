from openc2lib.types.base import Enumerated

class Feature(Enumerated):
	""" OpenC2 Feature

		An enumeration for the fields that can be included in the `Results` (see Sec. 3.4.2.4).
	"""
	versions   = 1
	profiles   = 2
	pairs      = 3
	rate_limit = 4

