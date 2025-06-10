#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#
import hashlib
import logging
import sys
import time
import openc2lib as oc2
from openc2lib.types.data.uri import  URI
from openc2lib.types.targets.file import File
from openc2lib.profiles.rcli.targets.processes import Processes

from openc2lib.profiles.rcli.data.process import Process
from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer

import openc2lib.profiles.rcli as rcli

# logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2producer')


def main():
    logger.info("Creating Producer")
    p = oc2.Producer("producer.example.net",
                     JSONEncoder(),
                     HTTPTransfer("127.0.0.1",
                                  8080))
    # p = oc2.Producer("producer.example.net",
    #                  JSONEncoder(),
    #                  HTTPTransfer("127.0.0.1",
    #                               5000))


    pf = rcli.Specifiers({})
    arg = rcli.Args({'response_requested': oc2.ResponseType.complete})

    #arg = rcli.Args({"duration": oc2.Duration(3000)})

    processes = Processes()
    processes.append(Process(pid=21881))

    #processes.append(Process(pid = ))
    cmd = oc2.Command(oc2.Actions.stop, processes, arg, actuator=pf)


    logger.info("Sending command: %s", cmd)
    resp = p.sendcmd(cmd)
    logger.info("Got response: %s", resp)


if __name__ == '__main__':
    main()
