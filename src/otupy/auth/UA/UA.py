from flask import Flask, request, jsonify
import requests
import sys
import threading
import logging
import os
from dotenv import load_dotenv
from otupy.auth.UA.casbin.AuthAgent import AuthorizationAgent, AuthorizationError
from urllib.parse import urlparse


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
MODEL_PATH="./casbin/model.conf"
POLICY_PATH="./casbin/policy.csv"


if not CONFIG_USERNAME or not CONFIG_PASSWORD:
    logger.error("USERNAME or PASSWORD not defined in .env file")
    sys.exit(1)


# Initialize Casbin Authorization Agent
try:
    auth_agent = AuthorizationAgent(model_path=MODEL_PATH, policy_path=POLICY_PATH)
except AuthorizationError as e:
    logger.error(f"Failed to initialize AuthorizationAgent: {e}")
    sys.exit(1)

from urllib.parse import urlparse
import requests
import logging

logger = logging.getLogger(__name__)

def auth_flow(url, command):
    session = requests.Session()
    try:
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
                    # Authorization check
                    is_allowed = True

                    for target in command.get('target', []):
                        try:
                            result = auth_agent.is_authorized(
                                user=CONFIG_USERNAME,
                                action=command['action'],
                                target=target,
                                actuator=command['actuator']
                            )
                            logger.info(
                                f"[AUTH CHECK] user={CONFIG_USERNAME}, action={command['action']}, "
                                f"target={target}, actuator={command['actuator']} => {'✅ ALLOWED' if result else '❌ DENIED'}"
                            )
                            if not result:
                                is_allowed = False
                        except AuthorizationError as e:
                            logger.error(f"[AUTH ERROR] Failed to check auth for target={target}: {e}")
                            is_allowed = False

                    if is_allowed:
                        logger.info(f"User {CONFIG_USERNAME} is authorized.")
                    else:
                        logger.warning(f"User {CONFIG_USERNAME} is NOT authorized.")

                    # Retry the original request
                    response = session.get(url)

                    if response.status_code == 200:
                        try:
                            data = response.json()
                            location = data.get('Location')

                            if not is_allowed and location:
                                try:
                                    parsed = urlparse(location)
                                    scheme = parsed.scheme
                                    host = parsed.hostname
                                    port = parsed.port

                                    error_url = f"{scheme}://{host}:{port}/error"
                                    logger.warning(f"User not authorized. Redirecting to: {error_url}")
                                    rsp = requests.get(error_url)
                                    return

                                except Exception as e:
                                    logger.exception(f"Error constructing error URL from location '{location}': {str(e)}")

                            if location:
                                logger.info(f"Redirecting to location: {location}")
                                try:
                                    resp = requests.get(location)
                                    logger.debug(f"Redirect response: {resp.status_code}")
                                except Exception as e:
                                    logger.exception(f"Error during redirection to location: {str(e)}")
                            else:
                                logger.error("Error: 'Location' not found in response")

                        except Exception as e:
                            logger.exception(f"Error parsing JSON from successful response: {str(e)}")
                        return

                    elif response.status_code == 401:
                        logger.warning("Still unauthorized after login, retrying...")
                        continue
                    else:
                        logger.error(f"Resource access error after login: {response.status_code}")
                        return
                else:
                    logger.warning(f'Login failed with status code: {login_response.status_code}')

            logger.error('Invalid credentials after 3 attempts')
            return

        else:
            # Initial request already succeeded
            try:
                logger.debug(response.json())
            except Exception as e:
                logger.exception(f"Error parsing JSON from initial response: {str(e)}")

    except Exception as e:
        logger.exception(f"Unexpected error in auth_flow: {e}")


@app.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()

    if not data or 'url' not in data:
        return jsonify({'error': 'Missing URL'}), 400

    url = data['url']
    command=data['command']
    print(command)
    threading.Thread(target=auth_flow, args=(url,command,)).start()
    return jsonify({'status': 'OK'}), 200


@app.route('/as_url', methods=['GET'])
def get_as_url():
    return jsonify({'as_url': as_authorize_url})


if __name__ == '__main__':
    app.run(debug=True, port=7000)
