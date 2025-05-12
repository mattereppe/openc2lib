import logging
import threading
from openc2lib.profiles.rcli.data.process import Process
from openc2lib.profiles.rcli.targets.processes import Processes
from openc2lib.actuators.rcli.database.SQLDB import db
from openc2lib.actuators.rcli.user.config import PRODUCER_ID

from openc2lib import ResponseType,Duration, DateTime
from openc2lib.actuators.rcli.handlers.argument_handler import get_sleep_times
from openc2lib.actuators.rcli.utils.process_utils import terminate_process_and_children, terminate_all_processes, are_pids_authorized
from openc2lib.actuators.rcli.handlers.response_handler import badrequest, notimplemented, processing, unauthorized

logger = logging.getLogger(__name__)

def stop(cmd):
    """
    Stops a process or performs an action based on the provided command.

    This method implements the `stop` action, which terminates processes 
    either immediately or after a specified delay. It validates the arguments 
    provided in the command and handles different scenarios based on the 
    type of the target.

    Args:
        cmd (Command): The `Command` object, which contains:
            - `target`: The target of the command, typically a process or resource.
            - `args`: A dictionary of optional arguments that can include:
                - `response_requested`: A flag indicating whether a response is requested (e.g., complete).
                - `stop_time`: A `DateTime` object specifying when to stop the process.
                - `duration`: A `Duration` object specifying how long to wait before stopping the process.

    Returns:
        Response: A response indicating the result of the stop action. The response 
                  will contain one of the following status codes:
                  - `badrequest`: If invalid arguments are provided.
                  - `processing`: If the process termination is scheduled for later.
                  - `unauthorized`: If the PID is not authorized for termination.
                  - `notimplemented`: If the target type is unsupported.

    Raises:
        KeyError: If an invalid argument is encountered in the command.
        
    Example:
        cmd = Command(target=Process(pid=123), args={'stop_time': DateTime('2025-04-01T12:00:00Z')})
        stop(cmd)
    """
    logger.info(f"Stopping action with command: {cmd}")
    if cmd.args is not None:
        try:
            if cmd.args.get('response_requested') is not None:
                if not (cmd.args['response_requested']==ResponseType.complete):
                    raise KeyError
            elif cmd.args.get('stop_time') is not None:  
                if not (isinstance(cmd.args['stop_time'],DateTime)):
                    raise KeyError
            elif cmd.args.get('duration') is not None:  
                if not (isinstance(cmd.args['duration'], Duration)):
                    raise KeyError
        except KeyError:
            return badrequest("Invalid stop argument")
    if cmd.target.getObj().__class__ == Processes:
        r = stop_process(cmd)
    else:
        return notimplemented("Unsupported Target Type.")
    return r

def stop_process(cmd):
    """
    Stops a process based on its PID or terminates all processes.

    This function attempts to terminate a specific process based on its PID 
    or terminates all processes if no valid PID is provided. It handles both 
    immediate and delayed termination based on the arguments passed in the 
    command.

    Args:
        cmd (Command): The `Command` object containing:
            - `target`: The target of the command, which should be a process.
            - `args`: A dictionary of optional arguments, including:
                - `stop_time`: A `DateTime` indicating when to stop the process.
                - `duration`: A `Duration` specifying how long to wait before stopping the process.

    Returns:
        Response: A response indicating the result of the stop action:
            - `processing`: If the termination is scheduled to occur later.
            - `unauthorized`: If the process termination request is unauthorized.
            - `notimplemented`: If the PID is invalid or unsupported.
            - `badrequest`: If invalid command is encountered.
            - `response` from `terminate_process_and_children` or `terminate_all_processes` on immediate termination.

    Side Effects:
        - If the `stop_time` or `duration` is greater than 0, the process will be terminated after the specified delay.
        - If the PID is 0 or missing, all processes may be terminated.
        - If the PID is authorized and valid, the targeted process and its children will be terminated.

    Example:
        cmd = Command(target=Process(pid=123), args={'duration': Duration(60)})
        stop_process(cmd)
    """
    target = cmd.target.getObj()
    arguments = cmd.args

    _, terminate_time = get_sleep_times(arguments)

    if not target:    

        return terminate_all_processes()
    else:
        pids: int= []

        for process in target:
            pid = process.get("pid")
            name = process.get("name")
            if pid:
                pids.append(int(process.get("pid")))
            elif name:
                pids.append(int(db.get_pid_by_name(PRODUCER_ID, name)))
            else:
                return badrequest("pid or name is required")
        if not are_pids_authorized(pids):
            return unauthorized('Unauthorized request')
        else:
            if terminate_time > 0:
                threading.Timer(terminate_time, terminate_all_processes, args=(pids,)).start()
                return processing('Process will terminate on time')
            return terminate_all_processes(pids)
        