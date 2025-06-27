#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#
import logging
import sys
import openc2lib as oc2
from openc2lib.types.data.feature import Feature
from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer

import openc2lib.profiles.fclm as fclm
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2producer')


def main():
    Feature.extend("export_fields",11)
    Feature.extend("exports_config",12)
    Feature.extend("imports_config",13)
    Feature.extend("import_controls",14)
    logger.info("Creating Producer")
    p = oc2.Producer("producer.example.net",
                     JSONEncoder(),
                     HTTPTransfer("127.0.0.1",
                                  8080))

    arg = fclm.Args({'response_requested': oc2.ResponseType.complete})
    pf = fclm.Specifiers({"asset_id" : "agent_x"})

    cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.export_fields,oc2.Feature.exports_config,oc2.Feature.import_controls,oc2.Feature.imports_config]), arg, actuator=pf)

    logger.info("Sending command: %s", cmd)
    resp = p.sendcmd(cmd)
    logger.info("Got response: %s", resp)



if __name__ == '__main__':
    main()
