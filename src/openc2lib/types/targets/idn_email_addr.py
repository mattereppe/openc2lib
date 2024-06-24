from openc2lib.types.targets.email_addr import EmailAddr

class IDNEmailAddr(EmailAddr):
	""" OpenC2 IDNEmailAddr

		Implements the `idn_email_addr` target (Section 3.4.1.8). 
		A single internationalized email address.
	"""
		
	def set(self, email):
		""" Allows IDN email (RFC6531): there is a dedicated class for this (`IDNEmailAddr`). """
		emailinfo = email_validator.validate_email(email, check_deliverability=False,allow_smtputf8=True)
		self._emailaddr = emailinfo.normalized
