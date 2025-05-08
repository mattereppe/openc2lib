import typing

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
