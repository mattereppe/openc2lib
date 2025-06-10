from openc2lib.actuators.nmf.nfm_flow_monitor import NetworkFlowMonitor
from openc2lib.actuators.nmf.handlers.response_handler import ok
import threading, logging, os
from openc2lib.actuators.nmf.handlers.argument_handler import get_sleep_times
from openc2lib.actuators.nmf.utils.random_name_generator import generate_unique_name
import openc2lib.profiles.nfm as nfm
from openc2lib.actuators.nmf.utils.bpf_filter_translator import generate_bpf_filter
from ruamel.yaml import YAML
from openc2lib.profiles.nfm.targets.monitor_id import MonitorID
from openc2lib import Feature
from openc2lib.actuators.nmf.configuration.probe_config_loader import ProbeConfigLoader
from openc2lib.actuators.nmf.utils.process_utils import run_monitor
from dotenv import load_dotenv
load_dotenv()
logger = logging.getLogger(__name__)

class PacketbeatActuator(NetworkFlowMonitor):
    def __init__(self, asset_id):
        super().__init__(asset_id)
        self.config = ProbeConfigLoader()

    def _handle_feature(self, f):
        match f:
            case Feature.information_elements:
                return self.config.get_info_element(self.asset_id)
            case Feature.exports:
                return self.config.get_feature(self.asset_id, "exports")
            case Feature.export_options:
                return self.config.get_feature(self.asset_id, "export_options")
            case Feature.flow_format:
                return self.config.get_feature(self.asset_id, "flow_fo.monitorrmat")
            case Feature.filters:
                return self.config.get_feature(self.asset_id, "filters")
            case _:
                return super()._handle_feature(f)

    def _start_monitor(self, cmd):
        monitor = cmd.target.getObj()
        args = cmd.args or {}
        
        interfaces, information_elements, output, bpf_filters, sampling = self._parse_monitor(monitor, args)
        sleep_time, terminate_time = get_sleep_times(args)

        if args.get("exporter"):
            output = self._get_output(args)
        monitor_id = generate_unique_name()
        config_file_name = self._configure_packetbeat_yaml(interfaces, information_elements, bpf_filters, output, sampling, monitor_id)
        cmd_list = [os.getenv("PACKETBEAT_EXECUTABLE"), "-c", config_file_name]
        if sleep_time > 0:
            threading.Timer(sleep_time, run_monitor, args=(cmd_list, terminate_time,monitor_id)).start()
            return ok("Monitor will start after delay", nfm.Results(monitor_id=MonitorID(monitor_id)))
        return run_monitor(cmd_list, terminate_time, monitor_id)

    def _parse_monitor(self, monitor, args):
        interfaces = [iface.name for iface in monitor.get("interfaces", [])]
        information_elements = self.config.get_info_element(self.asset_id,monitor.get("information_elements"))
        bpf_filters = generate_bpf_filter(monitor.filter_v4, monitor.filter_v6) if monitor.get("filter_v4") or monitor.get("filter_v6") else None
        sampling = args.get("exporter_options", {}).get("sampling")
        return interfaces, information_elements, None, bpf_filters, sampling

    def _get_output(self, args):
        exporter = args.get("exporter")
        if exporter and exporter.get("storage"):
            return (exporter.storage.get("path", ""), exporter.storage.get("name", ""))
        return None

    def _configure_packetbeat_yaml(self, interfaces, information_elements, bpf_filters, output, sampling, monitor_id):
        try:
            config = self._load_yaml_config(os.getenv("PACKETBEAT_BASE_CONFIG"))
            self._update_packetbeat_config(config, interfaces, information_elements, bpf_filters, output, sampling, monitor_id)
            return self._write_yaml_config(config, monitor_id)
        except Exception as e:
            logger.error(f"Error configuring packetbeat: {e}")
            raise

    def _load_yaml_config(self, path):
        try:
            with open(path, 'r') as f:
                return YAML().load(f)
        except FileNotFoundError:
            return {}

    def _update_packetbeat_config(self, config, interfaces, information_elements, bpf_filters, output, sampling, monitor_id):
        config.setdefault('packetbeat', {})
        if monitor_id:
            # put all paths in ocnfiguration file
            data_path = os.path.join(os.getenv("PACKETBEAT_DATA_DIR"), monitor_id)
            config.setdefault('path', {})['data'] = data_path
        if interfaces:
            config['packetbeat']['interfaces'] = [
                {'device': iface, 'bpf_filter': bpf_filters} for iface in interfaces
            ]
        if bpf_filters:
            for iface_config in config['packetbeat']['interfaces']:
                iface_config['bpf_filter'] = bpf_filters
        if sampling:
            config['packetbeat']['flows'] = {'period': f'{sampling}s'}
        if output:
            log_path = os.path.join(os.getenv("PACKETBEAT_LOG_DIR"), output[0])
            config['output'] = {'file': {
                'path': log_path,
                'filename': output[1],
                'rotate_every_kb': 3000,
                'number_of_files': 5
            }}
        if information_elements:
            config['processors'] = [{'include_fields': {'fields': information_elements}}]

    def _write_yaml_config(self, config, monitor_id):
        file_name = os.path.join(os.getenv("PACKETBEAT_CONFIG_DIR"), f"packetbeat_{monitor_id}.yml")
        try:
            with open(file_name, 'w') as f:
                YAML().dump(config, f)
            logger.info("Packetbeat configuration updated successfully.")
            return file_name
        except Exception as e:
            raise Exception(f"Failed to update Packetbeat configuration: {e}")
