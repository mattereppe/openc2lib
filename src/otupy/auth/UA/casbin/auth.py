import casbin
import json
import logging
import uuid
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path


class OpenC2StatusCode(Enum):
    """OpenC2 standard status codes"""
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_ERROR = 500
    NOT_IMPLEMENTED = 501


class AuthorizationResult(Enum):
    """Authorization decision results"""
    ALLOW = "allow"
    DENY = "deny"
    ERROR = "error"


@dataclass
class OpenC2Command:
    """OpenC2 Command structure"""
    action: str
    target: Dict[str, Any]
    args: Optional[Dict[str, Any]] = None
    actuator: Optional[Dict[str, Any]] = None
    command_id: Optional[str] = None

    def __post_init__(self):
        if not self.command_id:
            self.command_id = str(uuid.uuid4())

        # Validate required fields
        if not self.action or not self.target:
            raise ValueError("Action and target are required for OpenC2 commands")

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values"""
        result = {}
        for key, value in asdict(self).items():
            if value is not None:
                result[key] = value
        return result


@dataclass
class OpenC2Response:
    """OpenC2 Response structure"""
    status: int
    status_text: Optional[str] = None
    command_id: Optional[str] = None
    results: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values"""
        result = {"status": self.status}
        if self.status_text:
            result["status_text"] = self.status_text
        if self.command_id:
            result["command_id"] = self.command_id
        if self.results:
            result["results"] = self.results
        return result


class OpenC2AuthorizationError(Exception):
    """Custom exception for OpenC2 authorization errors"""
    pass


