import cassidy
import expo

from . import bases
from . import generators
from . import utils

@expo
class Name(bases.StrEnum): pass

@expo
class Index(bases.IntEnum): pass

@expo
class Integer(bases.IntEnum):
    _generate_next_value_ = utils.compose(generators.count, lambda count: count + 1)

@expo
class NoValue(bases.Enum):
    def __repr__(self) -> str:
        return f'<{type(self).__name__}.{self.name}>'

    @property
    def value(self) -> None:
        raise AttributeError(f'{type(self).__name__!r} object has no attribute \'value\'')

@expo
class Lower(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.lower)

@expo
class Upper(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.upper)

@expo
class Title(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.title)

@expo
class Sentence(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.sentence)

@expo
class Snake(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.snake)

@expo
class Helter(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.helter)

@expo
class Macro(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.macro)

@expo
class Flat(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.flat)

@expo
class Flush(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.flush)

@expo
class Camel(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.camel)

@expo
class Pascal(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.pascal)

@expo
class Kebab(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.kebab)

@expo
class Train(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.train)

@expo
class Cobol(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.cobol)

@expo
class Dot(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.dot)

@expo
class Path(bases.StrEnum):
    _generate_next_value_ = utils.compose(generators.name, cassidy.path)
