import os
import getpass

def get_username():
    """Returns the current logged-in username."""
    try:
        return os.getlogin()  # Works on most systems
    except OSError:
        return getpass.getuser()  # Fallback method

PRODUCER_ID: str = get_username()
