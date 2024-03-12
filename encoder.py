

class Encoder:
	@classmethod
	def encode(cls, obj):
		pass

	@staticmethod
	def todict(obj):
		dic = {}
		dic = obj.__dict__

		# Remove unassigned elements
		delete = []
		for k,v in dic.items(): 
			if v is None: delete.append(k)	
		for k in delete:
			del dic[k]

		# Convert complex types to string by interatively invoking the todict function


		return dic

from openc2.message import *
cmd = Command(Scan(), IPv4Net("130.251.17.0/24"))
Encoder.todict(cmd)

