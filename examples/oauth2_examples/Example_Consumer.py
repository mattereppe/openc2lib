#!/usr/bin/env python3
"""
Example to use the OpenC2 library with OAuth2 Resource Server protection

This example shows how to create a secure OpenC2 Consumer that validates
JWT tokens before processing commands, using the OAuth2Consumer class
that extends the original Consumer interface.
"""

import logging
import sys

from otupy.auth.Resource.oauth2consumer import OAuth2Consumer

from otupy.encoders.json import JSONEncoder
from otupy.transfers.http import HTTPTransfer
from otupy.actuators.iptables_actuator import IptablesActuator
import otupy.profiles.slpf as slpf

# Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2')


def main():
    """Create and run an OAuth2-protected OpenC2 Consumer"""

    actuators = {(slpf.nsid, 'iptables'): IptablesActuator()}

    consumer = OAuth2Consumer(
        consumer="testconsumer",
        introspection_url="http://127.0.0.1:9000/oauth/introspect",
        client_id="sz64Qq9PxLRURl05TN5Ppj1b",
        client_secret="Zr6o8gmnuSNT3AAtvbeK1X6YAog0dXXJFGdpy6YfgSZhTpqS",
        actuators=actuators,
        encoder=JSONEncoder(),
        transfer=HTTPTransfer("127.0.0.1", 8080),
        ua_url='http://127.0.0.1:7000'
    )

    logger.info("OAuth2Consumer initialized successfully")
    logger.info("Running secure OpenC2 Consumer...")

    consumer.run()


if __name__ == "__main__":
    logger.info("Starting secure OpenC2 Consumer example")
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Shutting down secure OpenC2 Consumer...")
    except Exception as e:
        logger.error(f"Error running secure consumer: {e}")
        sys.exit(1)
