from abc import abstractmethod
import threading, logging
from openc2lib.profiles.fclm import (
    Profile, AllowedCommandTarget, Results, validate_command, validate_args
)
from openc2lib.actuators.fclm.utils.process_utils import terminate_process_and_children
from openc2lib.profiles.fclm.targets.monitor_id import MonitorID   
from openc2lib.profiles.fclm.targets.monitor import LogMonitor

from openc2lib.actuators.fclm.handlers.argument_handler import get_sleep_times
from openc2lib.actuators.fclm.handlers.response_handler import (
    badrequest, notimplemented, ok, servererror, processing, notfound
)
from openc2lib import (
    ResponseType, Duration, DateTime, ArrayOf, Nsid, Version, Actions, Features, Feature
)
Feature.extend("export_fields",11)
Feature.extend("exports_config",12)
Feature.extend("imports_config",13)
Feature.extend("import_controls",14)
logger = logging.getLogger(__name__)
OPENC2VERS = Version(1, 0)
class LogCollectionMonitor:
    asset_id : str = None
    def __init__(self, asset_id):
        self.asset_id = asset_id

    def run(self, cmd):
        logger.info(f"Received command: {cmd}")
        if not validate_command(cmd) or not validate_args(cmd):
            return notimplemented('Invalid command or arguments')
        if cmd.actuator:
            try:
                if not self.__is_addressed_to_actuator(cmd.actuator.getObj()):
                    return notfound('Actuator not found')
            except Exception as e:
                return servererror('Failed to evaluate actuator', error=e)
        try:
            action_map = {
                Actions.query: self.query,
                Actions.start: self.start,
                Actions.stop: self.stop
            }
            return action_map.get(cmd.action, lambda _: notimplemented('Action not implemented'))(cmd)
        except Exception as e:
            logger.error(f"Processing failed: {e}")
            return servererror('Error processing command', error=e)

    def __is_addressed_to_actuator(self, actuator):
        return not actuator or any(
            getattr(self, "asset_id", None) == v for k, v in actuator.items()
        )

    def query(self, cmd):

        args = cmd.args or {}
        if "response_requested" in args and args["response_requested"] != ResponseType.complete:
            return badrequest("Invalid response_requested value")
        if isinstance(cmd.target.getObj(), Features):
            return self._query_feature(cmd)
        return badrequest(f"Query target '{cmd.target.getName()}' not supported")

    def _query_feature(self, cmd):

        features = {}
        for f in cmd.target.getObj():
            res = self._handle_feature(f)
            if res is not None:
                features[f.name] = res
        if not features:
            return notimplemented("No features matched")
        return ok("Features available", res=Results(features))

    def _handle_feature(self, f):
        match f:
            case Feature.versions:
                return ArrayOf(Version)([OPENC2VERS])
            case Feature.profiles:
                return ArrayOf(Nsid)([Nsid(Profile.nsid)])
            case Feature.pairs:
                return AllowedCommandTarget
            case _:
                return None

    def start(self, cmd):
        args = cmd.args or {}
        valid = all([
            args.get("response_requested") in (None, ResponseType.complete),
            isinstance(args.get("start_time", DateTime()), DateTime),
            isinstance(args.get("stop_time", DateTime()), DateTime),
            isinstance(args.get("duration", Duration(0)), Duration)
        ])
        if not valid:
            return badrequest("Invalid start argument")

        if isinstance(cmd.target.getObj(), LogMonitor):
            return self._start_monitor(cmd)
        return notimplemented("Unsupported Target Type")
    
    @abstractmethod
    def _start_monitor(self,cmd):
        """Subclasses must implement this method."""
        pass

    def stop(self, cmd):
        args = cmd.args or {}
        valid = all([
            args.get("response_requested") in (None, ResponseType.complete),
            isinstance(args.get("stop_time", DateTime()), DateTime),
            isinstance(args.get("duration", Duration(0)), Duration)
        ])
        if not valid:
            return badrequest("Invalid stop argument")

        if isinstance(cmd.target.getObj(), MonitorID):
            return self._stop_monitor_id(cmd)
        return notimplemented("Unsupported Target Type")

    def _stop_monitor_id(self, cmd):
        monitor_id = cmd.target.getObj()
        _, terminate_time = get_sleep_times(cmd.args or {})
        if not monitor_id:
            return badrequest("Monitor ID missing")

        if terminate_time:
            threading.Timer(terminate_time, terminate_process_and_children, args=(monitor_id,)).start()
            return processing('Termination scheduled')
        return terminate_process_and_children(monitor_id)


