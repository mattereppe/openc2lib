import typing

EnumValueGenerator = typing.Callable \
[
    [
        str,                    # name
        int,                    # start
        int,                    # count
        typing.List[typing.Any] # last_values
    ],
    typing.Any,
]
