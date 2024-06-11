import datetime 

class DateTime:
	""" OpenC2 Date-Time

		This is used to represents dates and times according to Sec. 3.4.2.2.
		 According to OpenC2 specification, this is the time in milliseconds from the epoch.
		Be careful that the `timedate` functions work with float timestamps expressed 
		in seconds from the epoch, hence conversion is needed.
	"""
	def __init__(self, timestamp=None):
		""" Initialize Date-Time
			
			The instance is initialized with the provided timestamp, or to the current time if no 
			argument is given. The timestamp is expressed in milliseconds
				from the epoch, according to the Language Specification.
			:param timestamp: The timestamp to initialize the instance.
		"""
		self.update(timestamp)

	def __str__(self):
		return str(self.time)

	def __int__(self):
		return self.time

	def update(self, timestamp=None):
		""" Change Date-Time

			Change the timestamp beard by the instance. The timestamp is expressed in milliseconds
			from the epoch. If no `timestamp` is given, sets to the current time.
			:param timestamp: The timestamp to initialize the instance.
		"""
		if timestamp == None:
			# datetime.timestamp() returns a float in seconds
			self.time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
		else:
			self.time = timestamp

	# RFC 7231       
	def httpdate(self, timestamp=None):
		""" Format  to HTTP headers

			Formats the timestamp according to the requirements of HTTP headers (RFC 7231).
			Use either the `timestamp`, if provided,  or the current time.
			:param timestamp: The timestamp to format, expressed in milliseconds from the epoch.
			:return RFC 7231 representation of the `timestamp`.
		"""
			
		if timestamp is None:
			timestamp = self.time

		return datetime.datetime.fromtimestamp(timestamp/1000).strftime('%a, %d %b %Y %H:%M:%S %Z')

