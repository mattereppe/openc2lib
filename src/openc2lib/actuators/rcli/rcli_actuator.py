""" Skeleton `Actuator` for RCLI profile

	This module provides an example to create an `Actuator` for the RCLI profile.
	It only answers to the request for available features.
"""

import logging
from openc2lib import  Actions, Feature
import openc2lib.profiles.rcli as rcli
from openc2lib.actuators.rcli.actions.copy import copy
from openc2lib.actuators.rcli.actions.delete import delete
from openc2lib.actuators.rcli.actions.start import start
from openc2lib.actuators.rcli.actions.stop import stop
from openc2lib.actuators.rcli.actions.query import query
from openc2lib.actuators.rcli.handlers.response_handler import notimplemented, servererror, notfound
logger = logging.getLogger(__name__)
Feature.extend("clicommands",5)

# An implementation of the rcli profile.
class RCLIActuator:
    """ RCLI implementation

        This class provides an implementation of the RCLI `Actuator`.
    """
    
    def run(self, cmd):
        logger.info(f"Received command for processing: {cmd}")
        if not rcli.validate_command(cmd):
            return notimplemented('Invalid Action/Target pair')
        if not rcli.validate_args(cmd):
            return notimplemented('Argument not supported')
        # Check if the Specifiers are actually served by this Actuator
        try:
            if not self.__is_addressed_to_actuator(cmd.actuator.getObj()):
                return notfound('Requested Actuator not available')
        except AttributeError:
            # If no actuator is given, execute the command
            pass
        except Exception as e:
            return servererror('Unable to identify actuator', e)
        try:
            match cmd.action:
                case Actions.query:
                    response = query(cmd)
                case Actions.start:
                    response = start(cmd)
                case Actions.stop:
                    response = stop(cmd)
                case Actions.copy:
                    response = copy(cmd)
                case Actions.delete:
                    response = delete(cmd)
                case _:
                    response = notimplemented('Command not implemented')
        except Exception as e:
            return servererror('Server error while processing command', e)

        logger.info(f"Response generated: {response}")
        return response

    def __is_addressed_to_actuator(self, actuator):
        """ Checks if this Actuator must run the command """
        if len(actuator) == 0:
            # Empty specifier: run the command
            return True
        for k, v in actuator.items():
            try:
                if v == self.asset_id:
                    return True
            except KeyError:
                pass
        return False



