
import mediatype
import requests
import re
import xml.etree.ElementTree as ET

iana_registry_url = "https://www.iana.org/assignments/media-types/media-types.xml"
""" The URL of the XML description of the IANA registry for Media Type """

class MediaTypes:
	""" Media type parsing and validation

		This class extends the `mediatype` package with validation of Media Types.
		You can get the map of valid types from the `types_map` attribute, once a first `update_iana_registry()` is performed.
	"""
	types_map = []
	""" The map of media types found in the IANA registry """

	@classmethod
	def update_iana_registry(cls):
		mt_req = requests.get(iana_registry_url)
		mt_file = mt_req.text

		root = ET.fromstring(mt_file)
		ns = re.match(r'\{.*\}', root.tag).group(0)
		for reg in root.findall(ns+'registry'):
			for rec in reg.findall(ns+'record'):
				for file in rec.findall(ns+'file'):
					cls.types_map.append(file.text)


	@classmethod
	def validate(cls, name, syntax=True, iana_registry=True):
		""" Validates Media Type

			This method can validate both syntax and iana registration of media types. Media types are cached 
			for improving performance, but they can be updated at any time through the `registry_update` 
			method.
			
			Note that if both validation options (`syntax` and `iana_registry`) are set to `False`, this method
			always returns `True`.

			:param name: The name to be validated as media type.
			:param syntax: Check the name as a valid media type syntax (Default to `True`).
			:param iana_registry: Check the name is registered in the IANA Media Type registry (Default to `True`).
			:return: True in case the name is valid according to the specific options (`syntax` and `iana_registry`).
		"""
		if not cls.types_map:
			cls.update_iana_registry()

		if syntax is True:
			mediatype.parse(name)
		
		if iana_registry is True:
			return name in cls.types_map

		return True
