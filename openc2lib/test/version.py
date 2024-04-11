class Version(str):
	def __new__(cls, major, minor):
		vers = str(major) + '.' + str(minor)
		instance = super().__new__(cls, vers)
		return instance

	def __init__(self, major, minor):
		self.major = major
		self.minor = minor
	
