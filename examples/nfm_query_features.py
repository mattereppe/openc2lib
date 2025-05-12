#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#
import logging
import sys
import openc2lib as oc2
from openc2lib.types.data.feature import Feature
from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer

import openc2lib.profiles.nfm as nfm

# logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2producer')


def main():
    Feature.extend("interfaces",5)
    Feature.extend("information_elements",6)
    Feature.extend("exports",7)
    Feature.extend("export_options",8)
    Feature.extend("flow_format",9)
    Feature.extend("filters",10)
    logger.info("Creating Producer")
    p = oc2.Producer("producer.example.net",
                     JSONEncoder(),
                     HTTPTransfer("127.0.0.1",
                                  8080))

    arg = nfm.Args({'response_requested': oc2.ResponseType.complete})
    pf = nfm.Specifiers({"asset_id" : "probe_x"})

    cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.information_elements,oc2.Feature.exports,oc2.Feature.interfaces]), arg, actuator=pf)

    logger.info("Sending command: %s", cmd)
    resp = p.sendcmd(cmd)
    logger.info("Got response: %s", resp)



if __name__ == '__main__':
    main()
