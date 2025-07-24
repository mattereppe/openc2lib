from otupy.auth.Authenticator import Authenticator
import os
import json
from flask import Flask, request
from authlib.integrations.requests_client import OAuth2Session
import requests
import threading
import time
import queue
import logging


class OAuth2Authenticator(Authenticator):
    def __init__(self, client_id, client_secret, consumer_url, redirect_uri, callback_port=8000 ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.consumer_url = consumer_url
        self.redirect_uri = redirect_uri
        self.callback_port = callback_port
        self.auth_response_queue = queue.Queue()
        self.client = OAuth2Session(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri
        )
        self.token = None
        self.flask_app = None
        self.flask_thread = None
        self.as_url = None
        self.ua_url = None
        self.logger = logging.getLogger('oauth2_auth')

    def setup_flask_app(self):
        """Configure Flask server to receive redirect"""
        if self.flask_app is None:
            self.flask_app = Flask(__name__)

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
            self.token = self.client.fetch_token(token_url,
                                                 authorization_response=auth_response)
            self.logger.info("Token obtained successfully")
            return self.token
        except Exception as e:
            self.logger.error(f"Error fetching the token: {e}")
            raise

    def authenticate(self, ua_url):
        """Starts the OAuth2 authentication process"""
        try:
            self.ua_url = ua_url
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
            payload = {"url": authorization_url}
            ua_auth = f"{ua_url}/authenticate"
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

    def extract_auth_endpoint_from_error(self, error_response):
        """Extracts the authentication endpoint from the error response"""
        try:
            parsed = json.loads(str(error_response))
            url = parsed['body']['openc2']['response']['results']['auth_endpoint']
        except Exception as e:
            self.logger.error(f"Error extracting authentication endpoint: {e}")
        return url
