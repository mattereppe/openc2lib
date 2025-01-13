import openc2
import sys
import uuid

sys.path.insert(0, "profiles/")

import mycompany_nox

id=mycompany_nox.UuidProperty().clean(uuid.uuid4())
argp=mycompany_nox.DebugArgsProperty(debug_logging=True)
act=mycompany_nox.MyCompanyActuator(asset_id=id)
t=openc2.v10.Features(features=["versions", "rate_limit", "profiles", "pairs"])

arg = mycompany_nox.MyCompanyArgs(**{"mycompany":argp})

cmd = openc2.v10.Command(action="query", target=t, args=arg, actuator=act)
print(cmd)
