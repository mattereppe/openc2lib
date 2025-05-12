from openc2lib.types.base import Map
from openc2lib.types.data.duration import Duration

class ImportOptions(Map):
    """
    ImportOptions Class (File Monitoring Profile)

    Represents Input configuration settings for file monitoring tools (e.g., Filebeat).

    Fields:
    - `scan_frequency`: How often to check for new or updated files.
    - `clean_inactive`: Clean up registry entry if file is inactive this long.
    - `max_backoff`: Max delay between retries when no data is available.
    - `close_inactive`: Time to close a file with no new log lines.
    - `ignore_older`: Skip files older than this duration (not harvested).
    """

    fieldtypes = {
        'scan_frequency': Duration,
        'clean_inactive': Duration,
        'max_backoff': Duration,
        'close_inactive': Duration,
        'ignore_older': Duration
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validate_fields()

    def validate_fields(self):
        for key, value in self.items():
            expected_type = self.fieldtypes.get(key)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(f"Expected '{key}' to be {expected_type.__name__}, got {type(value).__name__}")

    def __repr__(self):
        return f"ImportOptions({super().__repr__()})"
    
