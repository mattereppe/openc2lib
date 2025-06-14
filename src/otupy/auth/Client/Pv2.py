""" OAuth2 Authentication Support for OpenC2 Producer """

from flask import Flask, request
from authlib.integrations.requests_client import OAuth2Session
import requests
import threading
import time
import queue
import logging

from otupy.types.data import DateTime
from otupy.core.message import Content, Message
from otupy.core.command import Command
from otupy.core.encoder import Encoder
from otupy.core.transfer import Transfer
from otupy.core.producer import Producer


class OAuth2AuthManager:
    """Gestisce l'autenticazione OAuth2"""

    def __init__(self, client_id, client_secret, redirect_uri, callback_port=8000):
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.REDIRECT_URI = redirect_uri
        self.callback_port = callback_port

        self.auth_response_queue = queue.Queue()
        self.client = OAuth2Session(self.CLIENT_ID, self.CLIENT_SECRET,
                                    redirect_uri=self.REDIRECT_URI)
        self.token = None
        self.flask_app = None
        self.flask_thread = None
        self.logger = logging.getLogger('oauth2_auth')

    def setup_flask_app(self):
        """Configura il server Flask per ricevere il redirect"""
        if self.flask_app is None:
            self.flask_app = Flask(__name__)

            @self.flask_app.route('/callback')
            def callback():
                authorization_response = request.url
                self.auth_response_queue.put(authorization_response)
                return 'Autenticazione completata. Puoi chiudere questa finestra.', 200

    def get_token_threaded(self, token_url):
        """Thread per ottenere il token"""
        auth_response = self.auth_response_queue.get()
        try:
            self.token = self.client.fetch_token(token_url,
                                                 authorization_response=auth_response)
            return self.token
        except Exception as e:
            self.logger.error(f"Errore nel fetch del token: {e}")
            raise

    def authenticate(self, endpoint):
        """Avvia autenticazione verso l'endpoint specificato dal Consumer"""
        try:
            response = requests.get(endpoint)
            if response.status_code != 200:
                raise Exception(f"Endpoint di autorizzazione non disponibile: {response.status_code}")

            data = response.json()
            authorize_url = data["authorize_url"]
            token_url = data["token_url"]

            auth_url, state = self.client.create_authorization_url(authorize_url)
            requests.post(endpoint, json={"url": auth_url})  # invio richiesta all'UA

            self.setup_flask_app()
            if self.flask_thread is None or not self.flask_thread.is_alive():
                self.flask_thread = threading.Thread(
                    target=lambda: self.flask_app.run(port=self.callback_port, debug=False, use_reloader=False),
                    daemon=True
                )
                self.flask_thread.start()
                time.sleep(1)

            token_thread = threading.Thread(target=self.get_token_threaded, args=(token_url,), daemon=True)
            token_thread.start()
            token_thread.join(timeout=60)

            if self.token is None:
                raise TimeoutError("Timeout nell'ottenimento del token")

            return self.token
        except Exception as e:
            self.logger.error(f"Errore durante autenticazione: {e}")
            raise

    def get_auth_headers(self):
        if self.token is None:
            raise ValueError("Token non disponibile.")
        return {'Authorization': f"Bearer {self.token.get('access_token')}"}

    def is_authenticated(self):
        return self.token is not None


class OAuth2Producer(Producer):
    """Producer OpenC2 con supporto OAuth2"""

    def __init__(self, producer_id, encoder, transfer, oauth2_config, auto_authenticate=True):
        super().__init__(producer_id, encoder, transfer)
        self.oauth2_manager = OAuth2AuthManager(**oauth2_config)
        self.logger = logging.getLogger('oauth2_producer')
        if auto_authenticate:
            self.authenticate()

    def authenticate(self, endpoint=None):
        """Esegue l'autenticazione OAuth2"""
        self.logger.info("Avvio autenticazione OAuth2")
        token = self.oauth2_manager.authenticate(endpoint)
        self.logger.info("Autenticazione completata")
        return token

    def sendcmd(self, cmd: Command, encoder: Encoder = None, transfer: Transfer = None, consumers=None):
        encoder = encoder or self.encoder
        transfer = transfer or self.transfer
        if not encoder or not transfer:
            raise ValueError("Missing encoder or transfer")

        token = self.oauth2_manager.token

        try:
            msg=Message(cmd, from_=self.producer, to=consumers)
            return transfer.send(msg, encoder, token=token)
        except Exception as e:
            # Tentativo di recupero se 401 (no autorizzato)
            if hasattr(e, 'response') and e.response.status_code == 401:
                try:
                    ua_endpoint = e.response.json().get("redirect_uri")
                    self.logger.warning("Ricevuto 401, inizio autenticazione con endpoint: %s", ua_endpoint)
                    self.authenticate(endpoint=ua_endpoint)
                    token = self.oauth2_manager.token
                    return transfer.send(Message(cmd, from_=self.producer, to=consumers), encoder, token=token)
                except Exception as auth_exc:
                    self.logger.error(f"Autenticazione fallita: {auth_exc}")
                    raise auth_exc
            else:
                raise e

    def is_authenticated(self):
        return self.oauth2_manager.is_authenticated()

    def get_token_info(self):
        return self.oauth2_manager.token
