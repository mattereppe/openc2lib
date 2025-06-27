import logging
import time

logger = logging.getLogger(__name__)

def get_sleep_times(arguments):
    """
    Calculates the sleep and terminate times based on provided scheduling arguments.

    Args:
        arguments (dict): A dictionary containing scheduling parameters:
            - start_time (int, optional): The UNIX timestamp (ms) for when execution should start.
            - stop_time (int, optional): The UNIX timestamp (ms) for when execution should stop.
            - duration (int, optional): Duration in milliseconds.

    Returns:
        tuple: (sleep_time, terminate_time) in seconds.
            - sleep_time (int): The delay in seconds before execution starts.
            - terminate_time (int): The delay in seconds before execution stops.
    """
    start_time = arguments.get("start_time")
    stop_time = arguments.get("stop_time")
    duration = arguments.get("duration")

    current_time = int(time.time() * 1000)  # Current time in ms
    sleep_time = max((start_time - current_time) // 1000, 0) if start_time else 0
    terminate_time = max((stop_time - current_time) // 1000, 0) if stop_time else max(duration // 1000, 0) if duration else 0

    return sleep_time, terminate_time
