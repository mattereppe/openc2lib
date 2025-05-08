import dataclasses
import typing

import expo

@expo
@dataclasses.dataclass(frozen = True)
class Arguments:
    name:        str
    start:       int
    count:       int
    last_values: typing.List[str]
