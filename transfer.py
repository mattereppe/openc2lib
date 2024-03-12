import openc2.encoder

class Transfer:

	def send(self, msg, encoder):
		enc = encoder.encode(msg)

		print(enc)

	def recv(self, msg, encoder):
		return encoder.decode(msg)

