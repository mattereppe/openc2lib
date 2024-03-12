from uuid import uuid4
from openc2_Encoder import JSONEncoding

class MessageType(Enum):
	request: 1
	response: 2

class Command(Message):
	messagetype = None
    def __init__(self, action,
                 target,
                 args=None,
                 actuator=None,
                 to=None,
                 from_=None,
                 request_id=None,
                 slpf_rule_number=None):

        self.action = action
        self.target = target
        self.args = args
        self.actuator = actuator
        self.to = to
        self.from_ = from_
        self.request_id = request_id or str(uuid4())
# Why>????
        if slpf_rule_number:
            self.target['slpf:rule_number'] = slpf_rule_number

    def to_json(self):
# Take the json enconding from openc2_jsonencoding
		 "action" : self.action.to_json()

class Message:
#include headers

class Response(Message):
		
