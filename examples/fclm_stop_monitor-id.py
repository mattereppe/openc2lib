#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#
import logging
import sys
import openc2lib as oc2
from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer
from openc2lib.profiles.fclm import MonitorID  

import openc2lib.profiles.fclm as fclm

# logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2producer')


def main():
    logger.info("Creating Producer")
    p = oc2.Producer("producer.example.net",
                     JSONEncoder(),
                     HTTPTransfer("127.0.0.1",
                                  8080))
    pf = fclm.Specifiers({'asset_id': 'agent_x'})
    arg = fclm.Args(
        {'response_requested': oc2.ResponseType.complete,
         }
        )
    cmd = oc2.Command(oc2.Actions.stop, MonitorID("Theta_7197KK"), arg, actuator=pf)
    logger.info("Sending command: %s", cmd)
    resp = p.sendcmd(cmd)
    logger.info("Got response: %s", resp)

if __name__ == '__main__':
    main()
