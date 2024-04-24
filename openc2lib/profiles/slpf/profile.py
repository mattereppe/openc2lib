from openc2lib.profile import Profile
from openc2lib.basetypes import Map
from openc2lib.datatypes import Nsid

class slpf(Profile, Map):
	fieldtypes = dict(hostname=str, named_group=str, asset_id=str, asset_tuple = [str])

	def __init__(self, dic):
		Profile.__init__(self, 'slpf')
		Map.__init__(self, dic)
	
	def __str__(self):
		id = self.nsid + '('
		for k,v in self.items():
			id += str(k) + ':' + str(v) + ','
		id = id.strip(',')
		id += ')'
		return id

	@classmethod
	def validate_cmd(cmd):
		pass
