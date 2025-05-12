import subprocess, psutil, threading, logging, time
from openc2lib.profiles.fclm import Results
from openc2lib.profiles.fclm.targets.monitor_id import MonitorID
from openc2lib.actuators.fclm.database.SQLDB import SQLDatabase
from openc2lib.actuators.fclm.user.config import PRODUCER_ID
from openc2lib.actuators.fclm.handlers.response_handler import ok, servererror, notfound, forbidden
logger = logging.getLogger(__name__)
db = SQLDatabase()
def stream_output(pipe, log_fn, label, max_lines=10):
    line_count = 0
    for line in iter(pipe.readline, ''):
        if line_count >= max_lines:
            log_fn(f"[{label}] Output limit of {max_lines} lines reached, stopping stream.")
            break
        log_fn(f"[{label}] {line.strip()}")
        line_count += 1
    pipe.close()

def run_monitor(command, terminate_time, monitor_id):
    """
    Starts a monitoring process using the given command and manages its lifecycle.

    The function launches the process, attempts to capture initial output/errors within a short timeout,
    and registers the process PID in the database. If a terminate time is provided, the process is scheduled
    to be terminated after that duration.

    Args:
        command (list[str]): The command to execute as a list of arguments.
        terminate_time (int | float | None): Time in seconds after which the process should be terminated. 
                                             If None, the process will not be scheduled for termination.
        monitor_id (str): A unique identifier associated with this monitoring session.

    Returns:
        Response: A standardized response indicating success or failure using the response handler.
    """
    try:
        logger.info(f"Executing: {' '.join(command)}")
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
            text=True
        )
        pid = proc.pid

        # Start threads for logging output in real time
        threading.Thread(target=stream_output, args=(proc.stdout, logger.info, "Monitor Output",10), daemon=True).start()
        threading.Thread(target=stream_output, args=(proc.stderr, logger.error, "Monitor Error",10), daemon=True).start()

        # Wait briefly to check for early crash
        time.sleep(3)
        if proc.poll() is not None:
            return servererror("Monitor exited early", error=f"Return code {proc.returncode}")
        db.add_pid(PRODUCER_ID,pid,monitor_id)
        if terminate_time:
            threading.Timer(terminate_time, terminate_process_and_children, args=(pid,)).start()
        return ok("Monitor started", res=Results(monitor_id=MonitorID(monitor_id)))
    except Exception as e:
        return servererror("Execution failed", error=str(e))
    
def terminate_process_and_children(monitor_id):
    """
    Terminates a process and all its child processes by either PID or monitor ID.

    If the input is an integer or numeric string, it is treated as a PID.
    Otherwise, the function queries the database using the monitor ID to resolve the PID.
    After killing the process tree, the PID is removed from the database.

    Args:
        monitor_id (str | int): The monitor ID (or direct PID) identifying the process to terminate.

    Returns:
        Response: A standardized response indicating success or the type of failure (e.g., not found, forbidden).
    """
    try:
        if isinstance(monitor_id, int) or str(monitor_id).isdigit():
            print('pid',monitor_id)
            pid = int(monitor_id)
        else:
            try:
                pid = int(db.get_pid_by_monitor_id(PRODUCER_ID, monitor_id))
                print('id',monitor_id)
            except Exception:
                return servererror("Process already terminated or monitor ID not found")
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):
            if child.is_running():
                child.terminate()
                try:
                    child.wait(timeout=5)
                except psutil.TimeoutExpired:
                    child.kill()
        if parent.is_running():
            parent.terminate()
            try:
                parent.wait(timeout=10)
            except psutil.TimeoutExpired:
                parent.kill()
        db.delete_pid(pid)
        return ok("Process terminated")
    except psutil.NoSuchProcess:
        db.delete_pid(pid)
        return notfound("Process already terminated")
    except psutil.AccessDenied:
        return forbidden("Access denied")
    except Exception as e:
        return servererror("Termination failed", error=str(e))