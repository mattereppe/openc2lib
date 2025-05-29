
class Duration(int):
	""" OpenC2 Duration

		 A time (positive number) expressed in milliseconds (Sec. 3.4.2.3).
	""" 
	def __init__(self, dur):
		""" Initialization

			Initialize to `dur` if greater or equal to zero, raise an exception if negative.
		"""
		if int(dur) < 0:
			raise ValueError("Duration must be a positive number")
		self=int(dur)

