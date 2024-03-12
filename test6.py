import json

x = {"headers":{"request_id":"d1ac0489-ed51-4345-9175-f3078f30afe5","created":1545257700000,"from":"oc2producer.company.net","to":["oc2consumer.company.net"]},"body":{"openc2":{"request":{"action":"...","target":"...","args":"..."}}}}

class Target:
	def __init__(self):
		self.target = "iptables"

class Test:
	def __init__(self):
		self.cmd = "scan"
		self.target = Target()

	def __iter__(self):
		for key in self.__dict__:
			yield key, getattr(self, key)
	
class MyEncoder(json.JSONEncoder):
	def default(self, o):
		d = {'cmd': o.cmd}
		print(type(d))
		return d

t = Test()
print(json.dumps(t, cls=MyEncoder))

def todict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey)) 
            for key, value in obj.__dict__.items() 
            if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    elif isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S%z")
    else:
        return obj
