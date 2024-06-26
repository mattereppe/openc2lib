""" Formatting log messages

	This modules provides a formatter for the `logging` framework.
	
	The following generic format is provided:
	<datetime> [<level>] <modulename>: <message>
	where the <level> is colorized to give prominence to more critical messages. 
	All fields can be optionally omitted.

	This module requires 256-colors terminals.
"""

import logging

class LogFormatter(logging.Formatter):
	""" Colored logging formatter

		The colormap is fixed, but the user can select which fields to include:
		- datetime: date and time of the log
		- module name: the name of the module that generated the log
		The level and message are always included and cannot be omitted.
	"""

	grey = '\x1b[38;21m'
	green = '\x1b[38;5;42m'
	blue = '\x1b[38;5;39m'
	yellow = '\x1b[38;5;226m'
	red = '\x1b[38;5;196m'
	highlight_red = '\x1b[37;1m\x1b[41m'
	reset = '\x1b[0m'

	def __init__(self, datetime= True, name=True):
		""" Set the custom format

			  Select which optional fields will be included.
			  :param datetime: Set to `False` to disable date/time indication.
			  :param name: Set to `False` to diable module name indication.
		"""
		super().__init__()
		if datetime:
			self.fmt = "{asctime:s} [COLOR{levelname:^8s}" + self.reset + "]"
		else:
			self.fmt = "COLOR{levelname:8s}" + self.reset + ":"
		if name:
			self.fmt += "{name:s}:"
		self.fmt += " {message:s}"

		self.COLORS = {
		    logging.DEBUG: self.grey,
		    logging.INFO: self.green,
		    logging.WARNING: self.yellow,
		    logging.ERROR: self.red,
		    logging.CRITICAL: self.highlight_red
		}

	def format(self, record):
		""" Color the record according to the log level """
		log_fmt = self.fmt.replace('COLOR', self.COLORS[record.levelno])
		formatter = logging.Formatter(log_fmt, style='{')
		return formatter.format(record)

