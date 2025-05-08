import random
import typing
import itertools

from . import utils
from . import renderers

def lower(words: typing.List[str]) -> typing.List[str]:
    return [word.lower() for word in words]

def upper(words: typing.List[str]) -> typing.List[str]:
    return [word.upper() for word in words]

def title(words: typing.List[str]) -> typing.List[str]:
    return [word.title() for word in words]

def swapcase(words: typing.List[str]) -> typing.List[str]:
    return [word.swapcase() for word in words]

def capitalize(words: typing.List[str]) -> typing.List[str]:
    return \
    [
        (
            word.title()
            if index == 0
            else word.lower()
        )
        for index, word in enumerate(words)
    ]

def dromedary(words: typing.List[str]) -> typing.List[str]:
    return \
    [
        (
            word.lower()
            if index == 0
            else word.title()
        )
        for index, word in enumerate(words)
    ]

def alternating(words: typing.List[str]) -> typing.List[str]:
    return utils.chunk \
    (
        string = ''.join \
        (
            (str.lower, str.upper)[index % 2](character)
            for index, character in enumerate(itertools.chain(*words))
        ),
        sizes  = [len(word) for word in words],
    )

def sponge(words: typing.List[str]) -> typing.List[str]:
    return utils.chunk \
    (
        string = renderers.concatenate \
        (
            random.choice((str.lower, str.upper))(character)
            for word      in words
            for character in word
        ),
        sizes  = [len(word) for word in words],
    )
