import io
import typing
import types

def compose(*functions: typing.Callable) -> typing.Callable:
    def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        response: typing.Any = None

        index: int
        function: typing.Callable
        for index, function in enumerate(functions):
            response = \
            (
                function(*args, **kwargs)
                if not index
                else function(response)
            )

        return response

    return wrapper

def identity(x: typing.Any) -> typing.Any:
    return x

def is_lambda(obj: typing.Any) -> bool:
    return isinstance(obj, types.LambdaType) and obj.__name__ == '<lambda>'

def chunk(string: str, sizes: typing.List[int]) -> typing.List[str]:
    buffer: io.StringIO = io.StringIO(string)

    return \
    [
        buffer.read(size)
        for size in sizes
    ]

def named(obj: typing.Any) -> bool:
    return hasattr(obj, '__name__')
