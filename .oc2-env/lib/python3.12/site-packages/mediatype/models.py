import dataclasses
import typing


@dataclasses.dataclass
class MediaType:
    type: str
    subtype: str
    suffix: typing.Optional[str]
    parameters: typing.Optional[typing.Dict[str, str]]

    def __str__(self) -> str:
        return self.string()

    def string(self, suffix: bool = True, parameters: bool = True) -> str:
        return "".join(
            (
                f"{self.type}/",
                f"{self.subtype}",
                f"+{self.suffix}" if suffix and self.suffix else "",
                "; " if parameters and self.parameters else "",
                "; ".join(f'{key}="{value}"' for key, value in self.parameters.items())
                if parameters and self.parameters
                else "",
            ),
        )
