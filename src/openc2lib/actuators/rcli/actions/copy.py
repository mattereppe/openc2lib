import os
import logging
import openc2lib.profiles.rcli as rcli
from openc2lib import  ResponseType, Artifact
from openc2lib.types.targets.file import File
from openc2lib.types.base.array_of import ArrayOf
from openc2lib.types.data import Hashes
from openc2lib.types.base import Binaryx
from openc2lib.profiles.rcli.targets import Files
from openc2lib.actuators.rcli.database.SQLDB import db
from openc2lib.actuators.rcli.user.config import PRODUCER_ID
from openc2lib.actuators.rcli.utils.files_utils import get_file_path, get_payload, download_or_save_file,compare_hashes
from openc2lib.actuators.rcli.handlers.response_handler import servererror, badrequest, notimplemented, ok

logger = logging.getLogger(__name__)

def copy(cmd):
    """
    Handles the `copy` action by validating the command arguments and calling the appropriate method to copy an artifact.

    This method implements the OpenC2 `copy` action. It checks if the `response_requested` argument is valid, 
    ensures the `storage` argument is of type `Storage`, and verifies that the target is an `Artifact`. If the 
    target is not an `Artifact`, a `badrequest` response is returned. If the target is valid, the `copy_artifact` 
    method is called to perform the copy operation.

    Args:
        cmd (Command): The `Command` object containing:
            - `target`: The target of the copy action, which should be of type `Artifact`.
            - `args`: A dictionary of optional arguments, including:
                - `response_requested`: A flag indicating whether a response is requested.
                - `storage`: A `Storage` object specifying where to store the copied file.

    Returns:
        Response: A response indicating the result of the copy action:
            - `badrequest`: If the arguments are invalid or the target type is unsupported.
            - `notimplemented`: If the MIME type is unsupported.
            - `ok`: If the copy action was successful and the artifact was stored.
            - `servererror`: If there is an internal error during the copy operation.

    Example:
        cmd = Command(target=Artifact(mime_type='text/plain', payload='file_payload'), args={'response_requested': ResponseType.complete})
        copy(cmd)
    """
    logger.info(f"Copying action with command: {cmd}")
    if cmd.args is not None:
        try:
            if cmd.args.get('response_requested') is not None:
                if not (cmd.args['response_requested'] == ResponseType.complete):
                    raise KeyError
            elif cmd.args.get('storage') is not None:
                if not isinstance(cmd.args['storage'], File):
                    raise KeyError
        except KeyError:
            return badrequest("Invalid copy argument")
    if cmd.target.getObj().__class__ == Artifact:
        r = copy_artifact(cmd)
    else:
        return badrequest("Unsupported Target Type.")
    return r

def copy_artifact(cmd):
    """
    Copies a file from the target artifact and stores it in the specified directory.

    This method checks the MIME type of the target artifact, verifies file integrity using a hash check, 
    and saves the file to the specified location. If the MIME type is unsupported, a `notimplemented` response is 
    returned. If the file already exists at the target location, a `badrequest` response is returned. In case of 
    errors during the file copy process, a `servererror` response is returned.

    Args:
        cmd (Command): The `Command` object containing:
            - `target`: The `Artifact` containing the file to be copied.
            - `args`: A dictionary of optional arguments, including:
                - `storage`: A `Storage` object specifying the directory to store the copied file.

    Returns:
        Response: A response indicating the result of the copy action:
            - `badrequest`: If the file already exists or the payload is empty.
            - `notimplemented`: If the MIME type is unsupported.
            - `ok`: If the artifact was successfully copied and stored.
            - `servererror`: If an error occurred during the file copy process.

    Example:
        cmd = Command(target=Artifact(mime_type='application/json', payload='json_payload'), args={'storage': Storage(path='/target/directory')})
        copy_artifact(cmd)
    """
    target = cmd.target.getObj()
    arguments = cmd.args    
    mime_type = target.mime_type
    if mime_type not in ['text/plain', 'application/json', 'application/x-executable', 'application/x-sh']:
        return notimplemented('Unsupported MIME type',)

    payload, is_uri = get_payload(target)
    if not payload:
        return badrequest('Payload cannot be empty',)
        
    full_path, file_path, file_name = get_file_path(arguments)

    if os.path.exists(full_path):
        return badrequest('File already exists')
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path, exist_ok=True)
        calculated_hash = download_or_save_file(is_uri, payload, full_path)
        if not is_uri and not compare_hashes(target,calculated_hash):
            return servererror(text ='Hash mismatch, file integrity check failed')
        try: 
            db.add_file(PRODUCER_ID, file_path,file_name,str(calculated_hash))
        except Exception as e:
            servererror("File couldn't be saved to database")
        res =rcli.Results(file_status = Files([File(name=file_name, path=file_path, hashes=Hashes({'md5': Binaryx(calculated_hash)}))]))
        return ok('Ok', res= res)
    except Exception as e:
        return servererror('Error copying artifact')
