
import threading, logging, os
from ruamel.yaml import YAML
from openc2lib import Feature
from openc2lib.types.base import Choice
from openc2lib.types.data.duration import Duration
from openc2lib.profiles.fclm.targets.monitor_id import MonitorID
from openc2lib.actuators.fclm.handlers.argument_handler import get_sleep_times
from openc2lib.actuators.fclm.utils.random_name_generator import generate_unique_name
from openc2lib.actuators.fclm.fclm_file_monitor import LogCollectionMonitor
from openc2lib.actuators.fclm.handlers.response_handler import ok, badrequest
from openc2lib.actuators.fclm.configuration.log_config_loader import LogConfigLoader
from openc2lib.actuators.fclm.utils.process_utils import run_monitor
from dotenv import load_dotenv
import openc2lib.profiles.fclm as fclm
load_dotenv()
logger = logging.getLogger(__name__)

class FilebeatActuator(LogCollectionMonitor):
    """
    Actuator class for managing log collection using Filebeat.

    This class extends LogCollectionMonitor and enables dynamic configuration
    and launching of Filebeat agents based on OpenC2 commands. It supports monitoring
    files, sockets, and URIs, applying import/export controls, and defining custom
    output destinations.

    Attributes:
        load (LogConfigLoader): Loader for retrieving configuration parameters.
        filebeat_exe (str): Path to the Filebeat executable.
        base_config (str): Path to the base Filebeat YAML configuration file.
        config_dir (str): Directory where generated Filebeat config files are stored.
        log_dir (str): Directory where log output will be written.
        data_dir (str): Directory for Filebeat data storage.
    """
    def __init__(self, asset_id):
        """
        Initialize the FilebeatActuator.

        Args:
            asset_id (str): The unique identifier for the monitored asset.
        """
        super().__init__(asset_id)
        self.load = LogConfigLoader()
        self.filebeat_exe = os.getenv("FILEBEAT_EXECUTABLE")
        self.base_config = os.getenv("FILEBEAT_BASE_CONFIG")
        self.config_dir = os.getenv("FILEBEAT_CONFIG_DIR")
        self.log_dir = os.getenv("FILEBEAT_LOG_DIR")
        self.data_dir = os.getenv("FILEBEAT_DATA_DIR")

    def _handle_feature(self, f):
        """
        Return configuration data associated with a given feature.

        Args:
            f (Feature): The OpenC2 feature being queried.

        Returns:
            Any: The value of the requested feature.
        """
        match f:
            case Feature.export_fields:
                return self.load.get_export_fields(self.asset_id)
            case Feature.imports_config | Feature.exports_config | Feature.import_controls:
                return self.load.get_feature(self.asset_id, f.name)
            case _:
                return super()._handle_feature(f)

    def _start_monitor(self, cmd):
        """
        Handle a 'start' command by launching a Filebeat monitor.

        Args:
            cmd (Command): An OpenC2 command object containing target and args.

        Returns:
            Response: The result of starting the monitor, delayed or immediate.
        """
        monitor = cmd.target.getObj()
        args = cmd.args or {}
        files, uri, socket = self._parse_monitor(monitor)
        import_controls = args.get("import_controls", {})
        export_fields = args.get("export_fields", [])
        output = self._get_output(args)
        sleep_time, terminate_time = get_sleep_times(args)
        print(f"Terminate time: {terminate_time}")
        monitor_id = generate_unique_name()

        config_file = self._configure_filebeat_yaml(
            files, uri, socket, export_fields, import_controls, output, monitor_id
        )

        cmd_list = [self.filebeat_exe, "-c", config_file]
        if sleep_time > 0:
            threading.Timer(sleep_time, run_monitor, args=(cmd_list, terminate_time, monitor_id)).start()
            return ok("Monitor will start after delay", fclm.Results(monitor_id=MonitorID(monitor_id)))

        return run_monitor(cmd_list, terminate_time, monitor_id)

    def _parse_monitor(self, monitor):
        """
        Extract and classify the type of log source from the monitor object.

        Args:
            monitor (Choice): A Choice object containing the log type and its parameters.

        Returns:
            tuple: A 3-tuple representing (file_path, URI object, Socket object).

        Raises:
            TypeError: If monitor is not a valid Choice object.
        """
        if not isinstance(monitor, Choice):
            raise TypeError("Target must be a LogMonitor (Choice) object")
        log_type, log_obj = monitor.getName(), monitor.getObj()

        match log_type:
            case "file":
                return log_obj.get("path"), None, None
            case "URI":
                return None, log_obj, None
            case "socket":
                return None, None, log_obj
            case _:
                return badrequest(f"Unsupported log type: {log_type}")

    def _get_output(self, args):
        """
        Extract output destination path and file name from arguments.

        Args:
            args (dict): Arguments containing log exporter configuration.

        Returns:
            tuple or None: A tuple of (path, filename) or None if not defined.
        """
        exporter = args.get("log_exporter")
        if exporter and (storage := exporter.get("storage")):
            return storage.get("path", ""), storage.get("name", "filebeat_output")
        return None

    def _configure_filebeat_yaml(self, file, uri, socket, export_fields, import_controls, output, monitor_id):
        """
        Load and modify the base Filebeat configuration with new settings.

        Args:
            file (str): Path to the file to monitor.
            uri (URI): URI to monitor.
            socket (Socket): Socket to monitor.
            export_fields (list): Fields to include in the output.
            import_controls (dict): Controls for input frequency or other parameters.
            output (tuple): Output file path and name.
            monitor_id (str): Unique ID for this monitoring instance.

        Returns:
            str: Path to the generated Filebeat configuration file.

        Raises:
            Exception: If configuration cannot be generated.
        """
        try:
            config = self._load_yaml_config(self.base_config)
            export_fields = self.load.get_export_fields(self.asset_id, export_fields)
            self._update_filebeat_config(config, file, uri, socket, export_fields, import_controls, output, monitor_id)
            return self._write_yaml_config(config, monitor_id)
        except Exception as e:
            logger.error(f"Error configuring Filebeat: {e}")
            raise

    def _update_filebeat_config(self, config, file, uri, socket, export_fields, import_controls, output, monitor_id):
        """
        Update the YAML config dictionary with monitoring sources and parameters.

        Args:
            config (dict): Existing configuration loaded from base config.
            file (str): File path for file monitoring.
            uri (URI): URI object for HTTP/JSON polling.
            socket (Socket): Socket object for socket monitoring.
            export_fields (list): List of fields to include in logs.
            import_controls (dict): Input-related control parameters.
            output (tuple): Output path and filename.
            monitor_id (str): Unique identifier for this monitor.
        """
        config["filebeat.inputs"] = []

        if file:
            file_input = {'type': 'filestream', 'id': 'filestream-input', 'enabled': True, 'paths': [file]}
            config["filebeat.inputs"].append(self._apply_import_controls(file_input, import_controls))

        if uri:
            uri_input = {
                'type': 'httpjson', 'enabled': True,
                'interval': '1m',
                'request.url': uri.get(),
                'request.method': 'GET',
                'response.split': {'target': 'body.data'}
            }
            config["filebeat.inputs"].append(self._apply_import_controls(uri_input, import_controls))

        if socket:
            socket_input = {
                'type': socket.protocol.name,
                'id': 'socket-1',
                'enabled': True,
                'host': f"{socket.host}:{socket.port}"
            }
            config["filebeat.inputs"].append(self._apply_import_controls(socket_input, import_controls))

        if export_fields:
            config.setdefault("processors", []).append({'include_fields': {'fields': export_fields}})

        if output:
            config["output"] = {
                "file": {
                    "path": os.path.join(self.log_dir, output[0]),
                    "filename": output[1],
                    "rotate_every_kb": 3000,
                    "number_of_files": 5
                }
            }

        config.setdefault("path", {})["data"] = os.path.join(self.data_dir, monitor_id)

    def _apply_import_controls(self, input_cfg, import_controls):
        """
        Apply import controls to the given input configuration.

        Args:
            input_cfg (dict): The input configuration to modify.
            import_controls (dict): Dictionary of control parameters.

        Returns:
            dict: Modified input configuration.
        """
        for key, value in (import_controls or {}).items():
            if value is not None:
                input_cfg[key] = self._format_seconds_flex(value) if isinstance(value, Duration) else value
        return input_cfg

    def _load_yaml_config(self, path):
        """
        Load a YAML configuration file.

        Args:
            path (str): Path to the YAML file.

        Returns:
            dict: Parsed YAML configuration.
        """
        try:
            with open(path, "r") as f:
                return YAML().load(f)
        except FileNotFoundError:
            return {}

    def _write_yaml_config(self, config, monitor_id):
        """
        Write the generated configuration to a YAML file.

        Args:
            config (dict): Configuration to write.
            monitor_id (str): Unique ID used to name the file.

        Returns:
            str: Full path to the written YAML file.

        Raises:
            RuntimeError: If the file cannot be written.
        """
        file_path = os.path.join(self.config_dir, f"filebeat_{monitor_id}.yml")
        try:
            with open(file_path, "w") as f:
                YAML().dump(config, f)
            logger.info("Filebeat configuration updated successfully.")
            return file_path
        except Exception as e:
            raise RuntimeError(f"Failed to write Filebeat config: {e}")

    @staticmethod
    def _format_seconds_flex(seconds):
        """
        Convert seconds into a flexible time format (e.g., '1h30m').

        Args:
            seconds (int): Number of seconds.

        Returns:
            str: A flexible time format string.
        """
        seconds = int(seconds)
        h, seconds = divmod(seconds, 3600)
        m, s = divmod(seconds, 60)
        return ''.join(f"{v}{u}" for v, u in ((h, 'h'), (m, 'm'), (s, 's')) if v) or "0s"
