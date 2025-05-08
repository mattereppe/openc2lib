import typing

from . import enums, models


class Parser:
    @staticmethod
    def _parse_parameter(parameter: str) -> typing.Dict[str, str]:
        parameters: typing.Dict[str, str] = {}
        attribute: str
        value: str

        while parameter:
            attribute, parameter = map(str.strip, parameter.split("=", 1))

            if parameter.startswith('"'):
                value, parameter = map(str.strip, parameter[1:].split('"', 1))
            else:
                value = parameter[
                    : index if (index := parameter.find(";")) >= 0 else len(parameter)
                ]

            parameters[attribute] = value

            parameter = parameter[
                index + 1 if (index := parameter.find(";")) >= 0 else len(parameter) :
            ]

        return parameters

    @classmethod
    def parse(cls, mime_type: str) -> models.MediaType:
        type: str
        subtype: str
        suffix: typing.Optional[str] = None
        parameter: typing.Optional[str] = None

        mime_type = mime_type.strip().lower()

        if ";" in mime_type:
            mime_type, parameter = map(str.strip, mime_type.split(";", 1))

        type, subtype = map(str.strip, mime_type.split("/", 1))

        if "+" in subtype:
            subtype, suffix = map(str.strip, subtype.split("+"))

        type = (
            enums.MediaTypeType(type)
            if type in enums.MediaTypeType.__members__.values()
            else type
        )
        subtype = (
            enums.MediaTypeSubtype(subtype)
            if subtype in enums.MediaTypeSubtype.__members__.values()
            else subtype
        )
        suffix = (
            enums.MediaTypeSuffix(suffix)
            if suffix in enums.MediaTypeSuffix.__members__.values()
            else suffix
        )

        return models.MediaType(
            type=type,
            subtype=subtype,
            suffix=suffix,
            parameters=parameter and cls._parse_parameter(parameter),
        )
