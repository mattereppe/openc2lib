import fqdn

class Hostname:
	""" A hostname that can be used to connect to this device over a network """
		
	def __init__(self, hostname):
		self.set(str(hostname))

	def set(self, hostname):
		""" Check hostname fullfils RFC 1123 requirements """
		if fqdn.FQDN(str(hostname), min_labels=1).is_valid:
			self._hostname = str(hostname)
		else:
			raise ValueError("Invalid hostname -- not compliant to RFC 1123")

	def get(self):
		""" Returns the hostname as string """
		return self._hostname

	def __str__(self):
		return self._hostname
