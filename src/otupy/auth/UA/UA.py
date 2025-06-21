from flask import Flask, request, jsonify
import requests
import sys
import threading
import logging
import os
from dotenv import load_dotenv

# Carica le variabili d'ambiente da .env
load_dotenv()

# Configurazione del logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('UA')

# Flask app
app = Flask(__name__)

# URL dell'endpoint di login dell'Authorization Server
as_authorize_url = 'http://127.0.0.1:9000/'

# Credenziali da variabili ambiente
CONFIG_USERNAME = os.getenv("USERNAME")
CONFIG_PASSWORD = os.getenv("PASSWORD")

if not CONFIG_USERNAME or not CONFIG_PASSWORD:
    logger.error("USERNAME o PASSWORD non definite nel file .env")
    sys.exit(1)


def auth_flow(url):
    session = requests.Session()
    response = session.get(url)
    logger.debug(f'Response content: {response.content}\n')

    if response.status_code == 401:
        logger.info('Login required...')

        for attempt in range(3):
            login_payload = {
                'username': CONFIG_USERNAME,
                'password': CONFIG_PASSWORD
            }

            login_response = session.post(as_authorize_url, json=login_payload)

            if login_response.status_code == 200:
                response = session.get(url)
                if response.status_code == 200:
                    try:
                        data = response.json()
                        location = data.get('Location')
                        if location:
                            logger.info(f"Redirecting to location: {location}")
                            resp = requests.get(location)
                        else:
                            logger.error("Errore: Location non trovata nella risposta")
                    except Exception as e:
                        logger.exception(f"Errore parsing JSON: {str(e)}")
                    return
                elif response.status_code == 401:
                    continue
                else:
                    logger.error(f"Errore accesso risorsa: {response.status_code}")
                    return
            else:
                logger.warning(f'Login fallito con status code: {login_response.status_code}')
        logger.error('Credenziali errate dopo 3 tentativi')
        return

    try:
        logger.debug(response.json())
    except Exception as e:
        logger.exception(f"Errore parsing JSON: {str(e)}")


@app.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()

    if not data or 'url' not in data:
        return jsonify({'error': 'Missing URL'}), 400

    url = data['url']
    threading.Thread(target=auth_flow, args=(url,)).start()
    return jsonify({'status': 'OK'}), 200


@app.route('/as_url', methods=['GET'])
def get_as_url():
    return jsonify({'as_url': as_authorize_url})


if __name__ == '__main__':
    app.run(debug=True, port=7000)
