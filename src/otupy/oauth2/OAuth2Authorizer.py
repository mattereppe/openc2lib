from otupy.auth.Authorizer import Authorizer
from otupy.core.results import Results
import requests
import logging
from otupy.core.response import Response, StatusCode
from authlib.oauth2 import OAuth2Error
import json
from datetime import datetime, timezone
from typing import Optional, Dict, Any, Tuple


class OAuth2Authorizer(Authorizer):
    def __init__(self, client_id, client_secret, introspection_url, ua_url, timeout=5):
        self.client_id = client_id
        self.client_secret = client_secret
        self.introspection_url = introspection_url
        self.ua_url = ua_url
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)

    def authorize(self, msg,auth_info):
        try:
            command=msg.content
            action = command.action.name if hasattr(command.action, 'name') else str(command.action)
            target_type = command.target.choice
            target = [f"{target_type}.{t.name}" for t in command.target.obj]
            actuator = command.actuator.choice
            command_dict = {
                "action": action,
                "target": target,
                "actuator": actuator
            }
            username=auth_info['username']
            payload = {"command": command_dict,"username": username}
            ua_auth = f"{self.ua_url}/authorize"
            response = requests.post(ua_auth, json=payload)
            if response.status_code == 200 and response.json() is True:
                self.logger.info('Authorized to send command')
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error authorizing user: {e}")
            return False

    def introspect_token(self, token_string: str) -> Dict[str, Any]:
        data = {
            'token': token_string,
            'token_type_hint': 'access_token'
        }
        auth = (self.client_id, self.client_secret) if self.client_id and self.client_secret else None
        try:
            resp = requests.post(
                self.introspection_url,
                data=data,
                auth=auth,
                timeout=self.timeout,
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Token introspection request failed: {e}")
            raise

    def validate_token(self, token: str) -> Dict[str, Any]:
        """
               Introspect the token to retrieve token information.

        """
        try:
            token_info = self.introspect_token(token)

            if not token_info.get('active', False):
                self.logger.warning("Token is not active")
                raise OAuth2Error("Token is not active")

            exp = token_info.get('exp')
            if exp and datetime.fromtimestamp(exp, timezone.utc) < datetime.now(timezone.utc):
                self.logger.warning("Token has expired")
                raise OAuth2Error("Token has expired")

            self.logger.info(f"Token validated successfully for client: {token_info.get('client_id')}")
            return token_info

        except requests.exceptions.Timeout:
            self.logger.error("Timeout during token introspection")
            raise OAuth2Error("Token validation timeout")
        except requests.exceptions.ConnectionError:
            self.logger.error("Connection error during token introspection")
            raise OAuth2Error("Token validation connection failed")
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"HTTP error during token introspection: {e}")
            raise OAuth2Error(f"Token validation HTTP error: {e}")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request error during token introspection: {e}")
            raise OAuth2Error("Token validation request failed")
        except json.JSONDecodeError:
            self.logger.error("Invalid JSON response from introspection endpoint")
            raise OAuth2Error("Invalid introspection response")
        except OAuth2Error:
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during token validation: {e}")
            raise OAuth2Error("Token validation unexpected error")

    def validate_auth_info(self, auth_info: str):
        """
        Validates the token provided in the auth_info dictionary.

        :param auth_info: A dictionary containing at least the key 'access_token'.
        :return: (is_valid, token_info, error_response)
        """
        token = auth_info
        if not token:
            self.logger.warning("Missing access token in auth_info")
            result=Results(auth_endpoint=self.ua_url)
            return False, None, Response(
                status=StatusCode.UNAUTHORIZED,
                status_text='Missing access token.',
                results=result
        )

        try:
            token_info = self.validate_token(token)
            self.logger.info(token_info)
            return True, token_info, None

        except OAuth2Error as e:
            self.logger.warning(f"OAuth2 validation failed: {e}")
            return False, None, Response(
                status=StatusCode.UNAUTHORIZED,
                status_text=str(e)
            )
        except Exception as e:
            self.logger.error(f"Unexpected error during authorization: {e}")
            return False, None, Response(
                status=StatusCode.INTERNALERROR,
                status_text="Token validation error"
            )


