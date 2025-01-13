import openc2
import sys
import uuid

sys.path.insert(0, "profiles/")

import mycompany_capX

id=mycompany_capX.UuidProperty().clean(uuid.uuid4())
a=mycompany_capX.MyCompanyActuator(asset_id=id)

arg = mycompany_capX.MyCompanyArgs(debug_logging=True)

print(id)
print(a)
print(arg)
