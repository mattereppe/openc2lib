import subprocess
import threading
import time
import shutil
import os
import psutil
import logging
import openc2lib.profiles.rcli as rcli
from openc2lib import ArrayOf,File
#from openc2lib.profiles.rcli.data.extended_process import Process
from openc2lib.profiles.rcli.data.process import Process
from openc2lib.profiles.rcli.data.state import State

from openc2lib.actuators.rcli.cli.commands import Commands
from openc2lib.actuators.rcli.database.SQLDB import db
from openc2lib.actuators.rcli.user.config import PRODUCER_ID
from openc2lib.actuators.rcli.handlers.response_handler import servererror, badrequest, notfound, ok, forbidden, unauthorized


logger = logging.getLogger(__name__)

def get_command(target):
    """
    Determines the executable command based on the target attributes.

    Args:
        target (dict): A dictionary containing command attributes such as:
            - name (str, optional): The command name.
            - command_line (str, optional): Additional command-line arguments.
            - executable (File, optional): A File object representing an executable.

    Returns:
        tuple: (cmd (str), command_name (str)) if successful, otherwise (None, response).
    """
    name = target.get("name")
    command_line = target.get("command_line")
    executable = target.get("executable")
    cmd = None
    
    if name:
        if not Commands.validate_command(name, command_line):
            return None ,badrequest("Command is not supported")
        try:
            cmd = shutil.which(name)
            if command_line:
                cmd = f"{cmd} {command_line}" if cmd else command_line
            return cmd, name
        except Exception as e:
            return None,servererror("Command is not supported",error=e)
    elif executable:
        if isinstance(executable, File):
            path_executable = executable.get("path")
            file_executable = executable.get("name")
            if path_executable:
                ex  = os.path.join(path_executable, file_executable)
            else: 
                ex = file_executable
            cmd = f"docker run --rm -v ~/Downloads/docker-script:/mnt ubuntu bash /mnt/{ex}"
            if command_line:
                cmd = f"{cmd} {command_line}" if cmd else command_line
            return cmd, ex
    else : 
        None, badrequest("Command is not supported")
def open_process(cmd, scheduled_name, terminate_time):
    """
    Starts a new process and returns its process ID (PID) or error message.

    Args:
        cmd (str): The command to execute.
        scheduled_name (str, optional): The name of the scheduled process.
        terminate_time (int, optional): Time (in seconds) after which the process should be terminated.

    Returns:
        response: OK response with process status or a server error response.
    """
    try:
        # Start the process
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        parent_process = psutil.Process(process.pid)
        pid = process.pid
        time.sleep(3)  
        stdout, stderr = None, None
        if process.poll() is not None:  # f"{res}:{arguments.get("start_time")}"`poll()` returns None if the process is still running
            stdout, stderr = process.communicate()
            stdout, stderr = stdout.decode().strip(), stderr.decode().strip()
        if stderr:
            return servererror("Error in processing command", error=stderr)
        if terminate_time and terminate_time > 0:            
            threading.Timer(terminate_time, terminate_process_and_children, args=(pid,)).start()
        if scheduled_name:
            db.add_pid(PRODUCER_ID,pid,scheduled_name)
        else: 
            db.add_pid(PRODUCER_ID,pid)
            return Process(pid=pid,  command_line= cmd)
        

    except Exception as e:
        return servererror("Internal Server Error", error=str(e))

def terminate_process_and_children(process_pid):
    """
    Terminates a process and its child processes.

    Args:
        process_pid (int): The PID of the process to terminate.

    Returns:
        response: OK response if terminated successfully, or an error response.
    """
    try:
        # Get the process object using psutil
        parent_process = psutil.Process(process_pid)
    except psutil.NoSuchProcess:
        db.delete_pid(process_pid)
        return notfound("Process is already terminated")
    except psutil.AccessDenied:
        return forbidden("Access Denied")
    except Exception as e:
        return servererror("Access Denied", error=str(e))

    try:
        # Terminate child processes first
        for child in parent_process.children(recursive=True):
            if child.is_running():
                logger.info(f"Terminating child process {child.pid}")
                child.terminate()
                try:
                    child.wait(timeout=5)  # Give it 5 seconds to terminate
                except psutil.TimeoutExpired:
                    logger.warning(f"Child process {child.pid} did not terminate, force killing.")
                    child.kill()  # Escalate to force kill

        # Terminate the parent process
        if parent_process.is_running():
            logger.info(f"Terminating parent process {parent_process.pid}")
            parent_process.terminate()
            try:
                parent_process.wait(timeout=10)
            except psutil.TimeoutExpired:
                logger.warning(f"Parent process {parent_process.pid} did not terminate, force killing.")
                parent_process.kill()
        # Wait for processes to terminate and clean up to avoid zombie processes
        logger.info(f"Process and its children have been terminated successfully.")
        db.delete_pid(process_pid)
        return ok("Process(es) terminated")
    
    except psutil.TimeoutExpired:
        return servererror("Timeout during termination")
    except psutil.NoSuchProcess:
        db.delete_pid(process_pid)
        return notfound("Process is already terminated")
    except Exception as e:
        return servererror("Error in terminating process(es)", error=str(e))

def get_process_state(pid):
    """
    Retrieves the state of a process based on its PID.

    Args:
        pid (int): The PID of the process.

    Returns:
        response: OK response with process state, or an error response.
    """
    #use the user name which exists in the system
    if are_pids_authorized(str(pid)):
        try:
            process = psutil.Process(pid)
            return State.from_status(process.status())
        except psutil.NoSuchProcess:
            return State.not_found
        except Exception as e:
            return servererror("Error getting process state", error=str(e))
    else:
        return unauthorized("Unauthorized access to process")
        
def terminate_all_processes(pids=None):
    """
    Terminates specified processes if pids are provided and authorized;
    otherwise, terminates all processes started by the producer.

    Args:
        pids (list[int], optional): List of PIDs to terminate. If None, all producer PIDs are terminated.

    Returns:
        response: OK response if successful, or an error response.
    """
    try:
        if pids:
            for pid in pids:
                terminate_process_and_children(pid)
                db.delete_pid(pid)
        else:
            user_pids =list(map(int, db.get_pids(PRODUCER_ID))) 
            for user_pid in user_pids:
                terminate_process_and_children(user_pid)
                db.delete_pid(user_pid)
        return ok("Process(es) terminated")
    except Exception as e:
        return servererror("Error in terminating process(es)", error= str(e))

def are_pids_authorized(pids):
    """
    Checks if one or more PIDs are authorized to be stopped.

    Args:
        pids (int or list[int]): A PID or list of PIDs to check.

    Returns:
        bool: True if all given PIDs are authorized, False otherwise.
    """
    user_pids = db.get_pids(PRODUCER_ID)
    
    if isinstance(pids, str):
        return pids in user_pids
    
    return all(str(pid) in user_pids for pid in pids)

