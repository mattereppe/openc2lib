import requests
from openc2_Response import OpenC2Response


class Transfer:
    def send_openc2_command(self, command):
        pass


class OpenC2_HTTP(Transfer):
    def __init__(self, host, endpoint="/.well-known/openc2"):
        self.base_url = f"http://{host}{endpoint}"

    def send_openc2_command(self, command, encoder):
        """
        Send an OpenC2 command over HTTP.
        """

        headers = {
            "Content-Type": "application/openc2+json;version=1.0",
            "Accept": "application/openc2+json;version=1.0",
        }

        serialized_command = encoder.encode(command)

        try:
            response = requests.post(self.base_url, data=serialized_command, headers=headers)
            return OpenC2Response(response.status_code, response.json()).response_to_json()
        except Exception as e:
            return OpenC2Response(503, str(e)).response_to_json()



class OpenC2_MQTT(Transfer):
    pass


class OpenC2_HTTPS(OpenC2_HTTP):
    pass


class OpenC2_CoAP(Transfer):
    pass


class OpenC2_OpenDXL(Transfer):
    pass
    
