import abc
import dataclasses
import re
import string
import typing

class AbstractParser(abc.ABC):
    @abc.abstractmethod
    def parse(self, string: str) -> typing.List[str]:
        raise NotImplementedError

@dataclasses.dataclass(frozen = True)
class Parser(AbstractParser):
    tall:  str = string.ascii_uppercase
    small: str = string.ascii_lowercase + string.digits

    def __call__(self, string: str) -> typing.List[str]:
        return self.parse(string)

    def _split_sentence(self, sentence: str) -> typing.List[str]:
        return re.findall \
        (
            pattern = f'[{self.tall}{self.small}]+',
            string  = sentence,
        )

    def _split_word(self, word: str) -> typing.List[str]:
        words: typing.List[str] = []

        current: str
        for current in re.split(f'([{self.tall}][{self.small}]*)', word):
            if not current: continue

            if not words or not all(item[-1].isupper() for item in (current, words[-1]) if item):
                words.append(str())

            words[-1] += current

        return words

    def parse(self, string: str, case_sensitive: bool = False) -> typing.List[str]:
        return \
        [
            (
                word
                if case_sensitive
                else word.lower()
            )
            for segment in self._split_sentence(string)
            for word in self._split_word(segment)
        ]
