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
from openc2lib.actuators.rcli.database.SQLDB import SQLDatabase
from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer

import openc2lib.profiles.rcli as rcli



# logging.basicConfig(filename='openc2.log',level=logging.DEBUG)
'''logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2producer')'''
logger = logging.getLogger()
# Ask for 4 levels of logging: INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.INFO)
# Create stdout handler for logging to the console 
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True))

hdls = [ stdout_handler ]
# Add both handlers to the logger
logger.addHandler(stdout_handler)
# Add file logger
file_handler = logging.FileHandler("controller_rcli_copy_artifact.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True, datefmt='%t'))
logger.addHandler(file_handler)

def main():
    logger.info("Creating Producer")
    p = oc2.Producer("producer.example.net",
                     JSONEncoder(),
                     HTTPTransfer("127.0.0.1",
                                  8080))

    pf = rcli.Specifiers({})

    arg = rcli.Args({
        "storage" : File({'path': 'tmacp/fcd/a', 'name': 'acxzcsxs.txt'}),
    })

    bcontent=b'My binary payssssload'
    uri = "https://www.w3.org/TR/png/iso_8859-1.txt"

    h = oc2.Hashes({'md5': oc2.Binaryx(hashlib.md5(bcontent).digest())})
    a = oc2.Artifact(
            mime_type='application/json', 
            payload=oc2.Payload(URI(uri)),
    	    #payload=oc2.Binary(bcontent),
            #hashes= h
            )

    cmd = oc2.Command(oc2.Actions.copy, a, arg, actuator=pf)


    logger.info("Sending command: %s", cmd)
    resp = p.sendcmd(cmd)
    logger.info("Got response: %s", resp)


if __name__ == '__main__':
    main()
