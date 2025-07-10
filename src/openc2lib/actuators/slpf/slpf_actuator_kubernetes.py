import logging
import os
import subprocess

from kubernetes import config, client
from kubernetes.client.rest import ApiException

from openc2lib.actuators.slpf.slpf_actuator import SLPFActuator
from openc2lib import Actions, StatusCode, IPv4Net, IPv4Connection, IPv6Net, IPv6Connection, Response, StatusCodeDescription, Feature, ArrayOf, Version, Nsid, ActionTargets, TargetEnum
import openc2lib.profiles.slpf as slpf
from openc2lib.profiles.slpf.profile import Profile
from openc2lib.profiles.slpf.args import Direction

logger = logging.getLogger(__name__)

class SLPFActuator_kubernetes(SLPFActuator):
    """ `Kubernetes-based` SLPF Actuator implementation.

        This class provides an implementation of the `SLPF Actuator` using Kubernetes.
    """

    def __init__(self, config_file, kube_context, namespace, generate_name, hostname, named_group, asset_id, asset_tuple, db_path, db_name, db_commands_table_name, db_jobs_table_name, update_path):
        """ Initialization of the `Kubernetes-based` SLPF Actuator.

            This method connects to Kubernetes and initializes the `SLPF Actuator`.

            :param config_file: Absolute path to the Kubernetes configuration file.
            :type config_file: str
            :param kube_context: Name of the Kubernetes context.
            :type kube_context: str
            :param namespace: Name of the Kubernetes namespace.
            :type namespace: str
            :param generate_name: Prefix used by Kubernetes to generate a unique name for network policies.
            :type generate_name: str
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
        try:
            if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
                self.config_file = config_file if config_file else None
                self.kube_context = kube_context if kube_context else None
                self.namespace = namespace if namespace else "default"
                self.generate_name = generate_name if generate_name else "network-policy-"

                self.OPENC2VERS=Version(1,0)

                self.AllowedCommandTarget = ActionTargets()
                self.AllowedCommandTarget[Actions.query] = [TargetEnum.features]
                self.AllowedCommandTarget[Actions.allow] = [TargetEnum.ipv4_connection, TargetEnum.ipv6_connection, TargetEnum.ipv4_net, TargetEnum.ipv6_net]
                self.AllowedCommandTarget[Actions.delete] = [TargetEnum[Profile.nsid+':rule_number']]
                self.AllowedCommandTarget[Actions.update] = [TargetEnum.file]


            #   Connecting to Kubernetes
                self.connect_to_kubernetes()
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
            logger.info("[KUBERNETES] Initialization error: %s", str(e))
            raise e
        

    def connect_to_kubernetes(self):
        """ Kubernetes connection.
        
            This method loads the kubeconfig file (by default it loads from ~/.kube/config) 
            and creates an API client.
        """
        try:
            # Load the kubeconfig file (by default it loads from ~/.kube/config) and context
            config.load_kube_config(config_file=self.config_file, context=self.kube_context)
            # Create an API client
            self.api_client = client.NetworkingV1Api()
            logger.info("[KUBERNETES] Connection executed successfully")
        except Exception as e:
            logger.info("[KUBERNETES] Connection failed.")
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
            if action == Actions.deny:
                raise ValueError(StatusCode.NOTIMPLEMENTED, "Deny action not implemented for OpenStack.")
            elif action == Actions.update:
                ext = os.path.splitext(target['name'])[1] 
                if ext != '.yaml':
                    raise ValueError(StatusCode.BADREQUEST, "File not supported")
        except ValueError as e:
            raise e
        except Exception as e:
            raise e
        

    def execute_allow_command(self, target, direction):
        try:
            ingress = None
            egress = None
            _from = None
            to = None
            cidr = target.__str__() if type(target) == IPv4Net or type(target) == IPv6Net else None
            ports = None
            protocol = target.protocol.name.upper() if (type(target) == IPv4Connection or type(target) == IPv6Connection) and target.protocol else None
            port = None

            metadata=client.V1ObjectMeta(
                    generate_name=self.generate_name,
                    namespace=self.namespace
                )
            
            policy_types = [direction.name.capitalize()] if direction != Direction.both else ["Ingress", "Egress"]

            if direction == Direction.ingress or direction == Direction.both:
                if type(target) == IPv4Connection or type(target) == IPv6Connection:
                    if target.src_addr:
                       cidr = target.src_addr.__str__()
                    if target.protocol:
                        if target.src_port:
                            port = target.src_port
                        ports = [
                            client.V1NetworkPolicyPort(
                                protocol=protocol,
                                port=port
                            )
                        ]

                if cidr:
                    _from = [
                            client.V1NetworkPolicyPeer(
                                ip_block=client.V1IPBlock(cidr=cidr)
                            )
                        ]
                
                if _from or ports:
                    ingress = [
                        client.V1NetworkPolicyIngressRule(
                            _from=_from,
                            ports=ports
                        )
                    ]
            
            if direction == Direction.egress or direction == Direction.both:
                if type(target) == IPv4Connection or type(target) == IPv6Connection:
                    cidr = target.dst_addr.__str__() if target.dst_addr else None
                    ports = None
                    port = target.dst_port if target.dst_port else None

                    if target.protocol:
                        ports = [
                            client.V1NetworkPolicyPort(
                                protocol=protocol,
                                port=port
                            )
                        ]

                if cidr:
                    to = [
                            client.V1NetworkPolicyPeer(
                                ip_block=client.V1IPBlock(cidr=cidr)
                            )
                        ]

                if to or ports: 
                    egress = [
                        client.V1NetworkPolicyEgressRule(
                            to=to,
                            ports=ports
                        )
                    ]
                    
            network_policy = client.V1NetworkPolicy(
                metadata=metadata,
                spec=client.V1NetworkPolicySpec(
                    policy_types=policy_types,
                    ingress=ingress,
                    egress=egress,
                    pod_selector=client.V1LabelSelector(match_labels={})
                )
            )

            self.api_client.create_namespaced_network_policy(
                namespace=self.namespace,
                body=network_policy
            )    

        except Exception as e:
            raise e
        

    def execute_delete_command(self, command_to_delete):
        try:
            target = command_to_delete.target.getObj()
            direction = command_to_delete.args['direction']
            policy_types = [direction.name.capitalize()] if direction != Direction.both else ["Ingress", "Egress"]

            network_policies = self.api_client.list_namespaced_network_policy(namespace=self.namespace)
            
            for policy in network_policies.items:
                if set(policy.spec.policy_types) != set(policy_types):
                    continue

                ingress_rule_list = policy.spec.ingress
                egress_rule_list  = policy.spec.egress
                if ingress_rule_list and len(ingress_rule_list) > 1:
                    continue
                if egress_rule_list and len(egress_rule_list) > 1:
                    continue
                ingress_rule = ingress_rule_list[0] if ingress_rule_list else None
                egress_rule = egress_rule_list[0] if egress_rule_list else None

                cidr = target.__str__() if type(target) == IPv4Net or type(target) == IPv6Net else None
                protocol = target.protocol.name.upper() if (type(target) == IPv4Connection or type(target) == IPv6Connection) and target.protocol else None
                port = None
                if ingress_rule:
                    if type(target) == IPv4Connection or type(target) == IPv6Connection:
                        if target.src_addr:
                            cidr = target.src_addr.__str__()
                        if target.src_port:
                            port = target.src_port
                    if not self.kubernetes_match_policy(cidr, protocol, port, Direction.ingress, ingress_rule):
                        continue

                if egress_rule: 
                    if type(target) == IPv4Connection or type(target) == IPv6Connection:
                        cidr = None
                        port = None
                        if target.dst_addr:
                            cidr = target.dst_addr.__str__()
                        if target.dst_port:
                            port = target.dst_port
                    if not self.kubernetes_match_policy(cidr, protocol, port, Direction.egress, egress_rule):
                        continue

                logger.info("[KUBERNETES] Deleting Kubernetes Network Policy " + policy.metadata.name)
                self.api_client.delete_namespaced_network_policy(
                    name=policy.metadata.name,
                    namespace=self.namespace,
                    body=client.V1DeleteOptions()
                )
                return
            raise ValueError(StatusCode.INTERNALERROR, "Kubernetes network policy not found.")
        except ValueError as e:
            raise e    
        except Exception as e:
            raise e
        

    def kubernetes_match_policy(self, cidr, protocol, port, direction, policy):
        """ This method checks wheter a Kubernetes `network policy` matches the `cidr`, `protocol` and `port` for the specified direction.

            :param cidr: The desired cidr.
            :type cidr: str
            :param protocl: The desired protocol.
            :type protocol: str
            :param port: The desired port.
            :type port: Port
            :param direction: The desired direction.
            :type direction: Direction
            :param policy: The network policy to be checked.
            :type policy: V1NetworkPolicyIngressRule/V1NetworkPolicyEgressRule

            :return: `True` if the Kubernetes network policy matches the cidr, protocol and port for the specified direction. 
                    `False` otherwise.
        """
        try: 
            from_or_to = policy._from if direction == Direction.ingress else policy.to
            if (cidr and not from_or_to) or (not cidr and from_or_to):
                return False
            if cidr:
                if len(from_or_to) > 1:
                    return False
                peer = from_or_to[0]
                if not peer.ip_block:
                    return False
                if peer.ip_block.cidr != cidr:
                    return False
                
            ports = policy.ports
            if (protocol and not ports) or (not protocol and ports):
                return False
            if protocol:
                if len(ports) > 1:
                    return False
                prt = ports[0]
                if prt.protocol != protocol:
                    return False
                if port and prt.port != port:
                    return False
            return True
        except Exception as e:
            raise e
        

    def clean_actuator_rules(self):
        try:
            logger.info("[KUBERNETES] Deleting all Kubernetes network policy.")
            network_policies = self.api_client.list_namespaced_network_policy(namespace=self.namespace)
            for policy in network_policies.items:
                self.api_client.delete_namespaced_network_policy(
                    name=policy.metadata.name,
                    namespace=self.namespace,
                    body=client.V1DeleteOptions()
                )
        except Exception as e:
            logger.info("[KUBERNETES] An error occurred deleting all Kubernetes Network Policy: %s", str(e))
            raise e
    
    def execute_update_command(self, name, path):
        try:
            self.clean_actuator_rules()

            abs_path = os.path.join(path, name)
            cmd = "kubectl apply -f " + abs_path + " -n " + self.namespace
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            raise e
        except Exception as e:
            raise e
