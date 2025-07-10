""" OAuth2 Authentication Support for OpenC2 Producer """
import json
import os
from flask import Flask, request
from authlib.integrations.requests_client import OAuth2Session
import requests
import threading
import time
import queue
import logging

from otupy.core.message import Message
from otupy.core.command import Command
from otupy.core.encoder import Encoder
from otupy.core.transfer import Transfer
from otupy.core.producer import Producer


class OAuth2AuthManager:
    """Handles OAuth2 authentication"""

    def __init__(self, client_id, client_secret, redirect_uri, callback_port=8000):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.callback_port = callback_port
        self.token_path = os.path.join(os.getcwd(), 'oauth2_token.json')
        self.auth_response_queue = queue.Queue()
        self.client = OAuth2Session(self.client_id, self.client_secret,
                                    redirect_uri=self.redirect_uri)
        self.token = None
        self.flask_app = None
        self.flask_thread = None
        self.as_url = None
        self.logger = logging.getLogger('oauth2_auth')

    def setup_flask_app(self):
        """Configure Flask server to receive redirect"""
        if self.flask_app is None:
            self.flask_app = Flask(__name__)

            @self.flask_app.route('/error')
            def error():
                self.logger.error('User NOT authorized')
                self.auth_response_queue.put("ERROR")
                return 'OK', 200

            @self.flask_app.route('/callback')
            def callback():
                authorization_response = request.url
                self.auth_response_queue.put(authorization_response)
                return 'Authentication completed.', 200

    def get_token_threaded(self):
        """Thread to get token"""
        token_url = f"{self.as_url}/oauth/token"
        auth_response = self.auth_response_queue.get()
        try:
            if auth_response == "ERROR":
                raise PermissionError("User denied authorization")

            self.token = self.client.fetch_token(token_url,
                                                 authorization_response=auth_response)
            self.logger.info("Token obtained successfully")
            self.save_token_to_file()
            return self.token
        except Exception as e:
            self.logger.error(f"Error fetching the token: {e}")
            raise

    def authenticate(self, ua_url,command):
        """Starts the OAuth2 authentication process"""
        try:
            # print(command)
            action=command.action.name if hasattr(command.action, 'name') else str(command.action)
            target_type = command.target.choice
            target = [f"{target_type}.{t.name}" for t in command.target.obj]
            actuator= command.actuator.choice
            command_dict = {
                "action": action,
                "target": target,
                "actuator": actuator
            }
            response = requests.get(f"{ua_url}/as_url")
            if response.status_code != 200:
                raise Exception(f"Error fetching AS Url: {response.status_code}")

            self.as_url = response.json().get("as_url")
            as_auth_url = f"{self.as_url}/oauth/authorize"
            if not self.as_url:
                raise ValueError("Missing AS url")

            authorization_url, state = self.client.create_authorization_url(
                as_auth_url, request=None
            )
            authorization_url = authorization_url.replace("https://", "http://")
            payload = {"url": authorization_url, "command": command_dict}
            ua_auth = f"{ua_url}/auth"
            response = requests.post(ua_auth, json=payload)

            if response.status_code != 401:
                self.setup_flask_app()
                if self.flask_thread is None or not self.flask_thread.is_alive():
                    self.flask_thread = threading.Thread(
                        target=lambda: self.flask_app.run(
                            port=self.callback_port, debug=False, use_reloader=False
                        ),
                        daemon=True
                    )
                    self.flask_thread.start()
                    time.sleep(1)  # Wait tha Flask server start

                token_thread = threading.Thread(target=self.get_token_threaded, daemon=True)
                token_thread.start()

                token_thread.join(timeout=60)

                if self.token is None:
                    raise TimeoutError("Timeout fetching Token")

                if not token_thread.is_alive() and self.token is None:
                    raise PermissionError("User denied authorization")

                return self.token
            else:
                raise Exception(f"Error: {response.status_code}")

        except Exception as e:
            self.logger.error(f"Error: {e}")
            raise

    def is_authenticated(self):
        return self.token is not None

    def is_token_valid(self):
        if not self.token:
            return False
        expires_at = self.token.get("expires_at")
        if not expires_at:
            return False
        return time.time() < expires_at

    def save_token_to_file(self):
        path=self.token_path
        if self.token:
            try:
                with open(path, 'w') as f:
                    json.dump(self.token, f)
                self.logger.info("Token saved on file")
            except Exception as e:
                self.logger.error(f"Error saving token: {e}")

    def load_token_from_file(self):
        path=self.token_path
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    self.token = json.load(f)
                self.logger.info("Token loaded from file")
                return self.token
            except Exception as e:
                self.logger.error(f"Error loading token from file: {e}")
                self.token = None
        return None

class OAuth2Producer(Producer):
    """Oauth2 Producer class"""

    def __init__(self, producer, encoder, transfer, oauth2_config):
        super().__init__(producer, encoder, transfer)
        self.oauth2_manager = OAuth2AuthManager(**{k: v for k, v in oauth2_config.items()
                                                   if k not in ['consumer_url']})
        self.consumer_url = oauth2_config.get('consumer_url')
        if not self.consumer_url:
            raise ValueError("consumer_url must be specified in oauth2_config")

        self.logger = logging.getLogger('oauth2_producer')

    def authenticate(self, endpoint=None,command=None):
        """Performs OAuth2 authentication"""
        if endpoint is None:
            raise ValueError("Authentication endpoint not specified")

        self.logger.info(f"Starting OAuth2 authentication with endpoint: {endpoint}")
        token = self.oauth2_manager.authenticate(endpoint,command)
        self.logger.info("Authentication completed")
        return token

    def _extract_auth_endpoint_from_error(self, error_response):
        """Extracts the authentication endpoint from the error response"""
        try:
            parsed = json.loads(str(error_response))
            url=parsed['body']['openc2']['response']['auth_endpoint']
        except Exception as e:
            self.logger.error(f"Error extracting authentication endpoint: {e}")
        return url

    def sendcmd(self, cmd: Command, encoder: Encoder = None, transfer: Transfer = None, consumers=None):
        encoder = encoder or self.encoder
        transfer = transfer or self.transfer
        if not encoder or not transfer:
            raise ValueError("Missing encoder or transfer")

        target_consumers = consumers or [self.consumer_url]

        if not self.oauth2_manager.token or not self.oauth2_manager.is_token_valid():
            self.logger.info("Trying to load token from file")
            self.oauth2_manager.load_token_from_file()

        try:
            msg = Message(cmd, from_=self.producer, to=target_consumers)

            # First request without token
            token = self.oauth2_manager.token  #can be None
            return transfer.send(msg, encoder, token=token)

        except PermissionError as e:
            self.logger.error(f"401 Response. Starting authentication process {e}")
            auth_endpoint = self._extract_auth_endpoint_from_error(e)

            if not auth_endpoint:
                self.logger.error("Error fetching endpoint url")
                raise ValueError("Error fetching endpoint url")

            try:
                self.authenticate(endpoint=auth_endpoint,command=cmd)

                # Retry sending of the message
                token = self.oauth2_manager.token
                msg = Message(cmd, from_=self.producer, to=target_consumers)
                return transfer.send(msg, encoder, token=token)

            except Exception as auth_exc:
                self.logger.error(f"Authentication failed {auth_exc}")
                raise auth_exc
        except Exception as e:
            self.logger.error(f"Error sending the command {e}")
            raise e

    def is_authenticated(self):
        return self.oauth2_manager.is_authenticated()

    def get_token_info(self):
        return self.oauth2_manager.token
