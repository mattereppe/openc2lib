import random

def random_params(args):
	""" Generate random argument patterns

		For all possible number of arguments (1 to 6), this function creates random tuples by picking the corresponding number of arguments from the 
		list provided below.
		Running the test multiple times, will consist of different selections, but this is not much useful, since the parameters are 
		always the same.
	"""
	params = []
	for i in range(1, len(args)):
		param = {}
		for j in range(1,i+1):
			idx = random.randint(0,len(args)-1)
			k = list(args)[idx]
			v = args[list(args)[idx]]
			print("arg: ", k, v)
			print({k: v})
			param.update({k: v})
			print(param)
		params.append(param)
	return params
