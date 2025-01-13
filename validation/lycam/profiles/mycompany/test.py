import openc2
import sys
import uuid

sys.path.insert(0, "profiles/")

import mycompany

id=mycompany.UuidProperty().clean(uuid.uuid4())
argp=mycompany.DebugArgsProperty(debug_logging=True)
act=mycompany.MyCompanyActuator(asset_id=id)
t=openc2.v10.Features(features=["versions", "rate_limit", "profiles", "pairs"])

arg = mycompany.MyCompanyArgs(**{"x-mycompany":argp})


cmd = openc2.v10.Command(action="query", target=t, args=arg, actuator=act)
print(cmd)
