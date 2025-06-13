""" OAuth2 Authentication Wrapper for OpenC2 Producer

    This module provides OAuth2 authentication capabilities for the existing Producer class
    without modifying the original code.
"""
from flask import Flask, request
from authlib.integrations.requests_client import OAuth2Session
import requests
import threading
import time
import queue
import logging

from otupy.types.data import DateTime
from otupy.core.message import Content
from otupy.core.command import Command
from otupy.core.encoder import Encoder
from otupy.core.transfer import Transfer
from otupy.core.message import Message
from otupy.core.producer import Producer  # Import del Producer originale


class OAuth2AuthManager:
    """Gestisce l'autenticazione OAuth2"""
    
    def __init__(self, client_id, client_secret, authorize_url, token_url, 
                 redirect_uri, ua_url, callback_port=8000):
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.AUTHORIZE_URL = authorize_url
        self.TOKEN_URL = token_url
        self.REDIRECT_URI = redirect_uri
        self.UA_URL = ua_url
        self.callback_port = callback_port
        
        self.auth_response_queue = queue.Queue()
        self.client = OAuth2Session(self.CLIENT_ID, self.CLIENT_SECRET, 
                                   redirect_uri=self.REDIRECT_URI)
        self.token = None
        self.flask_app = None
        self.flask_thread = None
        self.logger = logging.getLogger('oauth2_auth')
        
    def setup_flask_app(self):
        """Configura l'app Flask per gestire il callback OAuth2"""
        if self.flask_app is None:
            self.flask_app = Flask(__name__)
            
            @self.flask_app.route('/callback')
            def callback():
                self.logger.info("Ricevuto callback OAuth2")
                authorization_response = request.url
                self.auth_response_queue.put(authorization_response)
                return 'Autenticazione completata. Puoi chiudere questa finestra.', 200
                
    def get_token_threaded(self):
        """Thread per ottenere il token OAuth2"""
        self.logger.info("In attesa dell'authorization_response")
        auth_response = self.auth_response_queue.get()
        self.logger.info(f"Authorization_response ricevuto")
        
        try:
            self.token = self.client.fetch_token(self.TOKEN_URL, 
                                               authorization_response=auth_response)
            self.logger.info("TOKEN ottenuto correttamente")
            return self.token
        except Exception as e:
            self.logger.error(f"Errore nel fetch del token: {e}")
            raise
            
    def authenticate(self):
        """Avvia il processo di autenticazione OAuth2"""
        try:
            authorization_url, state = self.client.create_authorization_url(
                self.AUTHORIZE_URL, request=None)
            authorization_url = authorization_url.replace("https://", "http://")
            
            payload = {"url": authorization_url}
            response = requests.post(self.UA_URL, json=payload)
            self.logger.info(f"Response dalla UA: {response.status_code}")
            
            if response.status_code != 401:
                # Setup Flask app
                self.setup_flask_app()
                
                # Avvia Flask server in thread separato
                if self.flask_thread is None or not self.flask_thread.is_alive():
                    self.flask_thread = threading.Thread(
                        target=lambda: self.flask_app.run(
                            port=self.callback_port, debug=False, use_reloader=False
                        ), daemon=True
                    )
                    self.flask_thread.start()
                    time.sleep(1)  # Attendi che Flask si avvii
                
                # Avvia il thread per ottenere il token
                token_thread = threading.Thread(target=self.get_token_threaded, daemon=True)
                token_thread.start()
                
                # Aspetta che il token sia ottenuto
                token_thread.join(timeout=60)  # Timeout di 60 secondi
                
                if self.token is None:
                    raise TimeoutError("Timeout nell'ottenimento del token OAuth2")
                    
                return self.token
            else:
                raise Exception(f"Errore nella richiesta di autorizzazione: {response.status_code}")
                
        except Exception as e:
            self.logger.error(f"Errore durante l'autenticazione: {e}")
            raise
            
    def get_auth_headers(self):
        """Restituisce gli headers di autenticazione per le richieste"""
        if self.token is None:
            raise ValueError("Token non disponibile. Eseguire prima l'autenticazione.")
        return {
            'Authorization': f"Bearer {self.token.get('access_token')}"
        }
        
    def is_authenticated(self):
        """Verifica se il client è autenticato"""
        return self.token is not None


