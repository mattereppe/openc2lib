from otupy.types.base import Enumerated

class ResponseType(Enumerated):
	""" OpenC2 Response-Type

		Enumerates the Response-Types according to Sec. 3.4.2.15.	
	"""	
	none=0
	ack=1
	status=2
	complete=3

