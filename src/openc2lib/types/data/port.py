class Port(int):
	""" L4 port number

		Defines a port number to be used to identify network services.
		Only requires the number to be in the 0-65535 range, without
		any additional control.
	"""

	def __init__(self, port):
		""" Instantiate a port

			:param port: The port number. Must be a valid number between 0 and 65535.
		"""
		if 0 <= port <= 65535:
			self._port = int(port)
		else:
			raise ValueError("Invalid port number")


