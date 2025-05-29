import macaddress

from otupy.core.target import target

@target('mac_addr')
class MACAddr:
	""" OpenC2 MACAddr

		Implements the `mac_addr`` target (Section 3.4.1.14). 
		Media Access Control / Extended Unique Identifier address - EUI- 48 or EUI-64.
		The text representation of a MAC Address in colon hexadecimal format.
	"""

	def __init__(self, eui):
		""" Raises an error if `eui` is not EUI48 or EUI64 """
		self.set(eui)
	
	def set(self, eui):
		""" Instantiates an EUI48/EUI64 address.
	
			Raises an error if `eui` is not EUI48 or EUI64.
  			Takes as input a string, a binary, or an integer.
		"""
		self.__eui = macaddress.parse(eui, macaddress.EUI48, macaddress.EUI64)

	def get(self):
		""" Returns colon hexadeciaml format """
		return str(self.__eui).replace('-',':')

	def __str__(self):
		return str(self.__eui).replace('-',':')
