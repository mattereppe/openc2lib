import email_validator

from otupy.types.base import Record
from otupy.core.target import target

@target('email_addr')
class EmailAddr:
	""" OpenC2 Email Address

		Implements the `email_addr` target (Section 3.4.1.4). 
		Email address, [RFC5322], Section 3.4.1.
	"""

	def __init__(self, email):
		self.set(email)

	def set(self, email):
		""" Doesn't allow IDN email (RFC6531): there is a dedicated class for this (`IDNEmailAddr`). """
		emailinfo = email_validator.validate_email(email, check_deliverability=False,allow_smtputf8=False)
		self._emailaddr = emailinfo.normalized

	def get(self):
		return self._emailaddr

	def __str__(self):
		return self._emailaddr
