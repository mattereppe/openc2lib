import logging
import os
import threading
from openc2lib.actuators.nmf.handlers.argument_handler import get_sleep_times
from openc2lib.actuators.rcli.utils.random_name_generator import generate_unique_name
import openc2lib.profiles.nfm as nfm
from openc2lib.actuators.nmf.utils.bpf_filter_translator import generate_bpf_filter
from openc2lib.profiles.nfm.targets.monitor_id import MonitorID
from openc2lib.actuators.nmf.handlers.response_handler import badrequest, ok
from openc2lib.actuators.nmf.utils.process_utils import run_monitor
from openc2lib.actuators.nmf.nfm_flow_monitor import NetworkFlowMonitor
from openc2lib import Feature
from openc2lib.actuators.nmf.configuration.probe_config_loader import ProbeConfigLoader
from dotenv import load_dotenv
load_dotenv()
# Initialize logger
logger = logging.getLogger(__name__)
class NprobeActuator(NetworkFlowMonitor):
    def __init__(self, asset_id):
        super().__init__(asset_id)
        self.config = ProbeConfigLoader()

    def _handle_feature(self, f):
        print("f")
        match f:
            case Feature.information_elements:
                print("123444")
                a =  self.config.get_info_element(self.asset_id)
                print(a)
                return a
            case Feature.exports:
                return self.config.get_feature(self.asset_id, "exports")
            case Feature.export_options:
                return self.config.get_feature(self.asset_id, "export_options")
            case Feature.flow_format:
                return self.config.get_feature(self.asset_id, "flow_format")
            case Feature.filters:
                return self.config.get_feature(self.asset_id, "filters")
            case _:
                return super()._handle_feature(f)

    def _start_monitor(self, cmd):
        monitor = cmd.target.getObj()
        args = cmd.args or {}
        cmd_list = [os.getenv("NPROBE_EXECUTABLE")]
        cmd_list = self._add_interfaces(cmd_list, monitor)
        cmd_list = self._add_bpf_filter(cmd_list, monitor)
        cmd_list = self._add_information_elements(cmd_list, monitor)
        cmd_list = self._add_exporter_options(cmd_list, args)
        sleep_time, terminate_time = get_sleep_times(args)
        monitor_id = generate_unique_name()
        if sleep_time > 0:
            threading.Timer(sleep_time, run_monitor, args=(cmd_list, terminate_time,monitor_id)).start()
            return ok("Monitor will start after delay", nfm.Results(monitor_id=MonitorID(monitor_id)))
        return run_monitor(cmd_list, terminate_time, monitor_id)

    # Private helper functions
    def _add_interfaces(self, cmd_list, monitor):
        if monitor.get("interfaces"):
            cmd_list += ["--interface"] + [iface.name for iface in monitor.interfaces]
        return cmd_list

    def _add_bpf_filter(self, cmd_list, monitor):
        bpf_filters = generate_bpf_filter(monitor.filter_v4, monitor.filter_v6) if monitor.get("filter_v4") or monitor.get("filter_v6") else None
        if bpf_filters:
            cmd_list += ["-f", f"'{bpf_filters}'"]
        return cmd_list

    def _add_information_elements(self, cmd_list, monitor):
        if monitor.get("information_elements"):
            cmd_list += ["-T"]
            value = self.config.get_info_element(self.asset_id,monitor.information_elements)
            if value is None:
                return badrequest("Information element is not supported")
            cmd_list.extend(value)
        return cmd_list

    def _add_exporter_options(self, cmd_list, args):
        exporter = args.get("exporter")
        if exporter:
            cmd_list = self._add_exporter_storage(cmd_list, exporter)
            cmd_list = self._add_exporter_collectors(cmd_list, exporter)
        
        opts = args.get("exporter_options", {})
        cmd_list = self._add_option(cmd_list, opts, "sampling", "--sampling-rate")
        cmd_list = self._add_option(cmd_list, opts, "aggregate", "--aggregate")
        cmd_list = self._add_option(cmd_list, opts, "buffer", "--collector-buffer-size")
        cmd_list = self._add_option(cmd_list, opts, "timeout", "--collector-timeout")
        cmd_list = self._add_option(cmd_list, opts, "format", "-D")

        return cmd_list

    def _add_exporter_storage(self, cmd_list, exporter):
        if exporter.storage:
            path = os.path.join(exporter.storage.get("path", ""), exporter.storage.get("name", ""))
            cmd_list += ["-P", path]
        return cmd_list

    def _add_exporter_collectors(self, cmd_list, exporter):
        for c in exporter.collectors or []:
            print("x")
            if c.address:
                if c.port:
                    cmd_list += ["--collector", f"{c.address.addr()}:{c.port}"]
        return cmd_list

    def _add_option(self, cmd_list, opts, opt, flag):
        val = opts.get(opt)
        if val:
            cmd_list += [flag, str(val)]
        return cmd_list
