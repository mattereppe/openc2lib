import typing

Parser     = typing.Callable[[str], typing.Iterable[str]]
Renderer   = typing.Callable[[typing.Iterable[str]], str]
Translator = typing.Callable[[typing.Iterable[str]], typing.Iterable[str]]
