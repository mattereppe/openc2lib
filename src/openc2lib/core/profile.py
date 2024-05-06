class Profile:
	def __init__(self, nsid):
		self.nsid = nsid

	def __str__(self):
		return self.nsid

class ProfilesDict(dict):
	def add(self, name: str, profile, identifier ):
		if name in self:
			raise ValueError("Profile already registered")
		self[name] = profile
	
Profiles = ProfilesDict()

