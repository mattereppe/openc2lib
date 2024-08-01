""" StateLess Packet Filter profile

	This modules contains the definition of the `slpf` profile. It is mostly used as a container
	for the namespace identifier.
"""
import openc2lib as oc2

from openc2lib.profiles.slpf.profile import Profile

""" SLPF Specifiers

	Define the set of specifiers defined in this specification that are meaningful in the context of SLPF.
	It implements the data structure define in Sec. 2.1.4.
"""
@oc2.actuator(nsid=Profile.nsid)
class Specifiers(oc2.Map):
	fieldtypes = dict(hostname=str, named_group=str, asset_id=str, asset_tuple = [str])
	""" Specifiers for Actuator

		Fields that may be specified to select the specific Actuator implementation.
		Usage of these fields is described by the SLPF Specification (Sec. 2.1.4), but their actual
		meaning and usage is up the the `Actuator` implementation.

		The extension mechanism is described in the 
		[Developing extensions](https://github.com/mattereppe/openc2lib/blob/main/docs/developingextensions.md#developing-extensions) Section of the main documentation.

		:param hostname: [RFC1123] hostname (can be a domain name or IP address) 
			for a particular device with SLPF functionality.
		:param named_group: User defined collection of devices with SLPF functionality.
		:param asset_id: Unique identifier for a particular SLPF.
		:param asset_tuple: Unique tuple identifier for a particular SLPF consisting 
			of a list of up to 10 strings. Not clear the definition and its usage.
	"""

	def __init__(self, dic):
		""" Initialize the `Actuator` profile

			The profile can be initialized by passing the internal fields explicitely 
			(i.e., by giving them as ***key=value*** pair.
			:param dic: A list of ***key=value*** pair which allowed values are given
				by `fieldtype`.
		"""
		self.nsid = Profile.nsid
		oc2.Map.__init__(self, dic)
	
	def __str__(self):
		id = self.nsid + '('
		for k,v in self.items():
			id += str(k) + ':' + str(v) + ','
		id = id.strip(',')
		id += ')'
		return id

