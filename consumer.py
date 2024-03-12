from openc2.encoder import Encoder
from openc2.transfer import Transfer

class Consumer:
	def __init__(self, encoder: Encoder = None, transfer: Transfer = None):
		self.encoder = encoder
		self.transfer = transfer

	def recv(self, encoder: Encoder = None, transfer: Transfer = None):
		if not encoder: encoder = self.encoder
		if not transfer: transfer = self.transfer
		if not transfer: raise ValueError('Missing transfer object')

		cmd = transfer.recv(encoder)
		return cmd
