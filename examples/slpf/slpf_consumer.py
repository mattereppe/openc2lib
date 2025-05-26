import json
import logging
import os
import sys
import subprocess

import openc2lib as oc2

from openc2lib.encoders.json import JSONEncoder
from openc2lib.transfers.http import HTTPTransfer
from openc2lib.actuators.slpf.slpf_actuator import SLPFActuator
from openc2lib.actuators.slpf.slpf_actuator_iptables import SLPFActuator_iptables
#from openc2lib.actuators.ctxd.ctxd_actuator_kubernetes import CTXDActuator_kubernetes
import openc2lib.profiles.slpf as slpf

# Declare the logger name
logger = logging.getLogger()
# Ask for 4 levels of logging: INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.INFO)
# Create stdout handler for logging to the console 
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True))
# Add both handlers to the logger
logger.addHandler(stdout_handler)
# Add file logger
file_handler = logging.FileHandler("server.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(oc2.LogFormatter(datetime=True,name=True, datefmt='%t'))
logger.addHandler(file_handler)

def main():
    try:
        #read the configuration file
        configuration_file = os.path.dirname(os.path.abspath(__file__))+"/configuration.json"
        with open(configuration_file, 'r') as file:
            configuration_parameters = json.load(file)
        
        #process = subprocess.Popen('source ./matteo-astrid.rc', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #stdout, stderr = process.communicate()

        actuators = {}
        for element in configuration_parameters['slpf_actuators']:
            if (element["type"] == "iptables"):
                #CTXDActuator_openstack is able to find vm connected to the cloud service openstack
                actuators[(slpf.Profile.nsid,element['asset_id'])] = SLPFActuator_iptables(
                      hostname = element['hostname'],
                      named_group = element['named_group'],
                      asset_id = element['asset_id'],
                      asset_tuple = element['asset_tuple'],
                      db_name = element['db_name'],
                      db_path = element['db_path'],
                      db_commands_table_name = element['db_commands_table_name'],
                      db_jobs_table_name = element['db_jobs_table_name'],
                      iptables_rules_path = element['iptables_rules_path'],
                      iptables_rules_v4_filename = element['iptables_rules_v4_filename'],
                      iptables_rules_v6_filename = element['iptables_rules_v6_filename'],
                      iptables_input_chain_name = element['iptables_input_chain_name'],
                      iptables_output_chain_name = element['iptables_output_chain_name'],
                      iptables_forward_chain_name = element['iptables_forward_chain_name'],
                      iptables_cmd = element['iptables_cmd'],
                      ip6tables_cmd = element['ip6tables_cmd'],
                      misfire_grace_time = element["misfire_grace_time"]
                )
            else:
                raise Exception("type must be equal to iptables")

        #-----------------------RUN THE CONSUMER with multiple actuators-----------------------------------------
        c = oc2.Consumer("testconsumer", actuators, JSONEncoder(), HTTPTransfer(configuration_parameters['consumer']['ip'],
                                                                                configuration_parameters['consumer']['port'],
                                                                                configuration_parameters['consumer']['endpoint']))
        c.run()  

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()