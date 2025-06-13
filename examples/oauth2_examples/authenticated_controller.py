#!../.oc2-env/bin/python3
# Example to use the OpenC2 library with OAuth2 authentication
#

import logging
import sys

from otupy.encoders.json import JSONEncoder
from otupy.transfers.http import HTTPTransfer
import otupy as oc2
import otupy.profiles.slpf as slpf

from otupy.core.producer import Producer  # Producer originale
from otupy.auth.Client.oauth2_producer import OAuth2ProducerWrapper

# Setup logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('openc2producer')


def main_with_oauth2():
    """Esempio di utilizzo con autenticazione OAuth2"""
    logger.info("Creating Producer with OAuth2 authentication")

    # Configurazione OAuth2
    oauth2_config = {
        'client_id': 'FXEHY5cASqiO2a6TDVJQcR2X',
        'client_secret': 'zdZ6zawQaOINAhfNxlwhsyRFD5aREUFCkL2Bqxu77g5B82Xb',
        'authorize_url': 'http://127.0.0.1:9000/oauth/authorize',
        'token_url': 'http://127.0.0.1:9000/oauth/token',
        'redirect_uri': 'http://127.0.0.1:8000/callback',
        'ua_url': 'http://127.0.0.1:7000/auth',
        'callback_port': 8000
    }

    # Crea il Producer autenticato usando il wrapper
    p = OAuth2ProducerWrapper(
        "producer.example.net",
        JSONEncoder(),
        HTTPTransfer("127.0.0.1", 8080),
        oauth2_config=oauth2_config,
        auto_authenticate=True  # Autentica automaticamente
    )

    # Verifica che l'autenticazione sia andata a buon fine
    if not p.is_authenticated():
        logger.error("Autenticazione fallita!")
        return

    logger.info("Autenticazione OAuth2 completata")
    token_info = p.get_token_info()
    logger.info(f"Token info: {token_info}")

    # Configurazione del comando come nell'esempio originale
    pf = slpf.Specifiers({
        'hostname': 'firewall',
        'named_group': 'firewalls',
        'asset_id': 'iptables'
    })

    arg = slpf.Args({'response_requested': oc2.ResponseType.complete})

    # Vari esempi di comandi
    commands = [
        # Query per versioni, profili e coppie
        oc2.Command(oc2.Actions.query,
                    oc2.Features([oc2.Feature.versions, oc2.Feature.profiles, oc2.Feature.pairs]),
                    arg, actuator=pf),

        # Allow di una rete
        # oc2.Command(oc2.Actions.allow, oc2.IPv4Net('130.0.16.0/20'), arg, actuator=pf),

        # Deny di un IP
        # oc2.Command(oc2.Actions.deny, oc2.IPv4Net('130.0.0.1'), arg, actuator=pf),

        # Update di file di regole
        # oc2.Command(oc2.Actions.update,
        #            oc2.File({'path':'http://192.168.197.128:8080','name':'iptables-rules.v4'}),
        #            arg, actuator=pf)
    ]

    # Esegui i comandi
    for i, cmd in enumerate(commands):
        logger.info(f"Sending command {i + 1}: {cmd}")
        try:
            resp = p.sendcmd(cmd)
            logger.info(f"Got response {i + 1}: {resp}")
        except Exception as e:
            logger.error(f"Error sending command {i + 1}: {e}")


#auto_authenticate=False
def main_manual_auth():
    """Esempio con autenticazione manuale"""
    logger.info("Creating Producer with manual OAuth2 authentication")

    oauth2_config = {
        'client_id': '4AdyEBAK7vJtsHxB2y84qzmF',
        'client_secret': 'LJPW4rDrlt7CTXCqQ21KwpYzHtXd1ylR2VtWOJAq6O2dLOBP',
        'authorize_url': 'http://127.0.0.1:8080/oauth/authorize',
        'token_url': 'http://127.0.0.1:8080/oauth/token',
        'redirect_uri': 'http://127.0.0.1:8000/callback',
        'ua_url': 'http://127.0.0.1:7000/auth',
        'callback_port': 8000
    }

    # Crea Producer senza auto-autenticazione usando il wrapper
    p = OAuth2ProducerWrapper(
        "producer.example.net",
        JSONEncoder(),
        HTTPTransfer("172.17.0.11", 8080),
        oauth2_config=oauth2_config,
        auto_authenticate=False  # Non autentica automaticamente
    )

    # Autentica manualmente quando necessario
    logger.info("Fare login tramite UA per continuare...")
    try:
        p.authenticate()
        logger.info("Autenticazione completata")

        # Procedi con i comandi...
        pf = slpf.Specifiers({'hostname': 'firewall', 'named_group': 'firewalls', 'asset_id': 'iptables'})
        arg = slpf.Args({'response_requested': oc2.ResponseType.complete})
        cmd = oc2.Command(oc2.Actions.query, oc2.Features([oc2.Feature.versions]), arg, actuator=pf)

        resp = p.sendcmd(cmd)  # Il wrapper gestisce automaticamente l'auth
        logger.info("Got response: %s", resp)

    except Exception as e:
        logger.error(f"Errore durante l'autenticazione: {e}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == "oauth2":
            main_with_oauth2()
        elif mode == "manual":
            main_manual_auth()
        else:
            print("Uso: python controller-iptables.py [oauth2|manual|no-auth]")
    else:
        # Default: usa OAuth2 automatico
        main_with_oauth2()
