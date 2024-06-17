""" Dumb profile mockup

	This profile is just meant for testing and providing an example of how to create
	a new profile. It does not perform any useful action. The definition if very simple
	and does not include additional types or extensions (at least so far).
"""


from openc2lib import Profile, Profiles

from openc2lib.profiles.dumb.nsid import nsid
from openc2lib.profiles.dumb.profile import *

Profiles.add(nsid, dumb, 9999)

