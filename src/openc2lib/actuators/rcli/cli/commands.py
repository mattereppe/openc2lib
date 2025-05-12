import re
import os
import json
from openc2lib import ArrayOf, Process

class Commands:
    # Load available commands from JSON
    with open(os.path.join(os.path.dirname(__file__), "available_commands.json"), "r") as file:
        available_commands = json.load(file)

    @staticmethod
    def get_available_commands(command_list=None):
        """
        Returns available commands with their respective flags.
        If command_list is provided, only returns the specified commands.
        """
        processes = ArrayOf(Process)()

        # Filter commands based on command_list, if provided
        commands_to_return = (
            list(Commands.available_commands.keys())
            if not command_list
            else [cmd for cmd in command_list if cmd in Commands.available_commands]
        )

        for name in commands_to_return:
            info = Commands.available_commands[name]

            # Construct the command line with path and flags
            command_line = f"<Path> " + " ".join(info["flags"]) if info.get("allow_path", False) else " ".join(info["flags"])

            # Create a Process object
            process = Process({
                "name": name,
                "command_line": command_line
            })
            processes.append(process)

        return processes

    @staticmethod
    def expand_flags(flag_string):
        """Expands combined short flags (e.g., '-la' -> ['-l', '-a'])."""
        flags = flag_string.split()  # Split into individual tokens
        expanded = []

        for flag in flags:
            if flag.startswith('-') and len(flag) > 2 and not flag.startswith('--'):  # Combined short flags
                expanded.extend([f"-{ch}" for ch in flag[1:]])
            else:
                expanded.append(flag)

        return expanded

    @staticmethod
    def validate_command(name, flags_string):
        """Validates the command name and its flags. Returns True if valid, else False."""
        if name not in Commands.available_commands:

            return False

        command_info = Commands.available_commands[name]

        # Expand and separate flags and potential paths
        parts = flags_string.split()
        expanded_flags = Commands.expand_flags(" ".join([p for p in parts if p.startswith('-')]))
        paths = [p for p in parts if not p.startswith('-')]

        # Validate flags
        if not set(expanded_flags).issubset(command_info["flags"]):
            return False

        # Validate paths
        if paths and not command_info.get("allow_path", False):
            return False

        # Prevent all dangerous commands using a blacklist approach
        dangerous_patterns = [
            r"\brm\s+-rf\s+/\b",    # 'rm -rf /'
            r"\bmkfs\b",             # mkfs (filesystem creation)
            r"\bdd\s+if=/dev/zero\b",  # dd with /dev/zero (data destruction)
            r"\b:(){\s*:|:&\s};\b",  # Fork bomb
            r"\bwget\s+http://.*\b",  # Possible malicious download
            r"\bcurl\s+http://.*\b",  # Possible malicious download
            r"\bchmod\s+777\s+/\b",  # chmod 777 (full permissions on root)
            r"\bchown\s+root:root\s+/\b",  # chown root:root on root filesystem
            r"\bshutdown\s+now\b",   # shutdown immediately
            r"\breboot\b",            # reboot command
        ]

        # Regex check for dangerous commands
        for pattern in dangerous_patterns:
            if re.search(pattern, flags_string):
                return False

        return True
