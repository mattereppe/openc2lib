import logging
import subprocess
import os
import hashlib

from openc2lib.actuators.slpf.slpf_actuator import SLPFActuator

from openc2lib import Version, Actions, IPv4Net, IPv4Connection , IPv6Net, IPv6Connection, L4Protocol, Binaryx
from openc2lib.profiles.slpf.args import Direction
from openc2lib.profiles.slpf.data import DropProcess

logger = logging.getLogger(__name__)

OPENC2VERS=Version(1,0)
""" Supported OpenC2 Version """

MY_IDS = {'hostname': None,
            'named_group': None,
            'asset_id': None,
            'asset_tuple': None }

class SLPFActuator_iptables(SLPFActuator):

    def __init__(self, hostname, named_group, asset_id, asset_tuple, iptables_rules_path, iptables_rules_v4_filename, iptables_rules_v6_filename, db_name, db_path, db_commands_table_name, db_jobs_table_name, misfire_grace_time):

        MY_IDS['hostname'] = hostname
        MY_IDS['named_group'] = named_group
        MY_IDS['asset_id'] = asset_id
        MY_IDS['asset_tuple'] = asset_tuple
        
        try:
            self.iptables_rules_path = iptables_rules_path if iptables_rules_path else os.path.dirname(os.path.abspath(__file__))
            if not os.path.exists(self.iptables_rules_path):
                raise

            self.iptables_rules_v4_filename = iptables_rules_v4_filename if iptables_rules_v4_filename else "iptables_rules.v4"
            if not os.path.exists(os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename)):
                with open(os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename), "w") as file:
                    file.write("")
                    
            self.iptables_rules_v6_filename = iptables_rules_v6_filename if iptables_rules_v6_filename else "iptables_rules.v6"
            if not os.path.exists(os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename)):
                with open(os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename), "w") as file:
                    file.write("")

            super().__init__(hostname, named_group, asset_id, asset_tuple, db_name, db_path, db_commands_table_name, db_jobs_table_name, misfire_grace_time)
        except Exception as e:
            raise e

    def execute_allow_command(self, target, direction):
        try:
            self.iptables_direction_handler(action=Actions.allow,
                                            target=target,
                                            direction=direction)
        except Exception as e:
            raise e   

    def execute_deny_command(self, target, direction, drop_process):
        try:
            self.iptables_direction_handler(action=Actions.deny,
                                            target=target,
                                            direction=direction,
                                            drop_process=drop_process)
        except Exception as e:
            raise e
        

    def execute_delete_command(self, command_to_delete):
        try:
            args = command_to_delete.args
            drop_process = args['drop_process'] if 'drop_process' in args else None

            self.iptables_direction_handler(action=Actions.delete,
                                            target=command_to_delete.target.getObj(),
                                            direction=command_to_delete.args['direction'],
                                            drop_process=drop_process,
                                            action_to_delete=command_to_delete.action)
        except Exception as e:
            raise e

        
    def iptables_direction_handler(self, **kwargs):
        try:
            self.iptables_execution_handler(**kwargs, forward=True)
            if kwargs['direction'] == Direction.both:
                kwargs['direction'] = Direction.ingress
                self.iptables_execution_handler(**kwargs)
                kwargs['direction'] = Direction.egress
            self.iptables_execution_handler(**kwargs)
        except Exception as e:
            raise e

    def iptables_execution_handler(self, **kwargs):
        try:
            cmd = self.iptables_create_command(**kwargs)
            self.iptables_execute_command(cmd)
        except Exception as e:
            raise e

    def iptables_create_command(self, action, target, direction, drop_process=None, action_to_delete=None, forward=False):   
        if isinstance(target, IPv4Connection) or isinstance(target, IPv4Net):
            cmd = "sudo iptables "
        elif isinstance(target, IPv6Connection) or isinstance(target, IPv6Net):
            cmd = "sudo ip6tables "

        if action == Actions.delete:
            cmd += "-D "
        else:
            cmd += "--append "

        if not forward:
            if direction == Direction.ingress:
                cmd += "INPUT "
            elif direction == Direction.egress:
                cmd += "OUTPUT "
        else:
            cmd += "FORWARD "

        # icmp da implementare
        if isinstance(target, IPv4Connection) or isinstance(target, IPv6Connection):
            if target.protocol:
                cmd += f"--protocol {target.protocol} "
            if ((target.dst_port and direction == Direction.ingress) or (target.src_port and direction == Direction.egress)) and not target.protocol:
                raise
            if target.src_addr:
                cmd += f"--source {target.src_addr} "
            if target.src_port:
                if target.protocol == L4Protocol.tcp or target.protocol == L4Protocol.udp or target.protocol == L4Protocol.sctp:
                    cmd += f"--sport {target.src_port} "
                else:
                    raise ValueError("src_port not supported with provided protocol")
            if target.dst_addr:
                cmd += f"--destination {target.dst_addr} "
            if target.dst_port:
                if target.protocol == L4Protocol.tcp or target.protocol == L4Protocol.udp or target.protocol == L4Protocol.sctp:
                    cmd += f"--dport {target.dst_port} "
                else:
                    raise ValueError("dst_port not supported with provided protocol")
        elif isinstance(target, IPv4Net) or isinstance(target, IPv6Net):
            ip = target.addr()
            cidr = target.prefix()
            if cidr:
                ip += f"/{cidr}"
            if direction == Direction.ingress or (forward and direction == Direction.both):
                cmd += f"--source {ip} "
            if direction == Direction.egress or (forward and direction == Direction.both):
                cmd += f"--destination {ip} "

        if action == Actions.allow or action_to_delete == Actions.allow:
            iptables_target = "ACCEPT"
        elif action == Actions.deny or action_to_delete == Actions.deny:
            if drop_process == DropProcess.none:
                iptables_target = "DROP"
            elif drop_process == DropProcess.reject:
                iptables_target = "REJECT --reject-with icmp-host-unreachable"
            elif drop_process == DropProcess.false_ack:
            #    return StatusCode.NOTIMPLEMENTED, 'drop_process false ack not implemented for iptables'
                raise ValueError("drop_process false ack not implemented for iptables")

        cmd += f"--jump {iptables_target} "

        if cmd:
            print("-------------> ", cmd)
            return cmd
        else:
            raise


    def save_persistent_commands(self):
        try:
            cmd = "sudo iptables-save > " + os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename)
            self.iptables_execute_command(cmd)
            cmd = "sudo ip6tables-save > " + os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename)
            self.iptables_execute_command(cmd)
        except Exception as e:
            raise e
        
    
    def restore_persistent_commands(self):
        try:
            cmd = "sudo iptables-restore < " + os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename)
            self.iptables_execute_command(cmd)
            cmd = "sudo ip6tables-restore < " + os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename)
            self.iptables_execute_command(cmd)
        except Exception as e:
            raise e
        
    def execute_update_command(self, name, path=None, hashes=None):
        try:
            ext = os.path.splitext(name)[1] 
            if ext != '.v4' and ext != '.v6' and ext != '.json':
                raise
            if not path:
                if ext == '.v4' or ext == '.v6':
                    path = self.iptables_rules_path
                else:
                    # Json
                    pass
            abs_path = os.path.join(path, name)   
            if not os.path.exists(abs_path):
                raise
            if hashes:
                self.iptables_check_hashes(abs_path, hashes)
              
            if ext == '.v4':
                destination = os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename)
            elif ext == '.v6':
                destination = os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename)
            elif ext == '.json':
                pass
            with open(abs_path, "r") as src, open(destination, "w") as dst:
                dst.write(src.read())
            if ext != '.json':
                if ext == '.v4':
                    cmd = "sudo iptables-restore < " + os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename)
                elif ext == '.v6':
                    cmd = "sudo ip6tables-restore < " + os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename)
                self.iptables_execute_command(cmd)
            else:
                pass
        except Exception as e:
            print("------>", str(e))
            raise e  
        

    def iptables_check_hashes(self, abs_path, hashes):
        try:
            md5_hash = hashlib.md5() if 'md5' in hashes else None
            sha1_hash = hashlib.sha1() if 'sha1' in hashes else None
            sha256_hash = hashlib.sha256() if 'sha256' in hashes else None

            with open(abs_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    if md5_hash:
                        md5_hash.update(chunk)
                    if sha1_hash:
                        sha1_hash.update(chunk)
                    if sha256_hash:
                        sha256_hash.update(chunk)

            if md5_hash and Binaryx(md5_hash.hexdigest()).__str__() != hashes['md5'].__str__():
                raise
            if sha1_hash and Binaryx(sha1_hash.hexdigest()).__str__() != hashes['sha1'].__str__():
                raise
            if sha256_hash and Binaryx(sha256_hash.hexdigest()).__str__() != hashes['sha256'].__str__():
                raise
        except Exception as e:
            raise e
    

    def iptables_execute_command(self, cmd):
        try:
             result = subprocess.run(cmd,
                                     shell=True,
                                     check=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
             if result.returncode == 0:
                 logger.debug("Command executed successfully: %s", cmd)
                 logger.debug("Output: %s", result)
                # return StatusCode.OK # 200
             else:
                 logger.debug("Command failed: %s", cmd)
                 logger.debug("Output: %s", result)
                # return StatusCode.INTERNALERROR # 500
                 raise
        except subprocess.CalledProcessError as e:
             logger.debug("Execution error for command: %s", cmd)
             logger.debug("Exception: %s", str(e))
            # return StatusCode.INTERNALERROR # 500
             raise e
        