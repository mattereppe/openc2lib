""" OpenC2 data types

	Definition of the data types in the OpenC2 DataModels (Sec. 3.4.2).
	The naming strictly follows the definition of the Language Specification
	as close as possible. The relevant exception is represented by hyphens
	that are always dropped.
"""

import aenum
import dataclasses


from openc2lib.types.data.ipv4_addr import IPv4Addr
from openc2lib.types.data.l4_protocol import L4Protocol
from openc2lib.types.data.datetime import DateTime
from openc2lib.types.data.duration import Duration
from openc2lib.types.data.version import Version
from openc2lib.types.data.feature import Feature
from openc2lib.types.data.nsid import Nsid
from openc2lib.types.data.response_type import ResponseType
from openc2lib.types.data.target_enum import TargetEnum
from openc2lib.types.data.action_targets import ActionTargets
from openc2lib.types.data.action_arguments import ActionArguments
from openc2lib.types.data.payload import Payload
from openc2lib.types.data.hashes import Hashes
from openc2lib.types.data.uri import URI
from openc2lib.types.data.hostname import Hostname
from openc2lib.types.data.idn_hostname import IDNHostname

import openc2lib.types.data.mime_types
		
