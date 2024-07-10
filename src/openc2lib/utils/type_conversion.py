""" Utils to convert types

	These utilis are meant to initialize openc2lib objects from basic types (e.g., strings).
	They may be useful to create openc2lib objects without explicit conversion for all fields.
"""

import enum

def convert_to(var, fieldtype):
	try:
		if issubclass(fieldtype, enum.Enum):
			return fieldtype[var]
		else:
			return fieldtype(var)
		
