# Interface that defines the basic behavior of the Transfer Protocols 

class Transfer:

	def send(self, msg, encoder):
		pass

	def receive(self, callback, encoder):
		pass
