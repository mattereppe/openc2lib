import uuid
import openc2

class UuidProperty(openc2.properties.Property):
	def __init__(self, **kwargs):
		super(UuidProperty, self).__init__(**kwargs)

	def clean(self, value):
		if isinstance(value, uuid.UUID):
			u= value
		if isinstance(value, str):
			u = uuid.UUID(hex=value)
		if isinstance(value, bytes):
			u = uuid.UUID(bytes=value)
		if isinstance(value, int):
			u = uuid.UUID(int=value)
		if isinstance(value, tuple):
			u = uuid.UUID(fields=value)

		return str(u)

		# The following code is only intended to demonstrate that the clean()
		# method is indeed used for serialization, and it must return anything
		# can be managed by JsonEncoder. If a dictionary is returned as a 'clean'
		# value, the UuidProperty must be ready to accept it as valid input.
#		if isinstance(value, dict):
#			u = value['myfield']
#
#		print("value: ", value)
#		print("u: ", u)
#		serialized = str(u)
#		print("Serialized: ", serialized)
#		dic =  {'myfield': serialized}
#		print("Dictionary: ", dic)
#		return dic


@openc2.properties.CustomProperty(
    "x-acme",
    [
        ("firewall_status", openc2.properties.StringProperty()),
#("container_id", openc2.properties.StringProperty()),
        ("container_id", UuidProperty()),
#        ("features", openc2.properties.EnumProperty(allowed=["versions", "profiles", "schema"])),
        ("features", openc2.properties.ListProperty(
					openc2.properties.EnumProperty(
						allowed=["versions", "profiles", "schema"]))),
    ],
)
class AcmeProperty(object):
    pass

