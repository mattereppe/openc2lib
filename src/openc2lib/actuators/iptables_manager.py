""" Iptables Manager

	This module provides a dumb actuator that always answer with a fixed 
	message. Use it for testing only.
"""
import subprocess
import logging

from openc2lib import ArrayOf,ActionTargets, TargetEnum, Nsid, Version,Results, StatusCode, StatusCodeDescription, Actions, Command, Response, IPv4Net, IPv4Connection #, IPv6Net, IPv6Connection


logger = logging.getLogger(__name__)

# A dumb actuator that does not implement any function but can
# be used to test the openc2 communication.
class IptablesManager:

	@staticmethod
	def parse_iptables(cmd):
		try:
		     result = subprocess.run(cmd,
		                             shell=True,
		                             check=True,
		                             stdout=subprocess.PIPE,
		                             stderr=subprocess.PIPE)
		     if result.returncode == 0:
		         logger.debug("Command executed successfully: %s", cmd)
		         logger.debug("Output: %s", result)
		         return 200
		     else:
		         logger.debug("Command failed: %s", cmd)
		         logger.debug("Output: %s", result)
		         return 500
		except subprocess.CalledProcessError as e:
		     logger.debug("Execution error for command: %s", cmd)
		     logger.debug("Exception: %s", str(e))
		     return 500

	@staticmethod
	def insert_rule(target, iptables_target):
		logger.debug("Starting insert rule %s %s", target, iptables_target)
		supported_targets = ['ipv4_connection', 'ipv6_connection', 'ipv4_net', 'ipv6_net']
		cmd = None
		base_cmd = "iptables -A INPUT"

		logger.debug("type of target: %s", type(target))
		if isinstance(target, IPv4Connection): # or isinstance(target.IPv6Connection):
			src_ip = target.src_addr
			dst_ip = target.dst_addr
			logger.debug("protocol: %s", protocol)
			src_port = target.src_port
			dst_port = target.dst_port
			protocol = target.protocol.name
			logger.debug("protocol: %s", protocol)
			cmd = f"{base_cmd} -p {protocol}"
			if src_ip:
				cmd += f" -s {src_ip}"
			if dst_ip:
				cmd += f" -d {dst_ip}"
			if src_port:
				cmd += f" --sport {src_port}"
			if dst_port:
				cmd += f" --dport {dst_port}"
			cmd += f" -j {iptables_target}"

		elif isinstance(target, IPv4Net): # or isinstance(target.IPv6Net):
			ip = target.addr()
			cidr = target.prefix()
			cmd = f"{base_cmd} -s {ip}"
			if cidr:
				cmd += f"/{cidr}"
			cmd += f" -j {iptables_target}"
		else:
			return 501


		if cmd:
			result = IptablesManager.parse_iptables([cmd])
#	result[0]['command'] = cmd
			return result, cmd

		return 500

	@staticmethod
	def delete_rule(cmd):
#		cmd_parts = additional_cmds[0].split()
#		if len(cmd_parts) > 1 and cmd_parts[1].startswith('-'):
#			cmd_parts[1] = '-D'
#			cmd = ' '.join(cmd_parts)
		return IptablesManager.parse_iptables(cmd)

	def modify_command_for_deletion(cmd):
		cmd_parts = cmd.split()
		if "INPUT" in cmd_parts:
			input_index = cmd_parts.index("INPUT")
			if input_index + 1 < len(cmd_parts) and cmd_parts[input_index + 1].isdigit():
				del cmd_parts[input_index + 1]
		for i, part in enumerate(cmd_parts):
			if part.startswith('-') and not part.startswith('-D'):
				cmd_parts[i] = '-D'
				break
		modified_cmd = ' '.join(cmd_parts)
		return modified_cmd

