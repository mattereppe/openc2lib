import openc2lib as oc2

from openc2lib.profiles.ctxd.profile import Profile #TO DO!
from openc2lib.types.base.array_of import ArrayOf
from openc2lib.profiles.ctxd.data.name import Name
from openc2lib.core.target import target

@oc2.target(name='context', nsid=Profile.nsid)
class Context(oc2.types.base.Record):
	"""Context
    It describes the service environment, its connections and security capabilities.
	"""
	services: ArrayOf(Name) = None # type: ignore
	""" List the service names that the command refers to """
	links: ArrayOf(Name) = None # type: ignore
	""" List the link names that the command refers to """



	def __init__(self, services = None, links = None):
		self.services = ArrayOf(Name)(services) if services is not None else None
		self.links = ArrayOf(Name)(links) if links is not None else None


	def __repr__(self):
		return (f"Context(services={self.services}, links={self.links})")
	
	def __str__(self):
		return f"Context(" \
	            f"services={self.services}, " \
	            f"links={self.links})"
