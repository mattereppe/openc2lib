import openc2
import sys
import uuid

sys.path.insert(0, "profiles/")

import mycompany_capX

id=mycompany_capX.UuidProperty().clean(uuid.uuid4())
argp=mycompany_capX.DebugArgsProperty(debug_logging=True)
act=mycompany_capX.MyCompanyActuator(asset_id=id)
t=openc2.v10.Features(features=["versions", "rate_limit", "profiles", "pairs"])

arg = mycompany_capX.MyCompanyArgs(**{"x-mycompany":argp})

#print(id)
#print(act)
#print(arg)

cmd = openc2.v10.Command(action="query", target=t, args=arg, actuator=act)
print(cmd)
