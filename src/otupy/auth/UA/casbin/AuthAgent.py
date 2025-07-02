import casbin
import logging
from pathlib import Path
import sys

class AuthorizationError(Exception):
    pass


class AuthorizationAgent:
    def __init__(self, model_path: str, policy_path: str):
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
        self.logger = logging.getLogger('AuthAgent')
        self.enforcer = self._initialize_enforcer(model_path, policy_path)
        self.logger.info("Authorization agent initialized")

    def _initialize_enforcer(self, model_path: str, policy_path: str) -> casbin.Enforcer:
        model_file = Path(model_path)
        policy_file = Path(policy_path)

        if not model_file.exists():
            raise AuthorizationError(f"Model file not found: {model_path}")
        if not policy_file.exists():
            raise AuthorizationError(f"Policy file not found: {policy_path}")

        try:
            return casbin.Enforcer(str(model_file), str(policy_file))
        except Exception as e:
            raise AuthorizationError(f"Failed to initialize enforcer: {e}")

    def is_authorized(self, user: str, action: str, target: str, actuator: str = "default") -> bool:
        try:
            #TODO parse command e estrarre info
            self.logger.debug(f"Checking permission: user={user}, action={action}, target={target}, actuator={actuator}")
            return self.enforcer.enforce(user, action, target, actuator)
        except Exception as e:
            self.logger.error(f"Authorization check failed: {e}")
            raise AuthorizationError(f"Error during authorization check: {e}")
