#!/usr/bin/env python3

import logging
import sys

from otupy.encoders.json import JSONEncoder
from otupy.transfers.http import HTTPTransfer
import otupy as oc2
import otupy.profiles.slpf as slpf

from otupy.auth.Client.oauth2producer import OAuth2Producer

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2producer')


def main():
    """Create an OAuth2 Producer and send commands"""

    # OAuth2 configuration
    oauth2_config = {
        'client_id': 'FXEHY5cASqiO2a6TDVJQcR2X',
        'client_secret': 'zdZ6zawQaOINAhfNxlwhsyRFD5aREUFCkL2Bqxu77g5B82Xb',
        'redirect_uri': 'http://127.0.0.1:8000/callback',
        'consumer_url': 'http://127.0.0.1:8080',
        'callback_port': 8000
    }

    try:
        producer = OAuth2Producer(
            producer="producer.example.net",
            encoder=JSONEncoder(),
            transfer=HTTPTransfer("127.0.0.1", 8080),
            oauth2_config=oauth2_config,
        )

        actuator_profile = slpf.Specifiers({
            'hostname': 'firewall',
            'named_group': 'firewalls',
            'asset_id': 'iptables'
        })

        args = slpf.Args({'response_requested': oc2.ResponseType.complete})

        # Example command: query features
        cmd = oc2.Command(
            oc2.Actions.query,
            oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs]),
            args,
            actuator=actuator_profile
        )

        logger.info("Sending OpenC2 command: %s", cmd)

        response = producer.sendcmd(cmd)
        logger.info("Received OpenC2 response: %s", response)

        if producer.is_authenticated():
            logger.info("Producer successfully authenticated with OAuth2")
            token_info = producer.get_token_info()
            logger.info("Token info: %s", token_info)
        else:
            logger.warning("Producer not authenticated")

    except ValueError as ve:
        logger.error("Configuration error: %s", ve)
        sys.exit(1)
    except TimeoutError as te:
        logger.error("Authentication timeout: %s", te)
        sys.exit(1)
    except Exception as e:
        logger.error("Error while sending command: %s", e)
        import traceback
        logger.error("Full traceback: %s", traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    logger.info("Starting OpenC2 Producer with OAuth2...")
    logger.info("Sending Command...")

    try:
        main()
        logger.info("OpenC2 Producer completed successfully")
    except KeyboardInterrupt:
        logger.info("Producer interrupted by user")
        sys.exit(0)
    except Exception as ex:
        logger.error(f"Unhandled exception: {ex}")
        import traceback

        logger.error("Full traceback: %s", traceback.format_exc())
        sys.exit(1)