# Interface that defines the basic behavior of the Transfer Protocols 

class Transfer:

	def send(self, msg, encoder):
		enc = encoder.encode(msg)

	def recv(self, msg, encoder):
		return encoder.decode(msg)

