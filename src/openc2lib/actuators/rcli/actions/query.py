import logging
import getpass
import openc2lib.profiles.rcli as rcli
from openc2lib.types.data import Hashes
from openc2lib.types.base import Binaryx
from openc2lib.profiles.rcli.targets import Processes, Files

from openc2lib import ArrayOf, Nsid, Version, Features, ResponseType, Feature , File
from openc2lib.actuators.rcli.cli.commands import Commands
from openc2lib.profiles.rcli.data.state import State
from openc2lib.profiles.rcli.data.process import Process

from openc2lib.actuators.rcli.database.SQLDB import db
from openc2lib.actuators.rcli.user.config import PRODUCER_ID
from openc2lib.actuators.rcli.utils.process_utils import get_process_state
from openc2lib.actuators.rcli.handlers.response_handler import servererror, badrequest, notimplemented, notfound, ok
logger = logging.getLogger(__name__)

""" Supported OpenC2 Version """
OPENC2VERS = Version(1, 0)


def query(cmd):
    """
    Handles the `query` action by validating the command arguments and querying the target.

    This method implements the OpenC2 `query` action. It validates the provided arguments, particularly
    the `response_requested` argument, and checks whether the requested target type (e.g., Features, Process,
    Clicommands, Userdata) is supported. If the target type is valid, the appropriate query function is called 
    (e.g., `query_feature`, `query_process`). Otherwise, a `badrequest` response is returned.

    Args:
        cmd (Command): The `Command` object containing:
            - `target`: The target of the query, which could be of type `Features`, `Process`, `Clicommands`, or `Userdata`.
            - `args`: A dictionary of optional arguments, including:
                - `response_requested`: A flag indicating whether a response is requested.

    Returns:
        Response: A response indicating the result of the query action:
            - `badrequest`: If the arguments are invalid or unsupported target type.
            - `ok`: If the query was successful.
            - `notfound`: If a queried process or resource is not found in the database.
            - `notimplemented`: If a requested feature is not yet implemented.

    Example:
        cmd = Command(target=Features(), args={'response_requested': ResponseType.complete})
        query(cmd)
    """
    logger.info(f"Querying action with command: {cmd}")
    if cmd.args is not None:
        try:
            if cmd.args.get('response_requested') is not None:
                if not (cmd.args['response_requested'] == ResponseType.complete):
                    raise KeyError
        except KeyError:
            return badrequest("Invalid query argument")
    if cmd.target.getObj().__class__ == Features:
        r = query_feature(cmd)
    elif cmd.target.getObj().__class__ == Processes:
        r = query_processes(cmd)
    elif cmd.target.getObj().__class__ == Files:
        r = query_files(cmd)
    else:
        return badrequest("Target not supported.")
    return r

@staticmethod
def query_files(cmd):
    target = cmd.target.getObj()
    try:
        files = Files()
        copied_files = db.get_files(PRODUCER_ID)
        # If target has files, filter based on the target
        if target:
            # Check if there are files in the target and return only those
            for path, name, file_hash in copied_files:
                for file in target:
                    file_name = file.get("name")
                    if file_name and name==file_name:
                        f = File(name=name, path=path, hashes=Hashes({'md5': Binaryx(file_hash)}))
                        files.append(f)
        else:
            # If there are no target files, return all files
            for path, name, file_hash in copied_files:
                files.append(File(name=name, path=path, hashes=Hashes({'md5': Binaryx(file_hash)})))
        res = rcli.Results(file_status=files)
        return ok("Ok", res=res)
    except Exception as e:
        logger.error(f"Error retrieving files: {e}")
        return servererror("Error retrieving files", e)

