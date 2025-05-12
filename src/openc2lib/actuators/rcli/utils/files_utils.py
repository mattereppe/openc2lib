import os
import uuid
import hashlib
import requests
import openc2lib as oc2
from pathlib import Path
from openc2lib.types.data.uri import URI
from openc2lib.types.targets.file import File

from openc2lib import Payload, Binary
from openc2lib.actuators.rcli.database.SQLDB import db
from openc2lib.actuators.rcli.user.config import PRODUCER_ID

def get_payload(target):
    """
    Extracts payload data from the target.

    Args:
        target (object): The target object that may contain a payload.

    Returns:
        tuple: (payload data (bytes or str), is_uri (bool))
            - If the payload is a binary file, returns the binary content.
            - If the payload is a URI, returns the URI as a string.
            - If no payload is found, returns (None, False).
    """
    if isinstance(target.payload, Payload):
        file = target.payload.getObj()
        if isinstance(file, Binary):
            return file.get(), False
        elif isinstance(file, URI):
            return file.get(), True
    return None, False

def get_file_path(arguments):
    """
    Determines the file path where an artifact should be saved.

    Args:
        arguments (dict): The command arguments containing storage details.

    Returns:
        tuple: (full_file_path (str), directory_path (str), file_name (str))
            - full_file_path: The full path where the file will be saved.
            - directory_path: The directory where the file is located.
            - file_name: The name of the file.
    """
    storage = arguments.get('storage')
    file_name = str(uuid.uuid4())  # Generate a unique filename if not provided

    if storage and isinstance(storage, File):
        path_value = storage.get("path", None)
        file_name = storage.get("name") or file_name
        file_path = os.path.join("/opt", str(PRODUCER_ID), path_value)
        return os.path.join(file_path, file_name), file_path, file_name

    file_path = os.path.join("/opt", str(PRODUCER_ID))
    return os.path.join(file_path, file_name), file_path, file_name

def download_or_save_file(is_uri, payload, file_path):
    """
    Downloads a file from a URL or saves binary data to a file, and returns the MD5 hash of the file.

    Args:
        is_uri (bool): Indicates whether the payload is a URI.
        payload (bytes or str): The file content or the URI.
        file_path (str): The path where the file should be saved.

    Raises:
        requests.exceptions.RequestException: If the file download fails.
        IOError: If the file cannot be written.
    """
    if is_uri:  # If the payload is a URI, download the file
        response = requests.get(payload)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        file_content = response.content
    else:  # If the payload is binary data, save it
        Path(file_path).write_text(payload.decode())
        file_content = payload
    # Calculate MD5 hash of the file content
    file_hash = hashlib.md5(file_content).digest()
    
    # Return the hash wrapped in an oc2.Binaryx object
    return oc2.Binaryx(file_hash)


def is_file_authorized(file_path, file_name):
    """
    Checks if a file is authorized for deletion.

    Args:
        file_path (str): The full path of the file.
        file_name (str): The name of the file.

    Returns:
        bool: True if the file is authorized, False otherwise.
    """
    user_files = db.get_files(PRODUCER_ID)
    
    # Check if the (file_path, file_name) pair exists in the database
    for stored_file_path, stored_file_name, _ in user_files:
        if stored_file_path == file_path and stored_file_name == file_name:
            return True
    
    return False


def compare_hashes(target, calculated_hash):
    """
    Compares the hash of a given payload with the expected hash.

    Args:
        target (object): The target object containing expected hash values.
        payload (bytes): The binary content of the file.

    Returns:
        bool: True if the computed hash matches the target's hash, False otherwise.
    """
    received_hash = target.hashes.get("md5")
    return str(calculated_hash) == str(received_hash)
