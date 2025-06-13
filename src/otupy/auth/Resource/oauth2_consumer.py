"""OAuth2 Consumer Wrapper

Wrapper che implementa le funzioni del Consumer OpenC2 con validazione OAuth2.
Il Consumer agisce come Resource Server e valida i token tramite introspection
verso l'Authorization Server.
"""

import logging
from typing import Optional, Dict, Any, List
import requests
from authlib.oauth2.rfc7662 import IntrospectTokenValidator
from authlib.oauth2 import OAuth2Error
import json
from datetime import datetime, timezone

from otupy.core.message import Message
from otupy.core.response import Response, StatusCode, StatusCodeDescription

logger = logging.getLogger(__name__)


class OAuth2TokenValidator(IntrospectTokenValidator):
    """Validatore OAuth2 per token introspection basato su authlib"""

    def __init__(self,
                 introspection_url: str,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None,
                 required_scopes: Optional[List[str]] = None,
                 timeout: int = 10):
        """
        Inizializza il validatore OAuth2

        :param introspection_url: URL dell'endpoint di introspection dell'Authorization Server
        :param client_id: Client ID per l'autenticazione con l'Authorization Server
        :param client_secret: Client Secret per l'autenticazione
        :param required_scopes: Lista degli scope richiesti (opzionale)
        :param timeout: Timeout per le richieste HTTP in secondi
        """
        super().__init__()
        self.introspection_url = introspection_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.required_scopes = required_scopes or []
        self.timeout = timeout

    def introspect_token(self, token_string: str) -> Dict[str, Any]:
        """
        Implementazione del metodo di introspection richiesto da authlib

        :param token_string: Token da validare
        :return: Risultato dell'introspection
        """
        data = {
            'token': token_string,
            'token_type_hint': 'access_token'
        }
        auth = None
        if self.client_id and self.client_secret:
            auth = (self.client_id, self.client_secret)

        resp = requests.post(
            self.introspection_url,
            data=data,
            auth=auth,
            timeout=self.timeout
        )
        print(resp.content)
        resp.raise_for_status()
        return resp.json()

    def validate_token(self, token: str) -> Dict[str, Any]:
        """
        Valida un token tramite introspection con controlli aggiuntivi

        :param token: Token da validare
        :return: Risultato dell'introspection
        :raises OAuth2Error: Se il token non è valido
        """
        try:
            # Usa il metodo introspect_token di authlib
            token_info = self.introspect_token(token)

            # Verifica se il token è attivo
            if not token_info.get('active', False):
                logger.warning("Token is not active")
                raise OAuth2Error("Token is not active")

            # Verifica gli scope se richiesti
            # if self.required_scopes:
            #     token_scopes = token_info.get('scope', '').split()
            #     missing_scopes = set(self.required_scopes) - set(token_scopes)
            #     if missing_scopes:
            #         logger.warning(f"Missing required scopes: {missing_scopes}")
            #         raise OAuth2Error(f"Insufficient scope. Missing: {', '.join(missing_scopes)}")

            # Verifica la scadenza
            exp = token_info.get('exp')
            if exp and datetime.fromtimestamp(exp, timezone.utc) < datetime.now(timezone.utc):
                logger.warning("Token has expired")
                raise OAuth2Error("Token has expired")

            logger.info(f"Token validated successfully for client: {token_info.get('client_id', 'unknown')}")
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
        except Exception as e:
            logger.error(f"Unexpected error during token validation: {e}")
            raise OAuth2Error("Token validation unexpected error")


