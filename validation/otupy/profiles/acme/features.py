from otupy import Map, ArrayOf, target, Enumerated

class Feature(Enumerated):
	""" OpenC2 Feature
	
	   An enumeration for the fields that can be included in the `Results` (see Sec. 3.4.2.4).
	"""
	versions   = 1
	profiles   = 2
	schema     = 100


class Features(ArrayOf(Feature)):
   def __init__(self, feats=[]):
      super().__init__(feats)
      self.validate(types=True, num_max=10)

@target(name='features', nsid='x-acme')
class AcmeFeatures(Map):
	fieldtypes = {'features': Features}

