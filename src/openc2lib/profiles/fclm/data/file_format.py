from openc2lib.types.base import Enumerated

class FileFormat(Enumerated):
    """File Format

    format of the file
    """

    text = 1
    json = 2
    yaml = 3
    csv = 4
    xml = 5