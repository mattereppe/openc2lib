import logging
from typing import Optional, Dict, Any, List, Tuple
import requests
from authlib.oauth2.rfc7662 import IntrospectTokenValidator
from authlib.oauth2 import OAuth2Error
import json
from datetime import datetime, timezone

from otupy.core.results import Results
from otupy.core.message import Message
from otupy.core.response import Response, StatusCode
from otupy.core.consumer import Consumer

logger = logging.getLogger(__name__)


class OAuth2TokenValidator(IntrospectTokenValidator):
    """Validatore OAuth2 per token introspection"""

    def __init__(self,
                 introspection_url: str,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 required_scopes: Optional[List[str]] = None,
                 timeout: int = 10):
        super().__init__()
        self.introspection_url = introspection_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.required_scopes = required_scopes or []
        self.timeout = timeout

    def introspect_token(self, token_string: str) -> Dict[str, Any]:
        """Token introspection"""
        data = {
            'token': token_string,
            'token_type_hint': 'access_token'
        }
        auth = None
        if self.client_id and self.client_secret:
            auth = (self.client_id, self.client_secret)

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
            logger.error(f"Token introspection request failed: {e}")
            raise

    def validate_token(self, token: str) -> Dict[str, Any]:
        """Validates the token and returns the information"""
        try:
            token_info = self.introspect_token(token)

            # Check if the token is active
            if not token_info.get('active', False):
                logger.warning("Token is not active")
                raise OAuth2Error("Token is not active")

            # Check if token has expired
            exp = token_info.get('exp')
            if exp and datetime.fromtimestamp(exp, timezone.utc) < datetime.now(timezone.utc):
                logger.warning("Token has expired")
                raise OAuth2Error("Token has expired")

            # Check token scopes
            # if self.required_scopes:
            #     token_scopes = token_info.get('scope', '').split()
            #     missing_scopes = set(self.required_scopes) - set(token_scopes)
            #     if missing_scopes:
            #         logger.warning(f"Token missing required scopes: {missing_scopes}")
            #         raise OAuth2Error(f"Insufficient scopes. Missing: {', '.join(missing_scopes)}")

            logger.info(f"Token validated successfully for client: {token_info.get('client_id')}")
            return token_info

        except requests.exceptions.Timeout:
            logger.error("Timeout during token introspection")
            raise OAuth2Error("Token validation timeout")
        except requests.exceptions.ConnectionError:
            logger.error("Connection error during token introspection")
            raise OAuth2Error("Token validation connection failed")
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error during token introspection: {e}")
            raise OAuth2Error(f"Token validation HTTP error: {e}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error during token introspection: {e}")
            raise OAuth2Error("Token validation request failed")
        except json.JSONDecodeError:
            logger.error("Invalid JSON response from introspection endpoint")
            raise OAuth2Error("Invalid introspection response")
        except OAuth2Error:
            raise
        except Exception as e:
            logger.error(f"Unexpected error during token validation: {e}")
            raise OAuth2Error("Token validation unexpected error")


class OAuth2Consumer(Consumer):
    """
    Oauth2 extension of Consumer
    """

    def __init__(self,
                 consumer: str,
                 introspection_url: str,
                 ua_url: str,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 required_scopes: Optional[List[str]] = None,
                 actuators: Optional[List] = None,
                 encoder=None,
                 transfer=None):
        super().__init__(consumer, actuators or [], encoder, transfer)
        self.oauth2_validator = OAuth2TokenValidator(
            introspection_url=introspection_url,
            client_id=client_id,
            client_secret=client_secret,
            required_scopes=required_scopes
        )
        self.ua_url = ua_url
        self._current_token = None  # Store current token for __runcmd
        logger.info(f"OAuth2Consumer initialized with introspection URL: {introspection_url}")
        logger.info(f"Auth endpoint: {self.ua_url}")

    def dispatch(self, msg: Message, token: Optional[str] = None) -> Message:
        """
        Dispatch with Oauth2 validation

        :param msg: OpenC2 Message
        :param token: Access token to be validated (extract from Transfer.receive())
        :return: Response message
        """
        logger.info("Processing message with OAuth2 validation")

        # Store token
        self._current_token = token
        return super().dispatch(msg)

    def _runcmd(self, msg, actuator):
        """
        Performs token validation before executing the command.
        :param msg: The OpenC2 message
        :param actuator: The actuator to execute the command
        :return: Response object
        """
        # Perform token validation before command execution
        is_valid, token_info, error_response = self.is_authorized(self._current_token)

        if not is_valid:
            logger.warning("Token validation failed during command execution")
            return Response(
                status=StatusCode.UNAUTHORIZED,
                status_text=f"Unauthorized: {error_response.status_text if error_response else 'Invalid token'}"
            )

        logger.info("Token validated successfully, proceeding with command execution")

        try:
            logger.info("Dispatching command to: %s", actuator[0])
            response_content = actuator[0].run(msg.content)
        except (IndexError, AttributeError):
            response_content = Response(status=StatusCode.NOTFOUND, status_text='No actuator available')

        return response_content

    def is_authorized(self, token: Optional[str]) -> Tuple[bool, Optional[Dict[str, Any]], Optional[Response]]:
        """
        Token Authorization Check

        :param token: Token extracted from Transfer
        :return: (is_valid, token_info, error_response)
        """
        if not token:
            logger.warning("Missing access token in request")
            return False, None, Response(
                status=StatusCode.UNAUTHORIZED,
                status_text="Missing access token"
            )

        try:
            token_info = self.oauth2_validator.validate_token(token)
            logger.info("Token validation successful")
            return True, token_info, None

        except OAuth2Error as e:
            logger.warning(f"OAuth2 validation failed: {e}")
            return False, None, Response(
                status=StatusCode.UNAUTHORIZED,
                status_text=str(e)
            )
        except Exception as e:
            logger.error(f"Unexpected error during authorization: {e}")
            return False, None, Response(
                status=StatusCode.INTERNALERROR,
                status_text="Token validation error"
            )

    def _create_error_message(self, original_msg):
        """
        Create an OAuth2 unauthorized error message with authentication endpoint info
        """
        auth_info = f"Auth endpoint: {self.ua_url} "
        response = Response(
            status=StatusCode.UNAUTHORIZED,
            status_text=auth_info
        )

        error_msg = Message(content=response)
        error_msg.status = StatusCode.UNAUTHORIZED
        error_msg.from_ = "consumer"
        error_msg.to = getattr(original_msg, 'from_', None)
        error_msg.request_id = getattr(original_msg, 'request_id', None)

        return error_msg