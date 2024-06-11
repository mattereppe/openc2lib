
class Version(str):
	""" OpenC2 Version

		Version of the OpenC2 protocol (Sec. 3.4.2.16). Currently a *<major>.<minor>* format is used.
	"""
	def __new__(cls, major, minor):
		""" Create `Version` instance

			Create a Version instance from major and minor numbers, expressed as numbers.
			:param major: Major number of OpenC2 version.
			:param minor: Minor number of OpenC2 version.
			:return: `Version` instance.
		"""
		vers = str(major) + '.' + str(minor)
		instance = super().__new__(cls, vers)
		return instance

	def __init__(self, major, minor):
		""" Initialize `Version` instance

			Initialize with major and minor numbers.
			:param major: Major number of OpenC2 version.
			:param minor: Minor number of OpenC2 version.
			:return: `Version` instance.
		"""
		self.major = major
		self.minor = minor

	@staticmethod
	def fromstr(v):
		""" Create `Version` instance

			Create `Version` instance from string (in the *<major>.<minor>* notation.
			:param v: Text string with the Version.
			:return: `Version` instance.
		"""
		vers = v.split('.',2)
		return Version(vers[0], vers[1])
	
	@classmethod
	def fromdict(cls, vers, e=None):
		""" Create `Version` instance

			Create `Version` instance from string (in the *<major>.<minor>* notation.
			This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
			This method should only be used internally the openc2lib.
			:param vers: Text string with the Version.
			:param e: `Encoder` instance to be used (only included to be compliance with the function footprint.
			:return: `Version` instance.
		"""
		return Version.fromstr(vers)

