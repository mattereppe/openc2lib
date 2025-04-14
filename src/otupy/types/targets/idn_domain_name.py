from otupy.types.data.idn_hostname import IDNHostname
from otupy.core.target import target

@target('idn_domain_name')
class IDNDomainName(IDNHostname):
	""" OpenC2 IDNDomainName

		Implements the `idn_domain_name` target (Section 3.4.1.7). 
		Internationalized Domain Name, [RFC5890], Section 2.3.2.3.
		The current requirements are equivalend to `IDNHostname`.
	"""
		