@staticmethod
def query_feature(cmd):
    """
    Handles the query for supported features, such as OpenC2 versions, profiles, and allowed command targets.

    Implements the 'query features' command, returning the features supported by the OpenC2 actuator.
    The supported features include OpenC2 versions, profiles, and allowed command targets. If a feature is not 
    implemented, a `notimplemented` response is returned.

    Args:
        cmd (Command): The `Command` object containing:
            - `target`: The target of the query, which should be of type `Features`.
            - `args`: A dictionary of optional arguments.

    Returns:
        Response: A response indicating the result of the query action:
            - `ok`: If the query was successful.
            - `notimplemented`: If a feature is not implemented or invalid feature is requested.
            - `servererror`: If an error occurs while processing the command, such as a database or internal failure.

    Example:
        cmd = Command(target=Features(), args={})
        query_feature(cmd)
    """
    logger.info(f"Querying features with command: {cmd}")
    features = {}
    for f in cmd.target.getObj():
        match f:
            case Feature.versions:
                features[Feature.versions.name] = ArrayOf(Version)([OPENC2VERS])
            case Feature.profiles:
                pf = ArrayOf(Nsid)()
                pf.append(Nsid(rcli.Profile.nsid))
                features[Feature.profiles.name] = pf
            case Feature.pairs:
                features[Feature.pairs.name] = rcli.AllowedCommandTarget
            case Feature.clicommands:
                features[Feature.clicommands.name] = Commands.get_available_commands()
            case Feature.rate_limit:
                return notimplemented("Feature 'rate_limit' not yet implemented")
            case _:
                return notimplemented("Invalid feature '" + f + "'")
    res = None
    try:
        res = rcli.Results(features)
        return ok("Ok", res=res)
    except Exception as e:
        return servererror("Server error while processing command",e)

@staticmethod
def query_processes(cmd):
    """
    Queries the status of multiple processes based on their `pid` or `name`.

    If no processes are specified in the `target`, it queries all process IDs from the database.

    Args:
        cmd (Command): The `Command` object containing:
            - `target`: The target of the query, which should be of type `ArrayOf(Process)`.
            - `args`: A dictionary of optional arguments.

    Returns:
        Response: A response indicating the result of the query action:
            - `badrequest`: If neither or both `pid` and `name` are specified in the query.
            - `ok`: If the process statuses are successfully retrieved.
            - `notfound`: If no matching processes are found in the database or system.
            - `servererror`: If there is a failure querying the processes.
    """
    target = cmd.target.getObj()
    # Ensure only "pid" or "name" is set, and no other attributes have values
    allowed_keys = {"pid", "name"}
    extra_keys = []

    # Check each process in target for extra keys
    for process in target:
        for key in process:
            if key not in allowed_keys and process[key] is not None:
                extra_keys.append(key)

    if extra_keys:
        return badrequest("Only 'pid' or 'name' allowed in query processes.")

    pids = []
    names = []
    for process in target:
        pid = process.get("pid")
        name = process.get("name")
        if pid:
            pids.append(pid)
        if name:
            names.append(name)
    process_states = Processes()
    # If no specific processes are provided, fetch all pids from the database
    if not pids and not names:
        try:
            # Fetch both pids and names from the database
            pids_and_names = db.get_pids_and_names(PRODUCER_ID)
            
            # If no processes found in the database
            if not pids_and_names:
                return notfound("No processes found in database.")
            
            # Process the list of tuples (pid, name)
            for pid, name in pids_and_names:
                # Now you have both pid and name to use
                # You can call your process state function, e.g., get_process_state
                process_state = get_process_state(int(pid))
                if isinstance(process_state, State):  # If it's a valid status response
                    # You can process or append it as needed
                    if name:
                        process_states.append(Process(pid=pid, name= name, state=process_state))
                    else:
                        process_states.append(Process(pid=pid, state=process_state))
                else:
                    # Handle error response
                    logger.error(f"Error retrieving process state for PID: {pid}")
                    return servererror(f"Error retrieving process state for PID: {pid}")
                    
            res = rcli.Results(process_status=process_states)
            return ok("Ok", res=res)
        
        except Exception as e:
            logger.error(f"Error retrieving pids from database: {e}")
            return servererror("Error retrieving pids", str(e))
    try:
        # Handle querying processes by name
        for name in names:
            scheduled_pid = db.get_pid_by_name(PRODUCER_ID, name)
            if scheduled_pid:
                process_state = get_process_state(int(scheduled_pid))
                if isinstance(process_state, State):
                    process_states.append(Process(pid=scheduled_pid, name= name, state=process_state))
                else:
                    # If an error response is returned, append the error message
                    return servererror(f"Error retrieving state for process with name {name}: {process_state}")
            else:
                return badrequest(f"Process with name {name} not found in database.")


        # Handle querying processes by pid
        for pid in pids:
            process_state = get_process_state(int(pid))
            if isinstance(process_state, State):
                process_states.append(Process(pid=pid, state=process_state))
            else:
                # If an error response is returned, append the error message
                return servererror(f"Error retrieving state for process with pid {pid}: {process_state}")

        # Return an array of process states
        res = rcli.Results(process_status=process_states)
        return ok("Ok", res=res)

    except Exception as e:
        logger.error(f"Error retrieving process states: {e}")
        return servererror("Error retrieving process states", e)