class OAuth2ConsumerWrapper:
    """
    Wrapper OAuth2 per il Consumer OpenC2

    Questo wrapper agisce come Resource Server e valida i token OAuth2
    prima di inoltrare i comandi al Consumer originale.
    """

    def __init__(self,
                 consumer,
                 oauth2_validator: OAuth2TokenValidator,
                 token_header: str = 'Authorization',
                 token_prefix: str = 'Bearer '):
        """
        Inizializza il wrapper OAuth2

        :param consumer: Istanza del Consumer OpenC2 originale
        :param oauth2_validator: Validatore OAuth2
        :param token_header: Nome dell'header che contiene il token (default: 'Authorization')
        :param token_prefix: Prefisso del token (default: 'Bearer ')
        """
        self.consumer = consumer
        self.oauth2_validator = oauth2_validator
        self.token_header = token_header
        self.token_prefix = token_prefix
        logger.info("OAuth2 Consumer Wrapper initialized")

    def extract_token(self, headers: dict) -> Optional[str]:
        """
        Estrae il token OAuth2 dagli header HTTP

        :param headers: Dizionario degli header HTTP
        :return: Token estratto o None se non trovato
        """
        auth_header = headers.get(self.token_header)
        print(auth_header)
        if auth_header and auth_header.startswith(self.token_prefix):
            return auth_header[len(self.token_prefix):]

        logger.warning("No OAuth2 token found in HTTP headers")
        return None

    def validate_message(self, msg: Message, headers: dict) -> tuple[
        bool, Optional[Dict[str, Any]], Optional[Response]]:
        """
        Valida il messaggio OAuth2

        :param msg: Messaggio da validare
        :param headers: Header HTTP contenente l'access token
        :return: Tupla (is_valid, token_info, error_response)
        """
        try:
            # Estrai il token
            token = self.extract_token(headers)
            if not token:
                error_response = Response(
                    status=StatusCode.UNAUTHORIZED,
                    status_text="Missing access token"
                )
                return False, None, error_response

            token_info = self.oauth2_validator.validate_token(token)

            logger.info(f"Message validated for client: {token_info.get('client_id', 'unknown')}\n")
            return True, token_info, None

        except OAuth2Error as e:
            logger.warning(f"OAuth2 validation failed: {e}")
            error_response = Response(
                status=StatusCode.UNAUTHORIZED,
                status_text=str(e)
            )
            return False, None, error_response
        except Exception as e:
            logger.error(f"Unexpected error during validation: {e}")
            error_response = Response(
                status=StatusCode.INTERNALERROR,
                status_text="Token validation error"
            )
            return False, None, error_response

    def dispatch(self, msg: Message, headers: dict) -> Message:
        """
        Dispatch protetto da OAuth2

        Valida il token OAuth2 prima di inoltrare al Consumer originale

        :param msg: Messaggio OpenC2 da processare
        :return: Messaggio di risposta
        """
        logger.info("Processing message with OAuth2 validation")

        # Valida il messaggio OAuth2
        is_valid, token_info, error_response = self.validate_message(msg, headers)

        if not is_valid:
            # Restituisci errore di validazione
            error_msg = self._create_error_message(msg, error_response)
            return error_msg

        # Aggiungi informazioni del token al messaggio (opzionale)
        if token_info:
            if not hasattr(msg, 'metadata'):
                msg.metadata = {}
            msg.metadata.update({
                'oauth2_client_id': token_info.get('client_id'),
                'oauth2_scopes': token_info.get('scope', '').split(),
                'oauth2_subject': token_info.get('sub'),
                'oauth2_validated_at': datetime.now(timezone.utc).isoformat()
            })

        try:
            logger.info("Forwarding validated message to original consumer")
            response_msg = self.consumer.dispatch(msg)
            return response_msg
        except Exception as e:
            logger.error(f"Error in original consumer dispatch: {e}")
            error_response = Response(
                status=StatusCode.INTERNALERROR,
                status_text="Internal processing error"
            )
            return self._create_error_message(msg, error_response)

    def _create_error_message(self, original_msg: Message, error_response: Response) -> Message:
        """
        Crea un messaggio di errore

        :param original_msg: Messaggio originale
        :param error_response: Risposta di errore
        :return: Messaggio di errore formattato
        """
        return self.consumer._Consumer__respmsg(original_msg, error_response)

    def run(self, encoder=None, transfer=None):
        """
        Avvia il Consumer con protezione OAuth2

        :param encoder: Encoder da utilizzare
        :param transfer: Transfer protocol da utilizzare
        """
        if not encoder:
            encoder = self.consumer.encoder
        if not transfer:
            transfer = self.consumer.transfer
        if not transfer:
            raise ValueError('Missing transfer object')

        logger.info("Starting OAuth2-protected Consumer")
        transfer.receive(self.dispatch, encoder)


def create_oauth2_consumer(consumer,
                           introspection_url: str,
                           client_id: Optional[str] = None,
                           client_secret: Optional[str] = None,
                           required_scopes: Optional[List[str]] = None):
    """
    Factory function per creare un Consumer protetto da OAuth2

    :param consumer: Consumer OpenC2 originale
    :param introspection_url: URL dell'endpoint di introspection
    :param client_id: Client ID
    :param client_secret: Client Secret
    :param required_scopes: Scope richiesti
    :return: Consumer wrapper protetto da OAuth2
    """
    validator = OAuth2TokenValidator(
        introspection_url=introspection_url,
        client_id=client_id,
        client_secret=client_secret,
        required_scopes=required_scopes
    )

    return OAuth2ConsumerWrapper(consumer, validator)