class OpenC2UserAgent:
    """
    OpenC2 User Agent implementing authorization middleware
    between Producer and Consumer
    """

    def __init__(self,
                 model_path: str,
                 policy_path: str,
                 agent_id: str = None,
                 log_level: str = "INFO"):
        """
        Initialize OpenC2 User Agent

        Args:
            model_path: Path to Casbin model configuration
            policy_path: Path to Casbin policy file
            agent_id: Unique identifier for this User Agent
            log_level: Logging level
        """
        self.agent_id = agent_id or f"ua-{uuid.uuid4().hex[:8]}"
        self._setup_logging(log_level)
        self.enforcer = self._initialize_enforcer(model_path, policy_path)
        self.command_history: List[Dict] = []

        self.logger.info(f"OpenC2 User Agent '{self.agent_id}' initialized")

    def _setup_logging(self, log_level: str) -> None:
        """Configure logging with OpenC2 context"""
        logging.basicConfig(
            level=getattr(logging, log_level.upper()),
            format='%(asctime)s - OpenC2-UA[%(name)s] - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(self.agent_id)

    def _initialize_enforcer(self, model_path: str, policy_path: str) -> casbin.Enforcer:
        """Initialize Casbin enforcer with validation"""
        try:
            model_file = Path(model_path)
            policy_file = Path(policy_path)

            if not model_file.exists():
                raise OpenC2AuthorizationError(f"Authorization model not found: {model_path}")
            if not policy_file.exists():
                raise OpenC2AuthorizationError(f"Authorization policy not found: {policy_path}")

            enforcer = casbin.Enforcer(str(model_file), str(policy_file))
            self.logger.info("Authorization enforcer initialized successfully")
            return enforcer

        except Exception as e:
            self.logger.error(f"Failed to initialize authorization: {e}")
            raise OpenC2AuthorizationError(f"Authorization initialization failed: {e}")

    def _extract_authorization_context(self, command: OpenC2Command, producer_id: str) -> tuple:
        """
        Extract authorization context from OpenC2 command

        Args:
            command: OpenC2 command
            producer_id: Producer identifier

        Returns:
            Tuple of (user, action, target, actuator) for authorization
        """
        user = producer_id
        action = command.action

        # Extract target information
        target_type = list(command.target.keys())[0] if command.target else "unknown"
        target_value = str(command.target.get(target_type, "")) if command.target else ""
        target = f"{target_type}:{target_value}"

        # Extract actuator information
        actuator = "default"
        if command.actuator:
            actuator_type = list(command.actuator.keys())[0]
            actuator_value = command.actuator.get(actuator_type, {})
            if isinstance(actuator_value, dict) and 'actuator_id' in actuator_value:
                actuator = actuator_value['actuator_id']
            else:
                actuator = actuator_type

        return user, action, target, actuator

    def authorize_command(self, producer_id: str, command: OpenC2Command) -> AuthorizationResult:
        """
        Authorize OpenC2 command using Casbin

        Args:
            producer_id: Producer identifier
            command: OpenC2 command to authorize

        Returns:
            Authorization result
        """
        try:
            user, action, target, actuator = self._extract_authorization_context(command, producer_id)

            self.logger.debug(
                f"Authorization check: producer='{producer_id}' "
                f"action='{action}' target='{target}' actuator='{actuator}'"
            )

            is_authorized = self.enforcer.enforce(user, action, target, actuator)

            result = AuthorizationResult.ALLOW if is_authorized else AuthorizationResult.DENY

            log_msg = (f"Producer '{producer_id}' {result.value.upper()} for command "
                       f"[{command.command_id}] {action} on {target}")

            if result == AuthorizationResult.ALLOW:
                self.logger.info(log_msg)
            else:
                self.logger.warning(log_msg)

            return result

        except Exception as e:
            self.logger.error(f"Authorization failed for producer '{producer_id}': {e}")
            return AuthorizationResult.ERROR

    def process_command(self, producer_id: str, command_data: Dict[str, Any]) -> OpenC2Response:
        """
        Process OpenC2 command from Producer

        Args:
            producer_id: Producer identifier
            command_data: Raw command data from Producer

        Returns:
            OpenC2 response
        """
        start_time = datetime.now(timezone.utc)

        try:
            # Parse OpenC2 command
            command = self._parse_command(command_data)

            # Log command receipt
            self.logger.info(
                f"Received command [{command.command_id}] from producer '{producer_id}': "
                f"{command.action}"
            )

            # Authorize command
            auth_result = self.authorize_command(producer_id, command)

            # Record command attempt
            self._record_command_attempt(producer_id, command, auth_result, start_time)

            # Handle authorization result
            if auth_result == AuthorizationResult.ALLOW:
                return self._forward_to_consumer(command)
            elif auth_result == AuthorizationResult.DENY:
                return OpenC2Response(
                    status=OpenC2StatusCode.FORBIDDEN.value,
                    status_text=f"Producer '{producer_id}' not authorized for this command",
                    command_id=command.command_id
                )
            else:  # ERROR
                return OpenC2Response(
                    status=OpenC2StatusCode.INTERNAL_ERROR.value,
                    status_text="Authorization system error",
                    command_id=command.command_id
                )

        except ValueError as e:
            self.logger.error(f"Invalid command from producer '{producer_id}': {e}")
            return OpenC2Response(
                status=OpenC2StatusCode.BAD_REQUEST.value,
                status_text=f"Invalid command format: {e}"
            )
        except Exception as e:
            self.logger.error(f"Unexpected error processing command from '{producer_id}': {e}")
            return OpenC2Response(
                status=OpenC2StatusCode.INTERNAL_ERROR.value,
                status_text="Internal server error"
            )

    def _parse_command(self, command_data: Dict[str, Any]) -> OpenC2Command:
        """Parse and validate OpenC2 command"""
        try:
            return OpenC2Command(
                action=command_data["action"],
                target=command_data["target"],
                args=command_data.get("args"),
                actuator=command_data.get("actuator"),
                command_id=command_data.get("command_id")
            )
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")
        except Exception as e:
            raise ValueError(f"Invalid command structure: {e}")

    def _forward_to_consumer(self, command: OpenC2Command) -> OpenC2Response:
        """
        Forward authorized command to Consumer
        (In real implementation, this would send to actual Consumer)

        Args:
            command: Authorized OpenC2 command

        Returns:
            OpenC2 response from Consumer
        """
        self.logger.info(f"Forwarding command [{command.command_id}] to Consumer")

        # Simulate consumer processing
        consumer_response = {
            "status": OpenC2StatusCode.OK.value,
            "status_text": "Command executed successfully",
            "command_id": command.command_id,
            "results": {
                "consumer_id": "consumer-001",
                "execution_time": datetime.now(timezone.utc).isoformat(),
                "command": command.to_dict()
            }
        }

        return OpenC2Response(**consumer_response)

    def _record_command_attempt(self,
                                producer_id: str,
                                command: OpenC2Command,
                                auth_result: AuthorizationResult,
                                timestamp: datetime) -> None:
        """Record command attempt for auditing"""
        record = {
            "timestamp": timestamp.isoformat(),
            "producer_id": producer_id,
            "command_id": command.command_id,
            "action": command.action,
            "target": command.target,
            "authorization_result": auth_result.value,
            "user_agent_id": self.agent_id
        }

        self.command_history.append(record)

        # Keep only last 1000 records to prevent memory issues
        if len(self.command_history) > 1000:
            self.command_history = self.command_history[-1000:]

    def get_command_history(self, producer_id: Optional[str] = None) -> List[Dict]:
        """Get command history, optionally filtered by producer"""
        if producer_id:
            return [record for record in self.command_history
                    if record["producer_id"] == producer_id]
        return self.command_history.copy()

    def get_producer_permissions(self, producer_id: str) -> List[List[str]]:
        """Get all permissions for a producer"""
        try:
            return self.enforcer.get_permissions_for_user(producer_id)
        except Exception as e:
            self.logger.error(f"Failed to get permissions for producer '{producer_id}': {e}")
            return []

    def add_producer_permission(self, producer_id: str, action: str, target: str, actuator: str = "default") -> bool:
        """Add permission for producer"""
        try:
            result = self.enforcer.add_permission_for_user(producer_id, action, target, actuator)
            if result:
                self.logger.info(f"Permission added for producer '{producer_id}': {action}, {target}, {actuator}")
            return result
        except Exception as e:
            self.logger.error(f"Failed to add permission for producer '{producer_id}': {e}")
            return False


def main():
    """Example"""
    try:
        # Initialize User Agent
        ua = OpenC2UserAgent(
            model_path="model.conf",
            policy_path="policy.csv",
            agent_id="ua-security-001",
            log_level="DEBUG"
        )

        # Example OpenC2 commands from different producers
        test_scenarios = [
            {
                "producer_id": "producer-analyst",
                "command": {
                    "action": "allow",
                    "target": {
                        "ip_addr": "192.168.1.42"
                    },
                    "actuator": {
                        "slpf": {
                            "actuator_id": "firewall-001"
                        }
                    }
                }
            },
            {
                "producer_id": "producer-soc",
                "command": {
                    "action": "deny",
                    "target": {
                        "domain_name": "malicious.com"
                    },
                    "actuator": {
                        "slpf": {
                            "actuator_id": "firewall-002"
                        }
                    }
                }
            },
            {
                "producer_id": "producer-external",
                "command": {
                    "action": "delete",
                    "target": {
                        "file": "/critical/system/file"
                    }
                }
            }
        ]

        print("=" * 80)
        print("OpenC2 User Agent - Authorization Demo")
        print("=" * 80)

        for i, scenario in enumerate(test_scenarios, 1):
            print(f"\n--- Test Scenario {i} ---")
            print(f"Producer: {scenario['producer_id']}")
            print(f"Command: {json.dumps(scenario['command'], indent=2)}")

            # Process command
            response = ua.process_command(scenario['producer_id'], scenario['command'])
            print(f"Response: {json.dumps(response.to_dict(), indent=2)}")

            # Show producer permissions
            permissions = ua.get_producer_permissions(scenario['producer_id'])
            print(f"Producer permissions: {permissions}")

        # Show command history
        print(f"\n--- Command History ---")
        history = ua.get_command_history()
        for record in history[-3:]:  # Show last 3 records
            print(f"[{record['timestamp']}] {record['producer_id']} -> "
                  f"{record['action']} ({record['authorization_result']})")

    except OpenC2AuthorizationError as e:
        print(f"Authorization system error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()