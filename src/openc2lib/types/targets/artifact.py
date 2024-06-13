import dataclass

import openc2lib.types.base

class Artifact(openc2lib.types.base.Record):
	""" OpenC2 Artifact

		Implements the Artifact target (Section 3.4.1.1). 
		An array of bytes representing a file-like object or a link to that object.
	"""
	mime_type: str = None
	payload: Payload = None
	hashes: Hashes = None

	def __post_init__(self):
		if self.mime_type == None and self.payload == None and self.hashes == None:
			raise ValueError("An 'Artifact' Target MUST contain at least one property.")
