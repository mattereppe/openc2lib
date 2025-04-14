""" HTTP Transfer Protocol

	This module defines implementation of the `Transfer` interface for the 
  	HTTP/HTTPs protocols. This implementation is mostly provided for 
	research and development purposes, but it is not suitable for production
	environments.

	The implementation follows the Specification for Transfer of OpenC2 Messages via HTTPS
	Version 1.1, which is indicated as the "Specification" in the following.

	This modules provides the following classes:
	- `HTTPTransfer` which implements the `Transfer` interface for the HTTP protocol;
	- `HTTPSTransfer` which implements the `Transfer` interface for the HTTP protocol over TLS.
"""

from otupy.transfers.http.http_transfer import HTTPTransfer, HTTPSTransfer
