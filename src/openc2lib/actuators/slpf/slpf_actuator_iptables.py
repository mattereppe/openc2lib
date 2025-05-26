import logging
import subprocess
import os


from openc2lib.actuators.slpf.slpf_actuator import SLPFActuator

from openc2lib import Version, Actions, IPv4Net, IPv4Connection , IPv6Net, IPv6Connection, L4Protocol, Binaryx, StatusCode
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
    """ `iptables-based` SLPF Actuator implementation.

        This class provides an implementation of the `SLPF Actuator` using iptables.
    """

    def __init__(self, hostname, named_group, asset_id, asset_tuple, iptables_rules_path, iptables_rules_v4_filename, iptables_rules_v6_filename, iptables_input_chain_name, iptables_output_chain_name, iptables_forward_chain_name, iptables_cmd, ip6tables_cmd, db_name, db_path, db_commands_table_name, db_jobs_table_name, misfire_grace_time):
        """ Initialization of the `iptables-based` SLPF Actuator.

            This method creates `personalized iptables chain`, 
            creates two `file` to store iptables v4 and v6 persistent rules, respectively, 
            finally initializes the `SLPF Actuator`.

            :param hostname: SLPF Actuator hostname.
            :type hostname: str
            :param named_group: SLPF Actuator group.
            :type named_group: str
            :param asset_id: SLPF Actuator asset id.
            :type asset_id: str
            :param asset_tuple: SLPF Actuator asset tuple.
            :type asset_tuple: str
            :param iptables_rules_path: Path to iptables rule files.
            :type rule_files_path: str
            :param iptables_rules_v4_filename: Name of the file where iptables rules v4 are stored.
            :type iptables_rules_v4_filename: str
            :param iptables_rules_v6_filename: Name of the file where iptables rules v6 are stored.
            :type iptables_rules_v6_filename: str
            :param iptables_input_chain_name: Name of the custom iptables input chain.
            :type iptables_input_chain_name: str
            :param iptables_output_chain_name: Name of the custom iptables output chain.
            :type iptables_output_chain_name: str
            :param iptables_forward_chain_name: Name of the custom iptables forward chain.
            :type iptables_forward_chain_name: str
            :param iptables_cmd: Base command for iptables v4 (e.g: sudo iptables).
            :type iptables_cmd: str
            :param ip6tables_cmd: Base command for iptables v6 (e.g: sudo ip6tables).
            :type ip6tables_cmd: str
            :param db_name: sqlite3 database name.
            :type db_name: str
            :param db_path: sqlite3 database path.
            :type db_path: str
            :param db_commands_table_name: Name of the `commands` table in the sqlite3 database.
            :type db_commands_table_name: str
            :param db_jobs_table_name: Name of the `APScheduler jobs` table in the sqlite3 database.
            :type db_jobs_table_name: str
            :param misfire_grace_time: Seconds after the designated runtime that the `APScheduler job` is still allowed to be run, because of a `shutdown`.
            :type misfire_grace_time: int
        """

        if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            MY_IDS['hostname'] = hostname
            MY_IDS['named_group'] = named_group
            MY_IDS['asset_id'] = asset_id
            MY_IDS['asset_tuple'] = asset_tuple

            self.iptables_input_chain_name = iptables_input_chain_name
            self.iptables_output_chain_name = iptables_output_chain_name
            self.iptables_forward_chain_name = iptables_forward_chain_name
            self.iptables_cmd = iptables_cmd
            self.ip6tables_cmd = ip6tables_cmd
        
            try:
            #   Creating personalized iptables/ip6tables chains and linking them with iptables/ip6tables chains
                if not self.iptables_existing_chain(self.iptables_cmd, self.iptables_input_chain_name):
                    logger.info("[IPTABLES] Creating personalized iptables chain %s", self.iptables_input_chain_name)
                    self.iptables_execute_command(self.iptables_cmd + " -N " + self.iptables_input_chain_name)
                    self.iptables_execute_command(self.iptables_cmd + " -A INPUT -j " + self.iptables_input_chain_name)
                if not self.iptables_existing_chain(self.iptables_cmd, self.iptables_output_chain_name):
                    logger.info("[IPTABLES] Creating personalized iptables chain %s", self.iptables_output_chain_name)
                    self.iptables_execute_command(self.iptables_cmd + " -N " + self.iptables_output_chain_name)
                    self.iptables_execute_command(self.iptables_cmd + " -A OUTPUT -j " + self.iptables_output_chain_name)     
                if not self.iptables_existing_chain(self.iptables_cmd, self.iptables_forward_chain_name):
                    logger.info("[IPTABLES] Creating personalized iptables chain %s", self.iptables_forward_chain_name)
                    self.iptables_execute_command(self.iptables_cmd + " -N " + self.iptables_forward_chain_name)
                    self.iptables_execute_command(self.iptables_cmd + " -A FORWARD -j " + self.iptables_forward_chain_name)
                if not self.iptables_existing_chain(self.ip6tables_cmd, self.iptables_input_chain_name):
                    logger.info("[IPTABLES] Creating personalized ip6tables chain %s", self.iptables_input_chain_name)
                    self.iptables_execute_command(self.ip6tables_cmd + " -N " + self.iptables_input_chain_name)
                    self.iptables_execute_command(self.ip6tables_cmd + " -A INPUT -j " + self.iptables_input_chain_name)
                if not self.iptables_existing_chain(self.ip6tables_cmd, self.iptables_output_chain_name):
                    logger.info("[IPTABLES] Creating personalized ip6tables chain %s", self.iptables_output_chain_name)
                    self.iptables_execute_command(self.ip6tables_cmd + " -N " + self.iptables_output_chain_name)
                    self.iptables_execute_command(self.ip6tables_cmd + " -A OUTPUT -j " + self.iptables_output_chain_name)
                if not self.iptables_existing_chain(self.ip6tables_cmd, self.iptables_forward_chain_name):
                    logger.info("[IPTABLES] Creating personalized ip6tables chain %s", self.iptables_forward_chain_name)
                    self.iptables_execute_command(self.ip6tables_cmd + " -N " + self.iptables_forward_chain_name)
                    self.iptables_execute_command(self.ip6tables_cmd + " -A FORWARD -j " + self.iptables_forward_chain_name)

            #   Path for iptables/ip6tables files
            #   These files are used by iptables/ip6tables-save and iptables/ip6tables-restore commands
                self.iptables_rules_path = iptables_rules_path if iptables_rules_path else os.path.dirname(os.path.abspath(__file__))
                if not os.path.exists(self.iptables_rules_path):
                    raise
        
            #   Creating the files
                self.iptables_rules_v4_filename = iptables_rules_v4_filename if iptables_rules_v4_filename else "iptables_rules.v4"
                if not os.path.exists(os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename)):
                    logger.info("[IPTABLES] Creating file %s", self.iptables_rules_v4_filename)
                    with open(os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename), "w") as file:
                        file.write("")
                    
                self.iptables_rules_v6_filename = iptables_rules_v6_filename if iptables_rules_v6_filename else "iptables_rules.v6"
                if not os.path.exists(os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename)):
                    logger.info("[IPTABLES] Creating file %s", self.iptables_rules_v6_filename)
                    with open(os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename), "w") as file:
                        file.write("")

                #   Initializing SLPF Actuator
                super().__init__(hostname, named_group, asset_id, asset_tuple, db_name, db_path, db_commands_table_name, db_jobs_table_name, misfire_grace_time, self.iptables_rules_path)
            except Exception as e:
                logger.info("[IPTABLES] Initialization error: %s", str(e))
                raise e
            
    def iptables_existing_chain(self, base_cmd, chain_name):
        """ This method checks if a custom iptables v4/v6 chain already exists.

            :param base_cmd: Base command for iptables v4/v6.
            :type base_cmd: str
            :param chain_name: Name of the custom iptables v4/v6 chain.
            :type chain_name: str
        """
        try:
            self.iptables_execute_command(base_cmd + " -L " + chain_name)
            return True
        except subprocess.CalledProcessError as es:
            return False

    
    def validate_action_target_args(self, action, target, args):
        try:
            if action == Actions.allow or action == Actions.deny:
                if type(target) == IPv4Connection or type(target) == IPv6Connection:
                    if (target.src_port or target.dst_port) and not target.protocol:
                        raise ValueError(StatusCode.BADREQUEST, "Protocol must be provided")
                if action == Actions.deny:
                    if 'drop_process' in args and args['drop_process'] == DropProcess.false_ack:
                        raise ValueError(StatusCode.NOTIMPLEMENTED, "Drop process argument with false ack value not implemented for iptables")
                
            if action == Actions.update:
                ext = os.path.splitext(target['name'])[1] 
                if ext != '.v4' and ext != '.v6':
                    raise ValueError(StatusCode.BADREQUEST, "File not supported")
        except ValueError as e:
            raise e
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
        """ This method handles the direction of an OpenC2 `allow`, `deny` or `delete` command and 
            the iptables `forward chain`.

            :param kwargs: A dictionary of arguments for the execution of the OpenC2 `allow`, `deny` or `delete` command.
            :type kwargs: dict
        """
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
        """ This method handles the execution of an OpenC2 `allow`, `deny` or `delete` command.

            Creates the desired iptables command and executes it.

            :param kwargs: A dictionary of arguments for the execution of the OpenC2 `allow`, `deny` or `delete` command.
            :type kwargs: dict
        """
        try:
            cmd = self.iptables_create_command(**kwargs)
            self.iptables_execute_command(cmd)
            logger.info("[IPTABLES] Command executed successfully: %s", cmd)
        except Exception as e:
            logger.info("[IPTABLES] Execution error for command: %s", cmd)
            logger.info("[IPTABLES] Exception: %s", str(e))
            raise e

    def iptables_create_command(self, action, target, direction, drop_process=None, action_to_delete=None, forward=False):   
        """ This method creates an iptables v4/v6 `accept rule`, `drop rule` or `delete rule` command.

            :param action: Command action.
            :type action: Actions
            :param target: Command target.
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection
            :param direction: Command direction.
            :type direction: Direction
            :param drop_process: Specifies how to handle denied packets: 
                                `none` drop the packet and do not send any notification to the source of the packet,
                                `reject` drop the packet and send an ICMP host unreachable (or equivalent) to the source of the packet,
                                `false_ack` drop the packet and send a false acknowledgment.
            :type drop_process: DropProcess
            :param action_to_delete: The action of the OpenC2 `Command` to delete.
            :type action_to_delete: Actions
            :param forward: A flag that specifies if the rule has to be inserted in the iptables forward chain.
            :type forward: bool
        """
        try:
            if type(target) == IPv4Connection or type(target) == IPv4Net:
                cmd = self.iptables_cmd + " "
            elif type(target) == IPv6Connection or type(target) == IPv6Net:
                cmd = self.ip6tables_cmd + " "

            if action == Actions.delete:
                cmd += "-D "
            else:
                cmd += "--append "

            if not forward:
                if direction == Direction.ingress:
                    cmd += self.iptables_input_chain_name + " "
                elif direction == Direction.egress:
                    cmd += self.iptables_output_chain_name + " "
            else:
                cmd += self.iptables_forward_chain_name + " "

            if type(target) == IPv4Connection or type(target) == IPv6Connection:
                if target.protocol:
                    cmd += f"--protocol {target.protocol} "
                if target.src_addr:
                    cmd += f"--source {target.src_addr} "
                if target.src_port:
                    cmd += f"--sport {target.src_port} "
                if target.dst_addr:
                    cmd += f"--destination {target.dst_addr} "
                if target.dst_port:
                    cmd += f"--dport {target.dst_port} "
            elif type(target) == IPv4Net or type(target) == IPv6Net:
                ip = target.addr()
                cidr = target.prefix()
                if cidr:
                    ip += f"/{cidr}"
            #   The address is always considered as a destination address
                cmd += f"--destination {ip} "

            if action == Actions.allow or action_to_delete == Actions.allow:
                iptables_target = "ACCEPT"
            elif action == Actions.deny or action_to_delete == Actions.deny:
                if drop_process == DropProcess.none:
                    iptables_target = "DROP"
                elif drop_process == DropProcess.reject:
                    iptables_target = "REJECT --reject-with icmp-host-unreachable"

            cmd += f"--jump {iptables_target} "

            return cmd
        except Exception as e:
            raise e


    def save_persistent_commands(self):
        try:
            cmd = self.iptables_cmd + "-save > " + os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename)
            self.iptables_execute_command(cmd)
            cmd = self.ip6tables_cmd + "-save > " + os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename)
            self.iptables_execute_command(cmd)
        except Exception as e:
            raise e
        
    
    def restore_persistent_commands(self):
        try:
            cmd = self.iptables_cmd + "-restore < " + os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename)
            self.iptables_execute_command(cmd)
            cmd = self.ip6tables_cmd + "-restore < " + os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename)
            self.iptables_execute_command(cmd)
        except Exception as e:
            raise e
        
    def clean_actuator_rules(self):
        try:
            cmd = self.iptables_cmd + " -F"
            self.iptables_execute_command(cmd)
            cmd = self.ip6tables_cmd + " -F"
            self.iptables_execute_command(cmd)
        except Exception as e:
            raise e
        
    def execute_update_command(self, name, path):
        try:             
            abs_path = os.path.join(path, name)
            ext = os.path.splitext(name)[1]

            if ext == '.v4':
                destination = os.path.join(self.iptables_rules_path, self.iptables_rules_v4_filename)
            elif ext == '.v6':
                destination = os.path.join(self.iptables_rules_path, self.iptables_rules_v6_filename)

            with open(abs_path, "r") as src, open(destination, "w") as dst:
                dst.write(src.read())

            self.restore_persistent_commands()

        except Exception as e:
            raise e  
    

    def iptables_execute_command(self, cmd):
        """ This method executes an iptables v4/v6 command.

            :param cmd: The iptables v4/v6 command to be executed.
            :type cmd: str
        """
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
             raise e
        