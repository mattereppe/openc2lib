import openc2
import sys
import uuid

sys.path.insert(0, "profiles/")

import mycompany_dots

id=mycompany_dots.UuidProperty().clean(uuid.uuid4())
argp=mycompany_dots.DebugArgsProperty(debug_logging=True)
act=mycompany_dots.MyCompanyActuator(asset_id=id)
t=openc2.v10.Features(features=["versions", "rate_limit", "profiles", "pairs"])

arg = mycompany_dots.MyCompanyArgs(**{"x-mycompany.example.com":argp})

cmd = openc2.v10.Command(action="query", target=t, args=arg, actuator=act)
print(cmd)
