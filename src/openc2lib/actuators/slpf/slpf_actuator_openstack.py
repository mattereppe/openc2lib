import logging
import os
import openstack

from openc2lib.actuators.slpf.slpf_actuator import SLPFActuator
from openc2lib import Actions, StatusCode, IPv4Net, IPv4Connection, IPv6Net, IPv6Connection, Response, StatusCodeDescription, Feature, ArrayOf, Version, Nsid, ActionTargets, TargetEnum
import openc2lib.profiles.slpf as slpf 
from openc2lib.profiles.slpf.profile import Profile
from openc2lib.profiles.slpf.args import Direction

logger = logging.getLogger(__name__)

class SLPFActuator_openstack(SLPFActuator):
    """ `OpenStack-based` SLPF Actuator implementation.

        This class provides an implementation of the `SLPF Actuator` using OpenStack.
    """

    def __init__(self, file_environment_variables, security_group_id, hostname, named_group, asset_id, asset_tuple, db_path, db_name, db_commands_table_name, db_jobs_table_name):
        """ Initialization of the `OpenStack-based` SLPF Actuator.

            This method connects to OpenStack and initializes the `SLPF Actuator`.

            :param file_environment_variables: Path to a file containing environment variables for connecting to OpenStack.
            :type file_environment_variables: str
            :param security_group_id: Id of the OpenStack security group to manage.
            :type security_group_id: str
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
        """
        try:
            if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
                self.file_environment_variables = file_environment_variables
                self.security_group_id = security_group_id

                self.OPENC2VERS=Version(1,0)

                self.AllowedCommandTarget = ActionTargets()
                self.AllowedCommandTarget[Actions.query] = [TargetEnum.features]
                self.AllowedCommandTarget[Actions.allow] = [TargetEnum.ipv4_connection, TargetEnum.ipv6_connection, TargetEnum.ipv4_net, TargetEnum.ipv6_net]
                self.AllowedCommandTarget[Actions.delete] = [TargetEnum[Profile.nsid+':rule_number']]


            #   Connecting to openstack
                self.connect_to_openstack()
            #   Initializing SLPF Actuator
                super().__init__(hostname=hostname,
                                 named_group=named_group,
                                 asset_id=asset_id,
                                 asset_tuple=asset_tuple,
                                 db_path=db_path,
                                 db_name=db_name,
                                 db_commands_table_name=db_commands_table_name,
                                 db_jobs_table_name=db_jobs_table_name,
                                 rule_files_path=None)

        except Exception as e:
            logger.info("[OPENSTACK] Initialization error: %s", str(e))
            raise e
    
    def connect_to_openstack(self):
        """ OpenStack connection.
        
            This method loads enviroment variables into linux OS to connect to OpenStack, 
            initialize the OpenStack connection 
            and authorizes the connection getting a token from the connection object.
        """
        try:
        #   Load enviroment variables into linux OS to connect to openstack
            if(self.file_environment_variables is not None): #if it is none, it will use the enviroment variables already present in the system
                with open(self.file_environment_variables, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith('export '):  # Only process lines starting with 'export'
                        #   Remove 'export ' and split on the first '='
                            line = line[len('export '):]
                            if '=' in line:
                                key, value = line.split('=', 1)
                            #   Strip quotes around the value if they exist
                                value = value.strip('"').strip("'")
                                os.environ[key] = value
        
            # Initialize the OpenStack connection using environment variables
            self.conn = openstack.connect()           
            # Get the token from the connection object (it will automatically handle authentication)
            token = self.conn.authorize()            
            # Verify successful authentication by checking token
            if token:
                logger.info("[OPENSTACK] Authentication executed successfully")
            else:
                logger.info("[OPENSTACK] Authentication failed")    
        except Exception as e:
            raise e
        

    def query_feature(self, cmd):
        try:
            features = {}
            for f in cmd.target.getObj():
                match f:
                    case Feature.versions:
                        features[Feature.versions.name]=ArrayOf(Version)([self.OPENC2VERS])	
                    case Feature.profiles:
                        pf = ArrayOf(Nsid)()
                        pf.append(Nsid(slpf.Profile.nsid))
                        features[Feature.profiles.name]=pf
                    case Feature.pairs:
                        features[Feature.pairs.name]=self.AllowedCommandTarget
                    case Feature.rate_limit:
                        return Response(status=StatusCode.NOTIMPLEMENTED, status_text="Feature 'rate_limit' not yet implemented")
                    case _:
                        return Response(status=StatusCode.NOTIMPLEMENTED, status_text="Invalid feature '" + f + "'")
            res = slpf.Results(features)
            return  Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK], results=res)
        except Exception as e:
            raise e

        
    
    def validate_action_target_args(self, action, target, args):
        try:
            if action == Actions.allow:
                if self.openstack_find_rule(target, args):
                    raise ValueError(StatusCode.BADREQUEST, "Openstack rule already exists.")
            elif action == Actions.deny:
                raise ValueError(StatusCode.NOTIMPLEMENTED, "Deny action not implemented for OpenStack.")
            elif action == Actions.update:
                raise ValueError(StatusCode.NOTIMPLEMENTED, "Update action not implemented for OpenStack.")
        except ValueError as e:
            raise e
        except Exception as e:
            raise e
        

    def execute_allow_command(self, target, direction):
        try:
            self.openstack_direction_handler(func=self.openstack_allow_handler,
                                             target=target,
                                             direction=direction)
        except Exception as e:
            raise e
        
    def openstack_allow_handler(self, target, direction):
        """ This method handles the execution of an OpenC2 `allow` command for `OpenStack`.

            Starting from OpenC2 `Target` and `direction` gets the corresponding OpenStack arguments for the execution
            of the create_security_group_rule(...) method in order to create a new OpenStack `rule`.

            :param target: The target of the allow action.
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection
            :param direction: Specifies whether to allow incoming traffic, outgoing traffic or both for the specified target.
            :type direction: Direction
        """
        try:
            kwargs = self.openstack_get_rule_arguments(target, direction)
            self.conn.network.create_security_group_rule(**kwargs)            
        except Exception as e:
            raise e
        
        
    def execute_delete_command(self, command_to_delete):
        try:
            self.openstack_direction_handler(func=self.openstack_delete_handler,
                                             target=command_to_delete.target.getObj(),
                                             direction=command_to_delete.args['direction'])
        except Exception as e:
            raise e
        

    def openstack_delete_handler(self, target, direction):
        """ This method handles the execution of an OpenC2 `delete` command for `OpenStack`.

            Starting from OpenC2 `Target` and `Args` of the command to delete 
            gets the corresponding OpenStack `rule id`, 
            finally deletes the OpenStack `rule`.

            :param target: The target of the delete action.
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection
            :param direction: Specifies whether to delete a rule for incoming traffic, outgoing traffic or both.
            :type direction: Direction
        """
        try:
            rule_id = self.openstack_get_rule_id(target, direction)
            if rule_id:
                self.conn.network.delete_security_group_rule(rule_id)
        except Exception as e:
            raise e
        
    
    def openstack_direction_handler(self, func, **kwargs):
        """ This method handles the direction of an OpenC2 `allow` or `delete` command.

            Executes the function passed as an argument with its kwargs for `ingress`, `egress` or `both` directions.

            :param func: The `OpenStack-based` SLPF Actuator handler method for OpenC2 `allow` or `delete` command.
            :type func: method
            :param kwargs: A dictionary of arguments for the execution of the `OpenStack-based` SLPF Actuator handler method for OpenC2 `allow` or `delete` command.
            :type kwargs: dict
        """
        try:
            if kwargs['direction'] == Direction.both:
                kwargs['direction'] = Direction.ingress
                func(**kwargs)
                kwargs['direction'] = Direction.egress
            func(**kwargs)
        except Exception as e:
            raise e
        

    def openstack_find_rule(self, target, args):
        """ This method search for an `OpenStack rule` that matches the OpenC2 `Target` and `Args` passed as arguments.

            :param target: The desired OpenC2 Target
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection
            :param args: The desired OpenC2 Args
            :type args: slpf.Args

            :return: This method returns `True` an `OpenStack rule` is found, `False` otherwise.
        """
        try:
            direction = args['direction']
            if direction == Direction.both:
                direction = Direction.ingress
                if self.openstack_get_rule_id(target, direction):
                    return True
                direction = Direction.egress
                if self.openstack_get_rule_id(target, direction):
                    return True
            else:
                if self.openstack_get_rule_id(target, direction):
                    return True
            return False
        except Exception as e:
            raise e
        
        
    def openstack_get_rule_id(self, target, direction):
        """ This method gets the OpenStack `rule id` of the corresponding OpenStack `rule` that matches the OpenC2 `Target` and `Args` passed as arguments.
        
            :param target: The desired OpenC2 Target
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection
            :param direction: The desired OpenC2 direction
            :type direction: Direction

            :return: The desired OpenStack `rule id`.
        """
        try:
            rules = self.conn.network.security_group_rules(security_group_id=self.security_group_id,
                                                           direction=direction.name,
                                                           ether_type='IPv4' if type(target) == IPv4Net or type(target) == IPv4Connection else 'IPv6',
                                                           protocol=target.protocol.name if (type(target) == IPv4Connection or type(target) == IPv6Connection) and target.protocol else None)
            kwargs = self.openstack_get_rule_arguments(target, direction)
            for rule in rules:
                if (rule.remote_ip_prefix == kwargs['remote_ip_prefix'] and
                    rule.port_range_min == kwargs['port_range_min'] and
                    rule.port_range_max == kwargs['port_range_max']):
                        return rule.id
        except Exception as e:
            raise e
        
    
    def openstack_get_rule_arguments(self, target, direction):
        """ This method gets `OpenStack` arguments from `OpenC2` arguments.
        
            Starting from OpenC2 `Target` and `direction` gets the corresponding OpenStack arguments for the execution
            of the create_security_group_rule(...) method in order to create a new OpenStack `rule`.

            :param target: The desired OpenC2 Target
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection
            :param direction: The desired OpenC2 direction
            :type direction: Direction
        """
        try:
            kwargs = {
                'security_group_id': self.security_group_id,
                'remote_ip_prefix': None,
                'direction': direction.name,
                'protocol': target.protocol.name if (type(target) == IPv4Connection or type(target) == IPv6Connection) and target.protocol else None,
                'ethertype':'IPv4' if type(target) == IPv4Net or type(target) == IPv4Connection else 'IPv6',
                'port_range_min': None,
                'port_range_max': None
            }
            
            if type(target) == IPv4Connection or type(target) == IPv6Connection:
                kwargs['remote_ip_prefix'] = "0.0.0.0/0" if type(target) == IPv4Connection else "::/0"
                if direction == Direction.ingress:
                    if target.src_addr:
                        kwargs['remote_ip_prefix'] = target.src_addr.__str__()
                    if target.src_port:
                        kwargs['port_range_min'] = target.src_port
                        kwargs['port_range_max'] = target.src_port
                elif direction == Direction.egress:
                    if target.dst_addr:
                        kwargs['remote_ip_prefix'] = target.dst_addr.__str__()
                    if target.dst_port:
                        kwargs['port_range_min'] = target.dst_port
                        kwargs['port_range_max'] = target.dst_port
            elif type(target) == IPv4Net or type(target) == IPv6Net:
                kwargs['remote_ip_prefix'] = target.addr()
                cidr = target.prefix()
                if cidr:
                    kwargs['remote_ip_prefix'] += f"/{cidr}"

            return kwargs
        except Exception as e:
            raise e
        