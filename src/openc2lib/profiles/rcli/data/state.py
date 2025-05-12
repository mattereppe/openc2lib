import psutil
from openc2lib.types.base import Enumerated

class State(Enumerated):
    running = 1
    sleeping = 2
    disk_sleep = 3
    stopped = 4
    tracing_stop = 5
    zombie = 6
    dead = 7
    wake_kill = 8
    waking = 9
    parked = 10
    idle = 11
    locked = 12
    waiting = 13
    suspended = 14
    not_found = 15

    @classmethod
    def from_status(cls, value: str) -> "State":
        """Create a State from psutil-like state strings (e.g. 'disk-sleep')."""
        key = value.replace("-", "_")
        if key in cls.__members__:
            return cls[key]
        raise ValueError(f"Unrecognized state: {value!r}")

