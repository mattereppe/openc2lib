import enum

import expo

from . import generators
from . import meta

@expo
class Enum(enum.Enum, metaclass = meta.EnumMeta): pass

class BaseTypeEnum(Enum):
    def __str__(self) -> str:
        return str(self.value)

@expo
class IntEnum(int, BaseTypeEnum):
    _generate_next_value_ = generators.count

@expo
class StrEnum(str, BaseTypeEnum):
    _generate_next_value_ = generators.name
