from openc2lib.types.base import Enumerated

class FlowFormat(Enumerated):
    """Flow Format

    format of the flow
    """

    netflow5 = 1
    netflow9 = 2
    ipfix = 3
    json = 4
    csv = 5