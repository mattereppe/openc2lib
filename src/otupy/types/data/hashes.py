from otupy.types.base import Map, Binaryx

class Hashes(Map):
	""" Hashes values """
	fieldtypes = {'md5': Binaryx, 'sha1': Binaryx, 'sha256': Binaryx }

	def __init__(self, hashes):
		super().__init__(hashes)
		self.validate_fields()

		for k, v in hashes.items():
			if k == 'md5' and v is not None and len(v) != 16:
				raise ValueError("Invalid MD5 length")
			if k == 'sha1' and v is not None and len(v) != 20:
				raise ValueError("Invalid SHA1 length")
			if k == 'sha256' and v is not None and len(v) != 32:
				raise ValueError("Invalid SHA256 length")
			
			
			
