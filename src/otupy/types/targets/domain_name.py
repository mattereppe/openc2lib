import fqdn

from otupy.core.target import target

@target('domain_name')
class DomainName:
	""" A hostname that can be used to connect to this device over a network 
		
		Same implementation as `Hostname`, but requires dotted-separated names.
	"""
		
	def __init__(self, domainname):
		self.set(domainname)

	def set(self, domainname):
		""" Check hostname fullfils RFC 1123 requirements """
		if fqdn.FQDN(domainname).is_valid:
			self._domainname = str(domainname)
		else:
			raise ValueError("Invalid hostname -- not compliant to RFC 1034")

	def get(self):
		""" Returns the hostname as string """
		return self._domainname

	def __str__(self):
		return self._domainname
