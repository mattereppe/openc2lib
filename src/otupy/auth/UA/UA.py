from flask import Flask, request, jsonify
import requests
import sys
import threading
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('UA')

app = Flask(__name__)

# Authorization Server login endpoint URL
as_authorize_url = 'http://127.0.0.1:9000/'

# Credentials from environment variables
CONFIG_USERNAME = os.getenv("USERNAME")
CONFIG_PASSWORD = os.getenv("PASSWORD")

if not CONFIG_USERNAME or not CONFIG_PASSWORD:
    logger.error("USERNAME or PASSWORD not defined in .env file")
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
                            logger.error("Error: 'Location' not found in response")
                    except Exception as e:
                        logger.exception(f"Error parsing JSON: {str(e)}")
                    return
                elif response.status_code == 401:
                    continue
                else:
                    logger.error(f"Resource access error: {response.status_code}")
                    return
            else:
                logger.warning(f'Login failed with status code: {login_response.status_code}')
        logger.error('Invalid credentials after 3 attempts')
        return

    try:
        logger.debug(response.json())
    except Exception as e:
        logger.exception(f"Error parsing JSON: {str(e)}")


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
