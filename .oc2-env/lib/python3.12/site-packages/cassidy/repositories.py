import dataclasses
import functools
import typing

from . import models
from . import utils

@dataclasses.dataclass
class Repository:
    store: set = dataclasses.field(default_factory = set)

    def __iter__(self) -> typing.Iterable:
        return iter(self.store)

    def __repr__(self) -> str:
        return '{class_name}[{cases}]'.format \
        (
            class_name = type(self).__name__,
            cases      = ', '.join(map(repr, self))
        )

    def add(self, item: typing.Any) -> None:
        return self.store.add(item)

    def clear(self) -> None:
        return self.store.clear()

    def copy(self):
        clone = self.__class__()

        clone.update(self.store)

        return clone

    def pop(self) -> typing.Any:
        return self.store.pop()

    def remove(self, item: typing.Any) -> None:
        return self.store.remove(item)

    def update(self, *iterables: typing.Iterable) -> None:
        return self.store.update(*iterables)

class Cases(Repository):
    def __call__ \
            (
                self,
                cls_or_fn: typing.Optional[typing.Union[typing.Type, typing.Callable]] = None,
                /,
                *,
                name: typing.Optional[str] = None,
            ):
        def wrap(cls_or_fn: typing.Union[typing.Type[models.Case], typing.Callable]):
            case_style: typing.Optional[str] = \
            (
                cls_or_fn.__name__.lower()
                if name is None and utils.named(cls_or_fn)
                else name
            )

            case: models.Case

            if isinstance(cls_or_fn, type):
                @functools.wraps(cls_or_fn, updated = ())
                @models.model
                class Wrapper(models.model(cls_or_fn)):
                    style: typing.Optional[str] = case_style

                case = Wrapper()

                cls_or_fn = Wrapper
            elif callable(cls_or_fn):
                case = models.Case \
                (
                    render = cls_or_fn,
                    style  = case_style,
                )

            self.add(case)

            return cls_or_fn

        return \
        (
            wrap
            if cls_or_fn is None
            else wrap(cls_or_fn)
        )

    def get(self, style: str, default: typing.Any = None) -> typing.Any:
        items: typing.List[models.Case] = \
        [
            case
            for case in self
            if case.style == style
        ]

        return \
        (
            items[0]
            if items
            else default
        )

    def identify(self, string: str) -> typing.List[models.Case]:
        return \
        [
            case
            for case in self
            if case.match(string)
        ]
