""" Formatting log messages

	This modules provides a formatter for the `logging` framework.
	
	The following generic format is provided:
	<datetime> [<level>] <modulename>: <message>
	where the <level> is colorized to give prominence to more critical messages. 
	All fields can be optionally omitted.

	This module requires 256-colors terminals.
"""

import logging
import datetime

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

	def __init__(self, datetime= True, name=True, datefmt=None):
		""" Set the custom format

			  Select which optional fields will be included.
			  :param datetime: Set to `False` to disable date/time indication.
			  :param name: Set to `False` to diable module name indication.
			  :param datefmt: Format the date according to this string. Takes common
			  		time.strftime specifiers, plus the '%t' which gives the timestamp.
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
		self.datefmt = datefmt

	def format(self, record):
		""" Color the record according to the log level """
		log_fmt = self.fmt.replace('COLOR', self.COLORS[record.levelno])
		self.fmt = self.fmt
		if self.datefmt:
			datefmt = self.datefmt.replace('%t', "{:.6f}".format((datetime.datetime.fromtimestamp(record.created)).timestamp()))
		else:
			datefmt = None
		# We are indeed inheriting from logging.Formatter, but looks like
		# there is no way to change the format string at runtime.
		formatter = logging.Formatter(log_fmt, datefmt, style='{')
		return formatter.format(record)

	def formatTime(record, datefmt=None):
		""" This function is invoked when (asctime) is used in the format string """
		if datefmt:
			datefmt.replace('%t', str(record.created))
		super().formatTime(record, datefmt)



