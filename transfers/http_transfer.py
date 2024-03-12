from openc2.transfer import Transfer

class HTTPTransfer(Transfer):
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def send(self, msg, encoder):
		pass

class HTTPSTransfer(Transfer):
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def send(self, msg, encoder):
		pass


