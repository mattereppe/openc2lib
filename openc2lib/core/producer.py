from openc2lib.core.message import Command, Message
from openc2lib.core.encoder import Encoder
from openc2lib.core.transfer import Transfer

class Producer:
	def __init__(self, producer, encoder=None, transfer=None):
		if not isinstance(producer, str):
			raise TypeError('Only strings are allowed for producer identifier')
		self.producer = producer
		self.encoder = encoder
		self.transfer = transfer

	def sendcmd(self, cmd: Command, encoder: Encoder =None, transfer: Transfer =None, consumers: [] =None):
		if not encoder: encoder = self.encoder
		if not transfer: transfer = self.transfer
		if not transfer: raise ValueError('Missing transfer object')
		if not encoder: raise ValueError('Missing encoder object')
		
		msg = Message(cmd)
		msg.from_=self.producer
		msg.to=consumers

		return transfer.send(msg, encoder)



