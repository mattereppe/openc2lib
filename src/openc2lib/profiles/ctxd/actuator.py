""" Context Discovery profile

	This modules contains the definition of the `ctxd` profile. It is mostly used as a container
	for the namespace identifier.
"""
import openc2lib as oc2

from openc2lib.profiles.ctxd.profile import Profile

""" CTXD Specifiers

	Define the set of specifiers defined in this specification that are meaningful in the context of CTXD.
	It implements the data structure define in the section "Actuator Specifiers"
"""
@oc2.actuator(nsid=Profile.nsid)
class Specifiers(oc2.Map):
	fieldtypes = dict(domain=str, asset_id=str)
	
	""" Specifiers for Actuator

		Fields that may be specified to select the specific Actuator implementation.

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

