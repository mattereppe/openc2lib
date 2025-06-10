import subprocess, psutil, threading, logging, time
from openc2lib.profiles.nfm import Results

from openc2lib.profiles.nfm.targets.monitor_id import MonitorID
from openc2lib.actuators.nmf.database.SQLDB import SQLDatabase
from openc2lib.actuators.nmf.user.config import PRODUCER_ID
from openc2lib.actuators.nmf.handlers.response_handler import ok, servererror, notfound, forbidden, badrequest
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
        threading.Thread(target=stream_output, args=(proc.stdout, logger.info, "Monitor Output", 100), daemon=True).start()
        threading.Thread(target=stream_output, args=(proc.stderr, logger.error, "Monitor Error", 100), daemon=True).start()

        # Wait briefly to check for early crash
        time.sleep(3)
        if proc.poll() is not None:
            return servererror("Monitor exited early", error=f"Return code {proc.returncode}")

        db.add_pid(PRODUCER_ID, pid, monitor_id)

        if terminate_time:
            threading.Timer(terminate_time, terminate_process_and_children, args=(pid,)).start()

        return ok("Monitor started", res=Results(monitor_id=MonitorID(monitor_id)))
    except Exception as e:
        logger.error(f"[Monitor Exception] {str(e)}")
        return servererror("Execution failed", error=str(e))

    
def terminate_process_and_children(monitor_id):
    try:
        try: 
            pid = int(db.get_pid_by_monitor_id(PRODUCER_ID,monitor_id))
        except:
            return servererror("Process already terminated")
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