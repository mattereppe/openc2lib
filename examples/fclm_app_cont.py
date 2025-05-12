#!../.oc2-env/bin/python3
# Example to use the OpenC2 library
#
import logging
import sys
import time
import openc2lib as oc2
from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer
import openc2lib.profiles.fclm as fclm
#module 'openc2lib' has no attribute 'IPv4Addr'
from openc2lib.types.targets.ipv4_net import IPv4Net

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
file_handler = logging.FileHandler("controller_fclm_app_no_stop.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True, datefmt='%t'))
logger.addHandler(file_handler)

def main():
    logger.info("Creating Producer")
    p = oc2.Producer("producer2.example.net",
                     JSONEncoder(),
                     HTTPTransfer("127.0.0.1",
                                  8080))
    pf = fclm.Specifiers({"asset_id": "agent_x"})
    efs= oc2.ArrayOf(fclm.EF)() # type: ignore
    efs.append(fclm.EF("timestamp"))
    efs.append(fclm.EF("metadata"))
    a = fclm.Collector(address=IPv4Net("192.1.1.6"), port=oc2.Port(1234),format = fclm.FileFormat.json)
    col = oc2.ArrayOf(fclm.Collector)()
    col.append(a)
    arg = fclm.Args({
        #"start_time": oc2.DateTime(time.time() * 1000 + 5000),
        #"stop_time" :  oc2.DateTime(time.time() * 1000 + 10000),
        "log_exporter" : fclm.Exporter(storage=oc2.File({'path': '/var/log/filebeat/flows'}), collectors=col),
        "import_controls" : fclm.ImportOptions(scan_frequency=oc2.Duration(1000),max_backoff= oc2.Duration(10)),
        "export_fields" : efs
        })
    file = fclm.LogMonitor(oc2.File({"path": "/var/log/*.log"}))
    socket = fclm.LogMonitor(fclm.Socket("192.118.0.0",1000,oc2.L4Protocol.tcp))
    uri = fclm.LogMonitor(oc2.URI("wwww.google.com"))
    cmd = oc2.Command(oc2.Actions.start, file, arg, actuator=pf)
  
    logger.info("Sending "
    "command: %s", cmd)
    resp = p.sendcmd(cmd)
    logger.info("Got response: %s", resp)

if __name__ == '__main__':
    main()
