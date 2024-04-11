from openc2lib.encoder import Encoder
from openc2lib.transfer import Transfer
from openc2lib.message import Message

class Consumer:
	def __init__(self, consumer, encoder: Encoder = None, transfer: Transfer = None):
		self.consumer = consumer
		self.encoder = encoder
		self.transfer = transfer

	def recv(self, encoder: Encoder = None, transfer: Transfer = None):
		if not encoder: encoder = self.encoder
		if not transfer: transfer = self.transfer
		if not transfer: raise ValueError('Missing transfer object')

		cmd = transfer.recv(encoder)
		return cmd

	def reply(self, response, encoder: Encoder = None, transfer: Transfer = None):
		if not encoder: encoder = self.encoder
		if not transfer: transfer = self.transfer
		if not transfer: raise ValueError('Missing transfer object')

		msg = Message(response)
		msg.from_=self.consumer
		msg.to="ciccio"

		transfer.send(msg, encoder)