class OAuth2ProducerWrapper:
    """Wrapper che aggiunge OAuth2 al Producer esistente senza modificarlo"""
    
    def __init__(self, producer_id, encoder, transfer, oauth2_config, auto_authenticate=True):
        """
        :param producer_id: ID del producer
        :param encoder: Encoder da utilizzare
        :param transfer: Transfer da utilizzare
        :param oauth2_config: Configurazione OAuth2
        :param auto_authenticate: Se True, autentica automaticamente
        """
        self.oauth2_manager = OAuth2AuthManager(**oauth2_config)
        self.logger = logging.getLogger('oauth2_producer_wrapper')
        self.encoder = encoder
        self.transfer = transfer
        
        # Crea il transfer autenticato
        # self.authenticated_transfer = AuthenticatedTransfer(transfer, self.oauth2_manager)
        
        # Crea il Producer originale con il transfer autenticato
        # self.producer = Producer(producer_id, encoder, self.authenticated_transfer)
        self.producer = Producer(producer_id,encoder)

        if auto_authenticate:
            self.authenticate()
            
    def authenticate(self):
        """Esegue l'autenticazione OAuth2"""
        self.logger.info("Avvio autenticazione OAuth2")
        token = self.oauth2_manager.authenticate()
        self.logger.info("Autenticazione completata")
        return token

    def sendcmd(self, cmd: Command, encoder: Encoder = None, transfer: Transfer = None, consumers = None):
        """Send command with OAuth2 token authentication support"""
    
        if not encoder: 
            encoder = self.encoder
        if not transfer: 
            transfer = self.transfer
        if not transfer: 
            raise ValueError('Missing transfer object')
        if not encoder: 
            raise ValueError('Missing encoder object')
        
        msg = Message(cmd)
        msg.from_ = self.producer
        msg.to = consumers
        
        # Add OAuth2 token to HTTP headers if available and transfer supports it
        if hasattr(self, 'oauth2_manager') and self.oauth2_manager.is_authenticated():
            auth_headers = self.oauth2_manager.get_auth_headers()
            
            # Check if transfer is HTTPTransfer and add headers
            if hasattr(transfer, 'url') and hasattr(transfer, 'send'):  # HTTPTransfer detection
                # For HTTPTransfer, we need to modify the send method to include auth headers
                original_send = transfer.send
                
                def authenticated_send(msg, encoder):
                    # Get the original HTTP data
                    openc2data = transfer._tohttp(msg, encoder)
                    
                    # Build headers with authentication
                    content_type = f"application/{msg.content_type}+{encoder.getName()};version={msg.version}"
                    date = msg.created if msg.created else int(DateTime())
                    openc2headers = {
                        'Content-Type': content_type, 
                        'Accept': content_type, 
                        'Date': DateTime(date).httpdate()
                    }
                    
                    # Add OAuth2 authorization header
                    openc2headers.update(auth_headers)
                    
                    self.logger.info("Sending to %s with OAuth2 authentication", transfer.url)
                    self.logger.info("HTTP Request Content:\n%s", openc2data)
                    
                    # Send the authenticated request
                    if transfer.scheme == 'https':
                        self.logger.warning("Certificate validation disabled!")
                    response = requests.post(transfer.url, data=openc2data, headers=openc2headers, verify=False)
                    self.logger.info("HTTP got response: %s", response)
                    self.logger.info("HTTP Response Content:\n%s", response.text)
                    
                    # Process response (same as original HTTPTransfer)
                    try:
                        if response.status_code >=400:
                            self.logger.error("HTTP error: %s", response.status_code)
                            return None
                        if response.text != "":
                            msg, encoder = transfer._fromhttp(response.headers, response.text)
                        else:
                            msg = None
                    except ValueError as e:
                        msg = Message(Content())
                        msg.status = response.status_code
                        self.logger.error("Unable to parse data: >%s<", response.text)
                        self.logger.error(str(e))
                    
                    return msg
                
                # Temporarily replace the send method
                transfer.send = authenticated_send
                result = transfer.send(msg, encoder)
                # Restore original send method
                transfer.send = original_send
                return result
            
            # For other transfer types that might support headers directly
            elif hasattr(transfer, 'headers'):
                if transfer.headers is None:
                    transfer.headers = {}
                transfer.headers.update(auth_headers)
            elif hasattr(transfer, 'set_headers'):
                transfer.set_headers(auth_headers)
        
        # Default behavior - send without authentication
        return transfer.send(msg, encoder)

    def is_authenticated(self):
        """Verifica se il producer è autenticato"""
        return self.oauth2_manager.is_authenticated()
        
    def get_token_info(self):
        """Restituisce informazioni sul token corrente"""
        return self.oauth2_manager.token
        
    def __getattr__(self, name):
        """Delega tutti gli altri metodi al Producer originale"""
        return getattr(self.producer, name)

