""" OAuth2 Authentication Support for OpenC2 Producer """
import json

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
        self.as_url=None
        self.logger = logging.getLogger('oauth2_auth')

    def setup_flask_app(self):
        """Configura il server Flask per ricevere il redirect"""
        if self.flask_app is None:
            self.flask_app = Flask(__name__)

            @self.flask_app.route('/callback')
            def callback():
                authorization_response = request.url
                self.auth_response_queue.put(authorization_response)
                return 'Autenticazione completata.', 200

    def get_token_threaded(self):
        """Thread per ottenere il token"""
        token_url=f"{self.as_url}/oauth/token"
        auth_response = self.auth_response_queue.get()
        try:
            self.token = self.client.fetch_token(token_url,
                                                 authorization_response=auth_response)
            self.logger.info("TOKEN ottenuto correttamente")
            return self.token
        except Exception as e:
            self.logger.error(f"Errore nel fetch del token: {e}")
            raise

    def authenticate(self, ua_url):
        """Avvia il processo di autenticazione OAuth2, contattando lo UA passato come parametro"""
        try:
            response = requests.get(f"{ua_url}/as_url")
            if response.status_code != 200:
                raise Exception(f"Error fetching AS Url: {response.status_code}")

            self.as_url = response.json().get("as_url")
            as_auth_url=f"{self.as_url}/oauth/authorize"
            if not self.as_url:
                raise ValueError("Missing AS url")

            authorization_url, state = self.client.create_authorization_url(
                as_auth_url, request=None
            )
            authorization_url = authorization_url.replace("https://", "http://")
            payload = {"url": authorization_url}
            ua_auth=f"{ua_url}/auth"
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
                    time.sleep(1)  # Aspetta che Flask si avvi

                token_thread = threading.Thread(target=self.get_token_threaded, daemon=True)
                token_thread.start()

                token_thread.join(timeout=60)

                if self.token is None:
                    raise TimeoutError("Timeout fetching Token")

                return self.token
            else:
                raise Exception(f"Error: {response.status_code}")

        except Exception as e:
            self.logger.error(f"Error: {e}")
            raise

    def is_authenticated(self):
        return self.token is not None


class OAuth2Producer(Producer):
    """Producer OpenC2 con supporto OAuth2"""

    def __init__(self, producer, encoder, transfer, oauth2_config):
        super().__init__(producer, encoder, transfer)
        self.oauth2_manager = OAuth2AuthManager(**{k: v for k, v in oauth2_config.items()
                                                   if k not in ['consumer_url']})
        self.consumer_url = oauth2_config.get('consumer_url')
        if not self.consumer_url:
            raise ValueError("consumer_url deve essere specificato in oauth2_config")

        self.logger = logging.getLogger('oauth2_producer')

    def authenticate(self, endpoint=None):
        """Esegue l'autenticazione OAuth2"""
        if endpoint is None:
            raise ValueError("Endpoint di autenticazione non specificato")

        self.logger.info(f"Avvio autenticazione OAuth2 con endpoint: {endpoint}")
        token = self.oauth2_manager.authenticate(endpoint)
        self.logger.info("Autenticazione completata")
        return token

    def _extract_auth_endpoint_from_error(self, error_response):
        """Estrae l'endpoint di autenticazione dalla risposta di errore"""
        try:
            parsed=json.loads(str(error_response))
            res=parsed['body']['openc2']['response']['status_text']
            url = res.split(":", 1)[1].strip()
        except Exception as e:
            self.logger.error(f"Errore nell'estrazione dell'endpoint di autenticazione: {e}")

        return url

    def sendcmd(self, cmd: Command, encoder: Encoder = None, transfer: Transfer = None, consumers=None):
        encoder = encoder or self.encoder
        transfer = transfer or self.transfer
        if not encoder or not transfer:
            raise ValueError("Missing encoder or transfer")

        target_consumers = consumers or [self.consumer_url]

        try:
            msg = Message(cmd, from_=self.producer, to=target_consumers)

            # Prima richiesta senza token
            token = self.oauth2_manager.token
            return transfer.send(msg, encoder, token=token)

        except PermissionError as e:
            self.logger.error(f"Rilevato errore 401 dal consumer, avvio processo di autenticazione {e}")
            auth_endpoint = self._extract_auth_endpoint_from_error(e)

            if not auth_endpoint:
                self.logger.error("Impossibile determinare l'endpoint di autenticazione dalla risposta 401")
                raise ValueError("Endpoint di autenticazione non trovato nella risposta 401")

            try:
                self.authenticate(endpoint=auth_endpoint)

                # Riprova l'invio del comando con il token
                token = self.oauth2_manager.token
                msg = Message(cmd, from_=self.producer, to=target_consumers)
                return transfer.send(msg, encoder, token=token)

            except Exception as auth_exc:
                self.logger.error(f"Autenticazione fallita: {auth_exc}")
                raise auth_exc
        except Exception as e:
            self.logger.error(f"Errore nell'invio del comando: {e}")
            raise e

    def is_authenticated(self):
        return self.oauth2_manager.is_authenticated()

    def get_token_info(self):
        return self.oauth2_manager.token
