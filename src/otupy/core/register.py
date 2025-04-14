""" Object registration

	This module provides a registration mechanism to extend the elements provided by the 
	Language Specification with additional definitions from the Profiles.
"""

class Register(dict):
	""" List of registered elements
	
		This class registers all available elements, both provided by the otupy and by Profiles.
		The class is meant to be instantiated internally and filled in with the elements provided by 
		the Language Specification. Profiles may fill in with additional definitions, to make their 
		classes and names available to the core system for encoding/deconding purposes.
	"""
	
	def add(self, name: str, register, identifier=None):
		""" Add a new element
	
			Register a new element and make it available within the system. 
			
			This method throw an Exception if the element is already registered.

			:param name: The name used for the element.
			:param register: The class that defines the element.
			:param identifier: A numeric value associated to the standard by the Specification (unused).
			:return: None
		"""
		try:
			list(self.keys())[list(self.values()).index(register)]
		except ValueError:
			# The item is not in the list
			self[name] = register
			return
		raise ValueError("Element already registered")

	def get(self, name: str):
		""" Get element by name

			Throws an exception if the given name does not correspond to any registered element.

			:param name: The name of the element to return.
			:return: The class  corresponding to the given name.
		"""
		return self[name]

	def getName(self, register):
		""" Get the name of a element

			Given a class element, this method returns its name (the name it was registered with. 
			Note that the returned name include the namespace prefix.

			Throws an exception if the given element is not registered.

			:param register: The class element to look for.
			:return: A string with the name of the element.
		"""
		return list(self.keys())[list(self.values()).index(register)]
