import enum
import typing

import expo

@expo
class EnumMeta(enum.EnumMeta):
    def __new__ \
            (
                metacls:   type,
                cls:       str,
                bases:     typing.Tuple[type],
                classdict: typing.Dict[str, typing.Any],
            ) -> object:
        annotations: dict = classdict.get('__annotations__', {})

        member: str
        for member in annotations:
            if member not in classdict:
                classdict[member]: enum.auto = enum.auto()

        return super().__new__(metacls, cls, bases, classdict)
