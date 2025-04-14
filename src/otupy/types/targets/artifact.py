from otupy.types.base import Record
from otupy.types.data import Payload, Hashes
from otupy.core.target import target
from otupy.utils.media_types import MediaTypes

@target('artifact')
class Artifact(Record):
	""" OpenC2 Artifact

		Implements the `artifact` target (Section 3.4.1.1). 
		An array of bytes representing a file-like object or a link to that object.

		Mime types, if used, may be validated for valid syntax or registered types in IANA. Both
		options are disabled by default, but can be enabled by setting the `validate_syntax` and
		`validate_iana` options, respectively. Mind that IANA registry validation needs to
		download the updated IANA registry, hence this option may take some time the first time
		it is used. Validation is enabled at the class level, so once enabled, it applies to all
		objects. Validation, if enabled, is automatically applied when instantiating an object,
		but can also be explicitly invoked at a later stage.
	"""
	mime_type: str = None
	""" Permitted values specified in the IANA Media Types registry, [RFC6838] """
	payload: Payload = None
	""" Choice of literal content or URL """
	hashes: Hashes = None
	""" Hashes of the payload content """

	validate_syntax: bool = False
	""" Validate the syntax of mime_type according to IANA media types rules """
	validate_iana: bool = False
	""" Validate the mime_type value is present in the IANA Media Types registry """

	def __init__(self, mime_type = None, payload = None, hashes = None):
		""" Initialize Artifact

			Initializes an Artifact and optionally performs validation on valid mime_types. Validation can include both 
			basic syntax validation as well as verification that the mime_type is registered in the IANA Media Types register.
			:param mime_type: Media Type
			:param payload: Payload
			:param hashes: Hashes value
			:param syntax_validation: Enable validation of media type syntax (Default: False).
			:param iana_validation: Check if the media type is registered in the IANA registry (Default: False)
		"""
		self.mime_type = mime_type if mime_type is not None else None
		self.payload = Payload(payload) if payload is not None else None
		self.hashes = Hashes(hashes) if hashes is not None else None

		self.validate()
			

	def validate(self):
		""" Validate this instance 

			Validation includes two options: validate the syntax and validate the presence of the media type in the IANA
			registry. Both these options are optional, and must be enabled explicitely by setting the `validate_syntax`
			and `validate_iana` class attributes.

			Validation also ensures the object includes at least one field, as required by the Specification.
			:return: True, if the fields are compliant to the Specification (according to selected validation options).
		"""

		if self.mime_type is not None and MediaTypes.validate(self.mime_type, self.validate_syntax, self.validate_iana) is False:
		# MediaTypes.validation return an exception if the syntax is not correct, so it returns False only when 
		# the mime_type is not found in the registry
			raise ValueError("Invalid mime_type")

		if self.mime_type == None and self.payload == None and self.hashes == None:
			raise ValueError("An 'Artifact' Target MUST contain at least one property.")
