import logging
import subprocess
import os
import ipaddress


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

    def __init__(self, iptables_rules_files_path, iptables_rules_v4_filename, iptables_rules_v6_filename, iptables_input_chain_name, iptables_output_chain_name, iptables_forward_chain_name, iptables_cmd, ip6tables_cmd, hostname, named_group, asset_id, asset_tuple, db_path, db_name, db_commands_table_name, db_jobs_table_name, update_path):
        """ Initialization of the `iptables-based` SLPF Actuator.

            This method creates `personalized iptables chain`, 
            creates two `file` to store iptables v4 and v6 persistent rules, respectively, 
            finally initializes the `SLPF Actuator`.

            :param iptables_rules_files_path: Path to the directory containing the files where iptables rules v4/v6 are stored.
            :type iptables_rules_files_path: str
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
            :param hostname: SLPF Actuator hostname.
            :type hostname: str
            :param named_group: SLPF Actuator group.
            :type named_group: str
            :param asset_id: SLPF Actuator asset id.
            :type asset_id: str
            :param asset_tuple: SLPF Actuator asset tuple.
            :type asset_tuple: str
            :param db_path: sqlite3 database path.
            :type db_path: str
            :param db_name: sqlite3 database name.
            :type db_name: str
            :param db_commands_table_name: Name of the `commands` table in the sqlite3 database.
            :type db_commands_table_name: str
            :param db_jobs_table_name: Name of the `APScheduler jobs` table in the sqlite3 database.
            :type db_jobs_table_name: str
            :param update_path: Path to the directory containing the files to be used as update.
            :type update_path: str
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
                self.iptables_rules_files_path = iptables_rules_files_path if iptables_rules_files_path else os.path.dirname(os.path.abspath(__file__))
                if not os.path.exists(self.iptables_rules_files_path):
                    raise
        
            #   Creating the files
                self.iptables_rules_v4_filename = iptables_rules_v4_filename if iptables_rules_v4_filename else "iptables_rules.v4"
                if not os.path.exists(os.path.join(self.iptables_rules_files_path, self.iptables_rules_v4_filename)):
                    logger.info("[IPTABLES] Creating file %s", self.iptables_rules_v4_filename)
                    with open(os.path.join(self.iptables_rules_files_path, self.iptables_rules_v4_filename), "w") as file:
                        file.write("")
                    
                self.iptables_rules_v6_filename = iptables_rules_v6_filename if iptables_rules_v6_filename else "iptables_rules.v6"
                if not os.path.exists(os.path.join(self.iptables_rules_files_path, self.iptables_rules_v6_filename)):
                    logger.info("[IPTABLES] Creating file %s", self.iptables_rules_v6_filename)
                    with open(os.path.join(self.iptables_rules_files_path, self.iptables_rules_v6_filename), "w") as file:
                        file.write("")

            #   Initializing SLPF Actuator
                super().__init__(hostname=hostname,
                                 named_group=named_group,
                                 asset_id=asset_id,
                                 asset_tuple=asset_tuple,
                                 db_path=db_path,
                                 db_name=db_name,
                                 db_commands_table_name=db_commands_table_name,
                                 db_jobs_table_name=db_jobs_table_name,
                                 update_path=update_path)
            except Exception as e:
                logger.info("[IPTABLES] Initialization error: %s", str(e))
                raise e
            
    def iptables_existing_chain(self, base_cmd, chain_name):
        """ This method checks if a custom iptables v4/v6 chain already exists.

            :param base_cmd: Base command for iptables v4/v6.
            :type base_cmd: str
            :param chain_name: Name of the custom iptables v4/v6 chain.
            :type chain_name: str

            :return: `True` if the custom iptables v4/v6 chain already exists, `False` otherwise.
        """
        try:
            self.iptables_execute_command(base_cmd + " -L " + chain_name)
            return True
        except subprocess.CalledProcessError as es:
            return False

    
    def validate_action_target_args(self, action, target, args):
        try:   
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
        """ This method handles the execution of an OpenC2 `allow`, `deny` or `delete` command for `iptables`.

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

            :return: The created `iptables command`.
        """
        try:
            if type(target) == IPv4Connection or type(target) == IPv4Net:
                cmd = self.iptables_cmd + " "
            elif type(target) == IPv6Connection or type(target) == IPv6Net:
                cmd = self.ip6tables_cmd + " "

            if action == Actions.delete:
                cmd += "-D "
            else:
                cmd += "-I "

            if not forward:
                if direction == Direction.ingress:
                    cmd += self.iptables_input_chain_name + " "
                elif direction == Direction.egress:
                    cmd += self.iptables_output_chain_name + " "
            else:
                cmd += self.iptables_forward_chain_name + " "

            if action != Actions.delete:
                position = self.iptables_get_rule_position(target, direction, forward)
                cmd += f"{position} "

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
            #   The address is always considered as a destination address
                cmd += "--destination " + target.__str__() + " "

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
        

    def iptables_get_rule_position(self, target, direction, forward):
        """ This method returns the position where the new rule should be inserted in the considered chain.

            Compare the specifity of the new rule to be inserted with the specifity of the rules already present.

            Specifity order (from lower to higher):
            - destination address,
            - source address,
            - protocol,
            - destination port,
            - source port.

            Networks are always placed at the bottom in size order.

            :param target: Command target.
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection
            :param direction: Command direction.
            :type direction: Direction
            :param forward: A flag that specifies if the rule has to be inserted in the iptables forward chain.
            :type forward: bool

            :return: The `position` found.
        """
        try:
            prot_specifity = None
            addr_specifity = None
            if type(target) == IPv4Connection or type(target) == IPv6Connection:
                if target.protocol and target.dst_port and target.src_port:
                    prot_specifity = 5
                elif target.protocol and target.dst_port and not target.src_port:
                    prot_specifity = 4
                elif target.protocol and not target.dst_port and target.src_port:
                    prot_specifity = 3
                elif target.protocol and not target.dst_port and not target.src_port:
                    prot_specifity = 2
                elif not target.protocol:
                    prot_specifity = 1

                if target.dst_addr and target.src_addr:
                    addr_specifity = 4
                elif target.dst_addr and not target.src_addr:
                    addr_specifity = 3
                elif not target.dst_addr and target.src_addr:
                    addr_specifity = 2
                elif not target.dst_addr and not target.src_addr:
                    addr_specifity = 1
                
            if not forward:
                if direction == Direction.ingress:
                    chain = self.iptables_input_chain_name
                elif direction == Direction.egress:
                    chain = self.iptables_output_chain_name
            else:
                chain = self.iptables_forward_chain_name

            cmd = self.iptables_cmd if type(target) == IPv4Connection or type(target) == IPv4Net else self.ip6tables_cmd
            cmd = cmd.strip().split()
            cmd.append("-S")
            cmd.append(chain)
            output = subprocess.check_output(cmd, text=True)
            rules = output.strip().splitlines()
            
            pos = 0
            for rule in rules:
                if not rule.startswith("-A"):
                    continue

                pos += 1
                rule_parts = rule.split()
                
                rule_addr_specifity = None
                if "-d" in rule_parts and "-s" in rule_parts:
                    rule_addr_specifity = 4
                elif "-d" in rule_parts and not "-s" in rule_parts:
                    rule_addr_specifity = 3
                elif not "-d" in rule_parts and "-s" in rule_parts:
                    rule_addr_specifity = 2
                elif not "-d" in rule_parts and not "-s" in rule_parts:
                    rule_addr_specifity = 1

                rule_prot_specifity = None
                if "-p" in rule_parts and "--dport" in rule_parts and "--sport" in rule_parts:
                    rule_prot_specifity = 5
                elif "-p" in rule_parts and "--dport" in rule_parts and not "--sport" in rule_parts:
                    rule_prot_specifity = 4
                elif "-p" in rule_parts and not "--dport" in rule_parts and "--sport" in rule_parts:
                    rule_prot_specifity = 3
                elif "-p" in rule_parts and not "--dport" in rule_parts and not "--sport" in rule_parts:
                    rule_prot_specifity = 2
                elif not "-p" in rule_parts:
                    rule_prot_specifity = 1

                if type(target) == IPv4Connection or type(target) == IPv6Connection:
                    if rule_addr_specifity < addr_specifity:
                        return pos
                    elif rule_addr_specifity > addr_specifity:
                        continue
                    elif rule_addr_specifity == addr_specifity: 
                        if rule_prot_specifity <= prot_specifity:
                            return pos
                        else:
                            continue
                elif type(target) == IPv4Net or type(target) == IPv6Net:
                    if rule_addr_specifity != 3 or rule_prot_specifity != 1:
                        continue
                    rule_cidr = rule_parts[rule_parts.index("-d") + 1]
                    rule_prefix = ipaddress.ip_network(rule_cidr, strict=False).prefixlen
                    target_prefix = ipaddress.ip_network(target.__str__(), strict=False).prefixlen
                    if rule_prefix <= target_prefix:
                        return pos
            return pos + 1
        except Exception as e:
            raise e


    def save_persistent_commands(self):
        try:
            logger.info("[IPTABLES] Saving iptables persistent commands")
            cmd = self.iptables_cmd + "-save > " + os.path.join(self.iptables_rules_files_path, self.iptables_rules_v4_filename)
            self.iptables_execute_command(cmd)
            cmd = self.ip6tables_cmd + "-save > " + os.path.join(self.iptables_rules_files_path, self.iptables_rules_v6_filename)
            self.iptables_execute_command(cmd)
        except Exception as e:
            logger.info("[IPTABLES] An error occurred saving iptables rules: %s", str(e))
            raise e
        
    
    def restore_persistent_commands(self):
        try:
            logger.info("[IPTABLES] Restoring iptables persistent commands")
            cmd = self.iptables_cmd + "-restore < " + os.path.join(self.iptables_rules_files_path, self.iptables_rules_v4_filename)
            self.iptables_execute_command(cmd)
            cmd = self.ip6tables_cmd + "-restore < " + os.path.join(self.iptables_rules_files_path, self.iptables_rules_v6_filename)
            self.iptables_execute_command(cmd)
        except Exception as e:
            logger.info("[IPTABLES] An error occurred restoring iptables rules: %s", str(e))
            raise e
        
    def clean_actuator_rules(self):
        try:
            logger.info("[IPTABLES] Deleting all iptables rules") 
        #   Deleting rules from iptables
            cmd = self.iptables_cmd + " -F"
            self.iptables_execute_command(cmd)
        #   Linking personalized iptables chains with iptables chains
            self.iptables_execute_command(self.iptables_cmd + " -A INPUT -j " + self.iptables_input_chain_name)
            self.iptables_execute_command(self.iptables_cmd + " -A OUTPUT -j " + self.iptables_output_chain_name)     
            self.iptables_execute_command(self.iptables_cmd + " -A FORWARD -j " + self.iptables_forward_chain_name)

        #   Deleting rules from ip6tables
            cmd = self.ip6tables_cmd + " -F"
            self.iptables_execute_command(cmd)
        #   Linking personalized ip6tables chains with ip6tables chains
            self.iptables_execute_command(self.ip6tables_cmd + " -A INPUT -j " + self.iptables_input_chain_name)
            self.iptables_execute_command(self.ip6tables_cmd + " -A OUTPUT -j " + self.iptables_output_chain_name)
            self.iptables_execute_command(self.ip6tables_cmd + " -A FORWARD -j " + self.iptables_forward_chain_name)
        except Exception as e:
            logger.info("[IPTABLES] An error occurred deleting all iptables rules: %s", str(e))
            raise e
        
    def execute_update_command(self, name, path):
        try:             
            abs_path = os.path.join(path, name)
            ext = os.path.splitext(name)[1]

            if ext == '.v4':
                destination = os.path.join(self.iptables_rules_files_path, self.iptables_rules_v4_filename)
            elif ext == '.v6':
                destination = os.path.join(self.iptables_rules_files_path, self.iptables_rules_v6_filename)

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
        except Exception as e:
            raise e
        