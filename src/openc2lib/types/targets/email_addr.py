import email_validator

from openc2lib.types.base import Record

class EmailAddr:
	""" OpenC2 Email Address

		Implements the `email_addr` target (Section 3.4.1.4). 
		Email address, [RFC5322], Section 3.4.1.
	"""

	def __init__(self, email):
		self.set(email)

	def set(self, email):
		emailinfo = email_validator.validate_email(email, check_deliverability=False)
		self._emailaddr = emailinfo.normalized

	def get(self):
		return self._emailaddr

	def __str__(self):
		return self._emailaddr
