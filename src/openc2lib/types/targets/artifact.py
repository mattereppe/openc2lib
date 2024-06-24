import dataclasses

from openc2lib.types.base import Record
from openc2lib.types.data import Payload, Hashes

@dataclasses.dataclass
class Artifact(Record):
	""" OpenC2 Artifact

		Implements the `artifact` target (Section 3.4.1.1). 
		An array of bytes representing a file-like object or a link to that object.
	"""
	mime_type: str = None
	payload: Payload = None
	hashes: Hashes = None

	def __post_init__(self):
		if self.mime_type == None and self.payload == None and self.hashes == None:
			raise ValueError("An 'Artifact' Target MUST contain at least one property.")
