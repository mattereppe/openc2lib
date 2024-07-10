
class Version(str):
	""" OpenC2 Version

		Version of the OpenC2 protocol (Sec. 3.4.2.16). Currently a *<major>.<minor>* format is used.
	"""
	def __new__(cls, major, minor=None):
		""" Create `Version` instance

			Create a Version instance from major and minor numbers, expressed as numbers.
			To not break the operation of the encoding/decoding modules, the major number can also be a 
			string or a Version. In such cases, the value of minor is ignored.

			:param major: Major number of OpenC2 version. Alternatively, a `str` or a `Version` object.
			:param minor: Minor number of OpenC2 version. Ignored if `major` is not an `int`.
			:return: `Version` instance.
		"""
		vers = str(major) 
		if isinstance(major, int):
			vers += '.' + str(minor)
		instance = super().__new__(cls, vers)
		return instance

	def __init__(self, major, minor=None):
		""" Initialize `Version` instance

			Initialize with major and minor numbers.
			:param major: Major number of OpenC2 version.
			:param minor: Minor number of OpenC2 version.
			:return: `Version` instance.
		"""
		if isinstance(major, int):
			self.major = major
			self.minor = minor
		else:
		 	self.major, self.minor = self.__split(major)

	@staticmethod
	def __split(vers):
		""" Split into major and minor numbers

			Assume vers is a string that must be split into major and minor numbers.
			:param vers: A `str` in the format '<major>.<minor>'.
			:return: A pair made of major and minor values.
		"""
		v = vers.split('.',2)
		return v[0], v[1]

	@staticmethod
	def fromstr(v):
		""" Create `Version` instance

			Create `Version` instance from string (in the *<major>.<minor>* notation.
			:param v: Text string with the Version.
			:return: `Version` instance.
		"""
		major, minor = Version.__split(v)
		return Version(int(major), int(minor))
	
	@classmethod
	def fromdict(cls, vers, e=None):
		""" Create `Version` instance

			Create `Version` instance from string (in the *<major>.<minor>* notation.
			This method is provided to deserialize an OpenC2 message according to the openc2lib approach.
			This method should only be used internally the openc2lib.
			:param vers: Text string with the Version.
			:param e: `Encoder` instance to be used (only included to be compliance with the function footprint).
			:return: `Version` instance.
		"""
		return Version.fromstr(vers)

