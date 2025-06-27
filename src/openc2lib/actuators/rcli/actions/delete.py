import os
import logging
from openc2lib import  ResponseType
from openc2lib.types.targets.file import File
import openc2lib.profiles.rcli as rcli
from openc2lib.actuators.rcli.database.SQLDB import db
from openc2lib.actuators.rcli.user.config import PRODUCER_ID
from openc2lib.actuators.rcli.utils.files_utils import is_file_authorized
from openc2lib.actuators.rcli.handlers.response_handler import servererror, badrequest, notimplemented, notfound, unauthorized, ok
from openc2lib.profiles.rcli.targets.files import Files

logger = logging.getLogger(__name__)

def delete(cmd):
    """ Delete action

        This method implements the `delete` action.
        :param cmd: The `Command` including `Target` and optional `Args`.
        :return: A `Response` including the result of the query and appropriate status code and messages.
    """
    logger.info(f"Deleting action with command: {cmd}")
    if cmd.args is not None:
        try:
            if cmd.args.get('response_requested') is not None:
                if not (cmd.args['response_requested']==ResponseType.complete):
                    raise KeyError
        except KeyError:
            return badrequest("Invalid start argument")
    if cmd.target.getObj().__class__ == Files:
        r = delete_file(cmd)
    else:
        return notimplemented("Unsupported Target Type.")
    return r

def delete_file(cmd):
    """
    Handles the `delete` action by validating the command arguments and calling the appropriate method to delete a file.

    This method implements the OpenC2 `delete` action. It checks if the `response_requested` argument is valid and
    ensures that the target type is a `File`. If the target is not a `File`, a `badrequest` response is returned. 
    If the target is a `File`, the `delete_file` method is called to perform the deletion.

    Args:
        cmd (Command): The `Command` object containing:
            - `target`: The target of the delete action, which should be of type `File`.
            - `args`: A dictionary of optional arguments, including:
                - `response_requested`: A flag indicating whether a response is requested.

    Returns:
        Response: A response indicating the result of the delete action:
            - `badrequest`: If the arguments are invalid or the target type is unsupported.
            - `notimplemented`: If the target type is unsupported.
            - `ok`: If the delete action was successful.
            - `servererror`: If there is an internal error during file deletion.
            - `unauthorized`: If the file is not authorized for deletion.
            - `notfound`: If the specified file is not found.

    Example:
        cmd = Command(target=File(path='/path/to/file', name='file.txt'), args={'response_requested': ResponseType.complete})
        delete(cmd)
    """
    target = cmd.target.getObj()

    if not isinstance(target, Files):
        return notimplemented("Unsupported Target Type.")
    
    if not target:
        return badrequest("Request should contain at least a file")
    for file in target:
        file_name = file.get("name")
        file_path = file.get("path")
        full_path = os.path.join(file_path, file_name)

        if not is_file_authorized(file_path,file_name):
            return unauthorized('Unauthorized request')

        if os.path.exists(full_path):
            try:
                os.remove(full_path)
                db.delete_file(PRODUCER_ID, file_path, file_name)
            except Exception as e:
                return servererror(f'Error deleting file {file_name}')
        else:
            return notfound(f'File not found {file_name}',)
    return ok('OK')