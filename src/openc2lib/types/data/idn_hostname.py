import idna

class IDNHostname:
	""" A hostname that can be used to connect to this device over a network 
		
		WARNING: This class has never been tested.
	"""
		
	def __init__(self, hostname):
		self.set(str(hostname))

	def set(self, hostname):
		""" Check hostname fullfils RFC 1123 requirements """
		try: 
			idna.encode(hostname)
			self._hostname = str(hostname)
		except:
			raise ValueError("Invalid hostname -- not compliant to RFC 5891")

	def get(self):
		""" Returns the hostname as string """
		return self._hostname

	def __str__(self):
		return self._hostname
