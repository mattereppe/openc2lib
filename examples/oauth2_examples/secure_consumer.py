#!/usr/bin/env python3
"""
Example to use the OpenC2 library with OAuth2 Resource Server protection

This example shows how to create a secure OpenC2 Consumer that validates
JWT tokens before processing commands, without modifying the original Consumer code.
"""

import logging
import sys
import os

import otupy as oc2
from otupy.auth.Resource.oauth2_consumer import create_oauth2_consumer

from otupy.encoders.json import JSONEncoder
from otupy.transfers.http import HTTPSTransfer, HTTPTransfer
from otupy.actuators.iptables_actuator import IptablesActuator
import otupy.profiles.slpf as slpf


# Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2')


def main():
    """Protect existing consumer instance"""

    # Create actuators
    actuators = {(slpf.nsid, 'iptables'): IptablesActuator()}

    # Create original consumer
    original_consumer = oc2.Consumer(
        "testconsumer",
        actuators,
        JSONEncoder(),
        HTTPTransfer("127.0.0.1", 8080)
    )

    logger.info("Original Consumer created, adding OAuth2 protection...")

    # Apply OAuth2 protection to existing consumer
    oauth2_consumer = create_oauth2_consumer(
        consumer=original_consumer,
        introspection_url="http://127.0.0.1:9000/oauth/introspect",
        required_scopes=["openc2:execute", "openc2:read"],  #non ci sono controlli qui
        client_id="sz64Qq9PxLRURl05TN5Ppj1b",
        client_secret="Zr6o8gmnuSNT3AAtvbeK1X6YAog0dXXJFGdpy6YfgSZhTpqS"
    )

    logger.info("OAuth2 protection applied successfully")
    logger.info("Starting protected OpenC2 Consumer...")

    # Run the protected consumer
    oauth2_consumer.run()


if __name__ == "__main__":

    logger.info(f"Starting secure OpenC2 Consumer example)")
    try:
        main()  #protect existing consumer
    except KeyboardInterrupt:
        logger.info("Shutting down secure OpenC2 Consumer...")
    except Exception as e:
        logger.error(f"Error running secure consumer: {e}")
        sys.exit(1)
