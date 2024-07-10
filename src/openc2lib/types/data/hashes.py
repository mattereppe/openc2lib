from openc2lib.types.base import Map, Binaryx

class Hashes(Map):
	""" Hashes values """
	fieldtypes = {'md5': Binaryx, 'sha1': Binaryx, 'sha256': Binaryx }

	def __init__(self, hashes):
		super().__init__(hashes)
		self.validate_fields()
