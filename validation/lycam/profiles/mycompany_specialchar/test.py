import openc2
import sys
import uuid

sys.path.insert(0, "profiles/")

import mycompany_specialchar

id=mycompany_specialchar.UuidProperty().clean(uuid.uuid4())
argp=mycompany_specialchar.DebugArgsProperty(debug_logging=True)
act=mycompany_specialchar.MyCompanyActuator(asset_id=id)
t=openc2.v10.Features(features=["versions", "rate_limit", "profiles", "pairs"])

arg = mycompany_specialchar.MyCompanyArgs(**{"x-mycompany/foo;bar":argp})

cmd = openc2.v10.Command(action="query", target=t, args=arg, actuator=act)
print(cmd)
