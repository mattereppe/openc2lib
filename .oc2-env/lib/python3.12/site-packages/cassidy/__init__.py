from .models       import Case
from .parsers      import Parser
from .repositories import Cases
from .styles       import *

parser: Parser = Parser()

parse = parser.parse

identify = cases.identify
case     = cases.__call__

locals().update \
(
    {
        case.style: case
        for case in cases
    }
)
