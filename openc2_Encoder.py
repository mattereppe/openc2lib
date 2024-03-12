import json
from datetime import datetime


class Encoding:
    def encode(self, message):
        pass


class JSONEncoding(Encoding):
    @staticmethod
    def encode(message):
		 message.to_json()

# the following moved to Message
        timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        command = {
# message            "headers": {
# message                "request_id": message.request_id,
# message                "created": timestamp,
# message                "Date": timestamp,
# message                "to": message.to,
# message                "from": message.from_
# message            },
# message            "body": {
# message                "openc2": {
#command                    "request": {
#command                        "action": message.action,
#command                        "target": message.target,
#command                        "args": message.args
#command                    }
# message                }
# message            }
# message        }
        if message.actuator:
            command["body"]["openc2"]["request"]["actuator"] = message.actuator
        return json.dumps(command, indent=2)

class XMLEncoding(Encoding):
	@staticmethod
	 def encode(message):
		 message.to_xml()
