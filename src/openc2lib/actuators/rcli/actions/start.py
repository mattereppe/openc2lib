import logging
import threading
from openc2lib import ResponseType,  Duration, DateTime
from openc2lib.profiles.rcli.data.process import Process

import openc2lib.profiles.rcli as rcli
from openc2lib.actuators.rcli.handlers.argument_handler import get_sleep_times
from openc2lib.actuators.rcli.utils.random_name_generator import generate_unique_name
from openc2lib.actuators.rcli.utils.process_utils import open_process, get_command
from openc2lib.actuators.rcli.handlers.response_handler import badrequest, notimplemented, ok
from openc2lib.profiles.rcli.targets.processes import Processes


logger = logging.getLogger(__name__)

def start(cmd):
    """
    Handles the `start` action by validating arguments and initiating the process start.

    This method implements the OpenC2 `start` action. It validates the provided arguments, including 
    `response_requested`, `start_time`, `stop_time`, and `duration`. If any arguments are invalid, 
    a `badrequest` response is returned. If the target is of type `Process`, the `start_process` function 
    is called to initiate the process. Otherwise, a `notimplemented` response is returned.

    Args:
        cmd (Command): The `Command` object containing:
            - `target`: The target of the command, which should be a `Process` object.
            - `args`: A dictionary of optional arguments, including:
                - `response_requested`: A flag indicating if a response is requested.
                - `start_time`: A `DateTime` indicating when to start the process.
                - `stop_time`: A `DateTime` indicating when to stop the process.
                - `duration`: A `Duration` specifying the wait time before starting the process.

    Returns:
        Response: A response indicating the result of the `start` action:
            - `badrequest`: If command is invalid.
            - `notimplemented`: If the target is not a `Process`.
            - `ok`: If the process is successfully started.

    Example:
        cmd = Command(target=Process(name="example_process"), args={'start_time': DateTime("2025-04-01T10:00:00Z")})
        start(cmd)
    """
    logger.info(f"Starting action with command: {cmd}")
    if cmd.args is not None:
        try:
            if cmd.args.get('response_requested') is not None:
                if not (cmd.args['response_requested']==ResponseType.complete):
                    raise KeyError
            elif cmd.args.get('start_time') is not None:
                if not (isinstance(cmd.args['start_time'], DateTime)):
                    raise KeyError
            elif cmd.args.get('stop_time') is not None:  
                if not (isinstance(cmd.args['stop_time'],DateTime)):
                    raise KeyError
            elif cmd.args.get('duration') is not None:  
                if not (isinstance(cmd.args['duration'], Duration)):
                    raise KeyError
        except KeyError:
            return badrequest("Invalid start argument")
    if cmd.target.getObj().__class__ == Processes:
        r = start_process(cmd)
    else:
        return notimplemented("Unsupported Target Type.")
    return r

def start_process(cmd):
    """
    Starts a process by executing allowed commands or an executable in isolation.

    This function handles both immediate and delayed execution of a process based on the arguments passed in 
    the `cmd` object. If a `start_time` or `duration` is provided, the process will be started after the 
    specified delay. It also generates a unique process name for delayed starts.

    Args:
        cmd (Command): The `Command` object containing:
            - `target`: The target of the command, which should be a `Process` object.
            - `args`: A dictionary of optional arguments, including:
                - `start_time`: A `DateTime` indicating when to start the process.
                - `stop_time`: A `DateTime` indicating when to stop the process.
                - `duration`: A `Duration` specifying how long to wait before starting the process.

    Returns:
        Response: A response indicating the result of the start action:
            - `ok`: If the process was started immediately or scheduled successfully.
            - `badrequest`: If the command is invalid.
            - `notimplemented`: If the target is not a supported process.

    Side Effects:
        - If `start_time` or `duration` is provided, the process will be scheduled to start after the specified delay.
        - A unique process name is generated for delayed starts.
        - The process is executed immediately if no delay is specified.
    """
    target = cmd.target.getObj()
    if not target:
        return badrequest("At one command is needed")
    arguments = cmd.args
    sleep_time, terminate_time = get_sleep_times(arguments)
    processes = Processes()
    for procs in target:
        cmd, res = get_command(procs)
        if not cmd:
            return res
        if sleep_time > 0:
            scheduled_name= generate_unique_name()
            threading.Timer(sleep_time, open_process, args=(cmd,scheduled_name,terminate_time)).start()
            processes.append(Process(name=scheduled_name, command_line= cmd))
        else:
            proc = open_process(cmd,None, terminate_time)
            if not isinstance(proc,Process):
                return proc
            else:
                processes.append(proc)
    return ok("OK", res=rcli.Results(process_status=processes))    
