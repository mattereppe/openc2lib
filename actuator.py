import subprocess
from openc2_actions import Query,Allow,Deny,Update,Delete
import json
import os

class Actuator:
    def __init__(self, actions, targets, args=None):
        self.actions = actions
        self.targets = targets
        self.args = args if args else {}


    def generic_handler(self, action, target, args):
        target_type = list(target.keys())[0]
        target_value = target[target_type]

        # Handle response_requested arguments
        response_requested = args.get('response_requested', 'complete')
        if response_requested == 'none':
            return None
        elif response_requested == 'ack':
            return {"status": 102}
        elif response_requested == 'status':
            return {"status": "in-progress"}
        elif response_requested == 'complete':
            # Simplified to return here directly, removing redundancy
            return {"status": "success", "message": f"Performed {action} on {target_type}: {target_value}"}



def execute_command(self, command):
    # Show the receive command from client
    print("Executing command:", command)
    action = command.get('action')
    target = command.get('target', {})
    args = command.get('args', {})

    # Validate action and target type
    if action not in self.actions:
        return {"status": "error", "message": f"Action '{action}' not supported"}
    if not target or list(target.keys())[0] not in self.targets:
        return {"status": "error", "message": "Target not supported"}

    # Attempt to call the corresponding handler
    method_name = f"{action}_handler"
    handler = getattr(self, method_name, None)
    if callable(handler):
        return handler(target, args)
    else:
        return {"status": "error", "message": f"No handler for action '{action}'"}


# SLPF_Actuator
class SLPF_Actuator(Actuator):
    def __init__(self, actions, targets, args=None):
        super().__init__(actions, targets, args)

    @classmethod
    def execute_SLPF_command(clear, cmd):
        try:
            cmd_list = cmd.split()
            subprocess.run(cmd_list, check=True)
            return {"status": "success", "message": "iptables command executed successfully"}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": f"iptables command failed with return code {e.returncode}"}
        except Exception as e:
            return {"status": "error", "message": f"Unexpected error occurred: {str(e)}"}


class Deny_Slpf(Deny):
    def __init__(self, action_type, target):
        super().__init__(action_type)
        self.target = target

    def execute_Deny(self):
        deny_command = ['iptables', '-A', 'INPUT', '-s', self.target, '-j', 'DROP']
        try:
            result = subprocess.run(deny_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return f"Successfully blocked {self.target}"
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e.stderr}")
            return None

    def validate(self):
        """validate logic should inheritance from target?"""
        if not self.target or not isinstance(self.target, str):
            raise ValueError("The target must be a non-empty string representing an IP address.")

    def __str__(self):
        return f"DenyAction(Type: {self.action_type}, Target: {self.target})"


class Allow_Slpf(Allow):
    def __init__(self, action_type, target):
        super().__init__(action_type)
        self.target = target

    def execute_Allow(self):
        allow_command = ['iptables', '-A', 'INPUT', '-s', self.target, '-j', 'ACCEPT']
        try:
            result = subprocess.run(allow_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True)
            return f"Successfully allowed traffic from {self.target}"
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e.stderr}")
            return None

    def validate(self):
        """validate logic should inheritance from target?"""
        if not self.target or not isinstance(self.target, str):
            raise ValueError("The target must be a non-empty string representing an IP address.")

    def __str__(self):
        return f"AllowAction(Type: {self.action_type}, Target: {self.target})"


class Update_Slpf(Update):
    def __init__(self, action_type, file_path, file_name):
        super().__init__(action_type)
        self.file_path = file_path
        self.file_name = file_name

    def execute_Update(self):
        update_command = f"cp {self.file_path}/{self.file_name} /etc/config_directory/"
        try:

            result = subprocess.run(update_command,
                                    check=True,
                                    shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)
            return f"Successfully updated configuration from {self.file_path}/{self.file_name}"
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while updating configuration: {e.stderr}")
            return None

    def validate(self):
        pass

    def __str__(self):
        return f"UpdateAction(Type: {self.action_type}, File: {self.file_path}/{self.file_name})"

    def to_json(self):
        base_json = json.loads(super().to_json())
        base_json['file_path'] = self.file_path
        base_json['file_name'] = self.file_name
        return json.dumps(base_json, indent=4)


class Delete_Slpf(Delete):
    def __init__(self, action_type, target):
        super().__init__(action_type)
        self.target = target

    def execute(self):
        if isinstance(self.target, str):
            return self.delete_file(self.target)
        elif isinstance(self.target, int):
            return self.delete_slpf_rule_number(self.target)
        else:
            return "Invalid target type."


    def delete_file(self, file_path):
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                return f"File {file_path} successfully deleted."
            except Exception as e:
                return f"Error deleting file: {e}"
        else:
            return "File not found in system."


    def delete_slpf_rule_number(self, rule_number):
        delete_command = ['iptables', '-D', 'INPUT', str(rule_number)]
        try:
            subprocess.run(delete_command,
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           text=True)
            return f"Input rule {rule_number} successfully deleted."
        except subprocess.CalledProcessError as e:
            return f"Error deleting rule: {e.stderr}"

    def validate(self):
        return True

    def __str__(self):
        return f"DeleteAction(Type: {self.action_type}, Target: {self.target})"

    def to_json(self):
        base_json = json.loads(super().to_json())
        base_json['target'] = self.target
        return json.dumps(base_json, indent=4)


class Query_slpf(Query):
    pass



# Nprobe service Actuator
from openc2_actions import start, stop,restart,set

class Nprobe_Actuator(Actuator):
    def __init__(self, actions, targets, args=None):
        super().__init__(actions, targets, args)




class Start_nprobe(start):
    pass


class Stop_nprobe(stop):
    pass


class Restart_nprobe(restart):
    pass


class Set_nprobe(set):
    pass
