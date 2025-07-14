""" Skeleton `Actuator` for SLPF profile

    This module provides an example to create an `Actuator` for the SLPF profile.
"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED

import os
import logging
import uuid
import time
from datetime import datetime
import threading
import atexit
import hashlib

from enum import Enum

from .sql_database import SQLDatabase

from openc2lib import ArrayOf, File, Nsid, Version,Actions, Command, Response, StatusCode, StatusCodeDescription, Features, ResponseType, Feature, IPv4Net, IPv4Connection , IPv6Net, IPv6Connection, DateTime, Duration, Binaryx, L4Protocol, Port
from openc2lib.core.actions import Actions
import openc2lib.profiles.slpf as slpf 
from openc2lib.profiles.slpf.data import DropProcess

logger = logging.getLogger(__name__)

OPENC2VERS=Version(1,0)
""" Supported OpenC2 Version """

MY_IDS = {'hostname': None,
            'named_group': None,
            'asset_id': None,
            'asset_tuple': None }

class SLPFActuator:
    """ `SLPF Actuator implementation`.

        This class provides an implementation of the `SLPF Actuator`.
    """

    
    class Mode(Enum):
        file = 'File'
        db = 'Database'

    def __init__(self,hostname=None, named_group=None, asset_id=None, asset_tuple=None, db_directory_path=None, db_name=None, db_commands_table_name=None, db_jobs_table_name=None, update_directory_path=None):
        """ Initialization of the `SLPF Actuator`.

            This method initializes a `sqlite3` database to store `allow` and `deny` OpenC2 commands as well as `APScheduler jobs` (for non executed scheduled commands in case of SLPF Actuator `shutdown`),  
            restores `persistent commands`, 
            initializes an `APScheduler scheduler` for managing commands that are set to be executed at a specific `start time` or `stop time` and 
            registers `slpf_exit()` method to be executed upon SLPF Actuator termination.

            :param hostname: SLPF Actuator hostname.
            :type hostname: str
            :param named_group: SLPF Actuator group.
            :type named_group: str
            :param asset_id: SLPF Actuator asset id.
            :type asset_id: str
            :param asset_tuple: SLPF Actuator asset tuple.
            :type asset_tuple: str
            :param db_directory_path: sqlite3 database directory path.
            :type db_directory_path: str
            :param db_name: sqlite3 database name.
            :type db_name: str
            :param db_commands_table_name: Name of the `commands` table in the sqlite3 database.
            :type db_commands_table_name: str
            :param db_jobs_table_name: Name of the `APScheduler jobs` table in the sqlite3 database.
            :type db_jobs_table_name: str
            :param misfire_grace_time: Seconds after the designated runtime that the `APScheduler job` is still allowed to be run, because of a `shutdown`.
            :type misfire_grace_time: int
            :param update_directory_path: Path to the directory containing files to be used as update.
            :type update_directory_path: str
        """
        
        # Needed in development phase
        # otherwise werkzeug development server launches the function twice
        # that is bad for the scheduler
        if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            MY_IDS['hostname'] = hostname
            MY_IDS['named_group'] = named_group
            MY_IDS['asset_id'] = asset_id if asset_id else " "
            MY_IDS['asset_tuple'] = asset_tuple

            self.tag = "[SLPF-" + MY_IDS['asset_id'] + "]"

            try:
            #   Path where update files are stored
                self.update_directory_path = update_directory_path if update_directory_path else os.path.dirname(os.path.abspath(__file__))
                if not os.path.exists(self.update_directory_path):
                    raise ValueError("Update directory path does not exists")
            #   Initializing database
                logger.info(self.tag + " Initializing database")
                self.db_directory_path = db_directory_path if db_directory_path else os.path.dirname(os.path.abspath(__file__))
                self.db_name = db_name if db_name else "slpf_commands.sqlite"
                if not os.path.exists(self.db_directory_path):
                    raise ValueError("Database directory path does not exists")
                self.db_commands_table_name = db_commands_table_name if db_commands_table_name else "iptables_commands"
                self.db_jobs_table_name = db_jobs_table_name if db_jobs_table_name else "iptables_jobs"         
                self.db = SQLDatabase(os.path.join(self.db_directory_path, self.db_name), self.db_commands_table_name, self.db_jobs_table_name)
            #   Checking SLPF Mode
                self.mode = SLPFActuator.Mode.file if self.db.is_empty() else SLPFActuator.Mode.db
                logger.info(self.tag + " " + self.mode.value + " mode")
            #   Restoring persistent commands
                self.restore_persistent_commands()                
            #   Initializing scheduler
                logger.info(self.tag + " Initializing scheduler")
                # Setting misfire grace time to 1 day
                self.misfire_grace_time = 86400
                self.scheduler = BackgroundScheduler()
                self.scheduler.add_listener(lambda event: self.scheduler_listener(event), EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
                self.restore_persistent_jobs()
                self.scheduler.start()
            #   Registering exit function
                atexit.register(self.slpf_exit)
                logger.info(self.tag + " Initialization executed successfully")
            except Exception as e:
                logger.info(self.tag + " Initialization error: %s", str(e))
                raise e
            
    def execute_allow_command(self, target, direction):
        """ Implementation of `allow` action

            Each Actuator must override this method in order to implement the allow action.

            :param target: The target of the allow action.
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection
            :param direction: Specifies whether to allow incoming traffic, outgoing traffic or both for the specified target.
            :type direction: Direction
        """
        pass

    def execute_deny_command(self, target, direction, drop_process):
        """ Implementation of `deny` action

            Each Actuator must override this method in order to implement the deny action.

            :param target: The target of the deny action.
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection
            :param direction: Specifies whether to deny incoming traffic, outgoing traffic or both for the specified target.
            :type direction: Direction
            :param drop_process: Specifies how to handle denied packets: 
                                `none` drop the packet and do not send any notification to the source of the packet,
                                `reject` drop the packet and send an ICMP host unreachable (or equivalent) to the source of the packet,
                                `false_ack` drop the packet and send a false acknowledgment.
            :type drop_process: DropProcess
        """
        pass

    def validate_action_target_args(self, action, target, args):
        """ This method should be implemented if an Actuator does not implements some SLPF `action`, `Target`, `features` 
            or has to perform some `checks` before executing an action (e.g: check if the file extension of an update target is supported).
            
            Possibles `action` values are `allow`, `deny` and `update` (since query and delete action are already fully validated).

            This method should validates `Target` and `Args` of an `allow` action for a specific Actuator.
            
            This method should validates `Target` and `Args` of a `deny` action for a specific Actuator.
            
            This method should validates `Target` of an `update` action for a specific Actuator, since `Args` are already fully validated.

            :param action: The action to validate.
            :type action: Actions
            :param target: The target of the action to validate.
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection/File
            :param args: The `Args` of the action to validate. 
                        Contains the `direction` argument in case of `allow` action, 
                        `direction` and `drop_process` arguments in case of `deny` action
                        and has a `None` value in case of `update` action.
            :type args: slpf.Args
        """
        pass

    def execute_delete_command(self, command_to_delete):
        """ Implementation of `delete` action

            Each Actuator must override this method in order to implement the delete action.

            :param command_to_delete: The OpenC2 `Command` to delete.
            :type command_to_delete: Command
        """
        pass

    def execute_update_command(self, name, path):
        """ Implementation of `update` action

            Each Actuator must override this method in order to implement the update action.

            :param name: The `name` of the target file.
            :type name: str
            :param path: The `path` of the target file.
            :type path: str
        """
        pass

    def save_persistent_commands(self):
        """ Each Actuator must override this method in order to `save` all setted commands. """
        pass

    def restore_persistent_commands(self):
        """ Each Actuator must override this method in order to `restore` all commands saved with `save_persistent_commands()`. """
        pass

    def clean_actuator_rules(self):
        """ Each Actuator must override this method in order to set the `SLPF Actuator` in `DB mode` deleting all setted commands. """
        pass
      

    def run(self, cmd):
        # Check if the Command is compliant with the implemented profile
        if not slpf.validate_command(cmd):
            return Response(status=StatusCode.NOTIMPLEMENTED, status_text='Invalid Action/Target pair')
        if not slpf.validate_args(cmd):
            return Response(status=StatusCode.NOTIMPLEMENTED, status_text='Option not supported')

        # Check if the Specifiers are actually served by this Actuator
        try:
            if not self.__is_addressed_to_actuator(cmd.actuator.getObj()):
                return Response(status=StatusCode.NOTFOUND, status_text='Requested Actuator not available')
        except AttributeError:
            # If no actuator is given, execute the command
            pass
        except Exception as e:
            return Response(status=StatusCode.INTERNALERROR, status_text='Unable to identify actuator')
        
        try:
            match cmd.action:
                case Actions.query:
                    response = self.query(cmd)
                case Actions.allow:
                    response = self.allow(cmd)
                case Actions.deny:
                    response = self.deny(cmd)
                case Actions.update:
                    response = self.update(cmd)
                case Actions.delete:
                    response = self.delete(cmd)
                case _:
                    response = self.__notimplemented(cmd)
        except Exception as e:
            return self.__servererror(cmd, e)

        return response


    def __is_addressed_to_actuator(self, actuator):
        """ Checks if this Actuator must run the command """
        if len(actuator) == 0:
            # Empty specifier: run the command
            return True

        for k,v in actuator.items():		
            try:
                #if v == MY_IDS[k]:
                if(v == self.asset_id):
                    return True
            except KeyError:
                pass

        return False
        

    def query(self, cmd):
        """ `Query` action

            This method implements the `query` action.

            :param cmd: The `Command` including `Target` and optional `Args`.
            :type cmd: Command
            :return: A `Response` including the result of the query and appropriate status code and messages.
        """
        
        # Sec. 4.1 Implementation of the 'query features' command
        if cmd.args is not None:
            if ( len(cmd.args) > 1 ):
                return Response(satus=StatusCode.BADREQUEST, statust_text="Invalid query argument")
            if ( len(cmd.args) == 1 ):
                try:
                    if cmd.args['response_requested'] != ResponseType.complete:
                        raise KeyError
                except KeyError:
                    return Response(status=StatusCode.BADREQUEST, status_text="Invalid query argument")

        if ( cmd.target.getObj().__class__ == Features):
            r = self.query_feature(cmd)
        else:
            return Response(status=StatusCode.BADREQUEST, status_text="Querying " + cmd.target.getName() + " not supported")

        return r


    def query_feature(self, cmd):
        """ Query features

            Implements the 'query features' command according to the requirements in Sec. 4.1 of the Language Specification.

            Each Actuator must override this method if the query feature command cannot be completely implemented.
        """
        features = {}
        for f in cmd.target.getObj():
            match f:
                case Feature.versions:
                    features[Feature.versions.name]=ArrayOf(Version)([OPENC2VERS])	
                case Feature.profiles:
                    pf = ArrayOf(Nsid)()
                    pf.append(Nsid(slpf.Profile.nsid))
                    features[Feature.profiles.name]=pf
                case Feature.pairs:
                    features[Feature.pairs.name]=slpf.AllowedCommandTarget
                case Feature.rate_limit:
                    return Response(status=StatusCode.NOTIMPLEMENTED, status_text="Feature 'rate_limit' not yet implemented")
                case _:
                    return Response(status=StatusCode.NOTIMPLEMENTED, status_text="Invalid feature '" + f + "'")

        res = None
        try:
            res = slpf.Results(features)
        except Exception as e:
            return self.__servererror(cmd, e)

        return  Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK], results=res)


    def allow(self, cmd):
        """ `Allow` action

            This method implements the `allow` action.

            :param cmd: The `Command` including `Target` and optional `Args`.
            :type cmd: Command
            :return: A `Response` including the result of the allow command and appropriate status code and messages.
        """

        try:
            return self.allow_deny_handler(cmd)
        except Exception as e:
            return self.__servererror(cmd, e)


    def deny(self, cmd):
        """ `Deny` action

            This method implements the `deny` action.
            
            :param cmd: The `Command` including `Target` and optional `Args`.
            :type cmd: Command
            :return: A `Response` including the result of the deny command and appropriate status code and messages.
        """

        try:
            return self.allow_deny_handler(cmd)           
        except Exception as e:
            return self.__servererror(cmd, e)
        

    def allow_deny_handler(self, cmd):
        """ This method manages the execution of `allow` and `deny` commands.

            Validates and manages allow and deny `Target` and `Args`, 
            sets the SLPF Actuator in `db mode` (database rules in use) iff database is empty, 
            inserts the command in the `database` 
            and sets the allow or deny action to be executed at a specific `start` and/or `stop time`.

            :param cmd: The `Command` including `Target` and optional `Args`.
            :type cmd: Command
            :return: A `Response` including the result of the allow or deny command and appropriate status code and messages.
        """

        try:
            action = cmd.action
            target = cmd.target.getObj()
            args = cmd.args

        #   Validating target
            if type(target) != IPv4Net and type(target) != IPv6Net and type(target) != IPv4Connection and type(target) != IPv6Connection:
                raise TypeError("Invalid target type")
            if type(target) == IPv4Connection or type(target) == IPv6Connection:
                if target.protocol and target.protocol != L4Protocol.tcp and target.protocol != L4Protocol.udp and target.protocol != L4Protocol.sctp:
                    if target.src_port or target.dst_port:
                        raise ValueError(StatusCode.BADREQUEST, "Source/Destination port not supported with provided protocol")
                if not target.protocol and (target.src_port or target.dst_port):
                        raise ValueError(StatusCode.BADREQUEST, "Protocol must be provided")

                addr_type = IPv4Net if type(target) == IPv4Connection else IPv6Net
                if ((target.src_addr and type(target.src_addr) != addr_type)
                    or (target.dst_addr and type(target.dst_addr) != addr_type)
                    or (target.protocol and type(target.protocol) != L4Protocol)
                    or (target.src_port and type(target.src_port) != Port)
                    or (target.dst_port and type(target.dst_port) != Port)):
                        raise TypeError("Invalid target type")

        #   Validating args
            if ( ('response_requested' in args and type(args['response_requested']) != ResponseType)
                or ('insert_rule' in args and type(args['insert_rule']) != slpf.RuleID)
                or ('direction' in args and type(args['direction']) != slpf.Direction)
                or ('persistent' in args and type(args['persistent']) != bool)
                or ('drop_process' in args and type(args['drop_process']) != DropProcess)
                or ('start_time' in args and type(args['start_time']) != DateTime)
                or ('stop_time' in args and type(args['stop_time']) != DateTime)
                or ('duration' in args and type(args['duration']) != Duration)):
                    tmp_str = "Invalid allow argument type" if action == Actions.allow else "Invalid deny argument type"
                    raise TypeError(tmp_str)

            if 'insert_rule' in args:
                if args['response_requested'] != ResponseType.complete:
                        raise ValueError(StatusCode.BADREQUEST, "Response requested must be complete with insert rule argument")
                if self.db.find_command(args['insert_rule']):
                    raise ValueError(StatusCode.NOTIMPLEMENTED, "Rule number currently in use")

            if ('start_time' in args) and ('stop_time' in args): 
                if 'duration' in args:
                    raise ValueError(StatusCode.BADREQUEST, "Only two arguments between start time, stop time and duration can be specified")
                if args['start_time'] > args['stop_time']:
                    raise ValueError(StatusCode.BADREQUEST, "Start time greater than stop time")
            if'stop_time' in args and (args['stop_time'] < time.time() * 1000):
                raise ValueError(StatusCode.BADREQUEST, "Stop time already expired")
       
        #   Setting default args values
            if not 'direction' in args:
                args['direction'] = slpf.Direction.both
            if action == Actions.deny and not 'drop_process' in args:
                args['drop_process'] = DropProcess.none

        #   Validating action, target, args for specific implementation
            temp_args = {'direction': args['direction']}
            if 'drop_process' in args:
                temp_args['drop_process'] = args['drop_process']
            self.validate_action_target_args(action=action,
                                             target=target,
                                             args=temp_args)

        #   Calculating start/stop time
            if 'start_time' in args:
                args['start_time'] = args['start_time'] / 1000
            else:
                if 'stop_time' in args and 'duration' in args:
                    args['start_time'] = (args['stop_time'] - args['duration']) / 1000
                else:
                    args['start_time'] = time.time()
            if 'stop_time' in args:
                args['stop_time'] = args['stop_time'] / 1000
            else:
                if 'duration' in args:
                    args['stop_time'] = (args['start_time']*1000 + args['duration']) / 1000

        #   Setting SLPF Actuator in db mode
        #   Clean all rules in specific implementation
        #   Starting to use db rules
            if self.mode == SLPFActuator.Mode.file:
                self.mode = SLPFActuator.Mode.db
                logger.info(self.tag + " " + self.mode.value + " mode setted") 
                self.clean_actuator_rules()
                self.save_persistent_commands()

        #   Generating job ids
            job_ids = {'start_job_id': self.generate_unique_job_id(),
                       'stop_job_id': self.generate_unique_job_id() if 'stop_time' in args else None,
                       'my_id': None }

        #   Inserting commands in db   
            logger.info(self.tag + " Inserting command in database")
            rule_number = self.db_handler(action, target, args, job_ids)

        #   Managing the scheduler    
            start_time = datetime.fromtimestamp(args['start_time'])            
            self.scheduler.add_job(self.allow_deny_execution_wrapper,
                                   'date',
                                   next_run_time=start_time,
                                   args=[action, rule_number],
                                   kwargs={'target': target, **temp_args},
                                   id=job_ids['start_job_id'],
                                   misfire_grace_time=self.misfire_grace_time)
            if 'stop_time' in args:
#               Just needed args                
                command = Command(action, target, slpf.Args(temp_args))
                job_ids['my_id'] = job_ids['stop_job_id']
                stop_time = datetime.fromtimestamp(args['stop_time'])
                self.scheduler.add_job(self.delete_handler,
                                       'date',
                                       next_run_time=stop_time,
                                       kwargs={'command_to_delete': command, 'rule_number': rule_number, 'job_ids': job_ids},
                                       id=job_ids['stop_job_id'],
                                       misfire_grace_time=self.misfire_grace_time)              
            
            res = slpf.Results(rule_number=slpf.RuleID(rule_number))
            return Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK], results=res)
        except TypeError as e:
            return Response(status=StatusCode.BADREQUEST, status_text=str(e))
        except ValueError as e:
            return Response(status=e.args[0], status_text=e.args[1])
        except Exception as e:
            return Response(status=StatusCode.INTERNALERROR, status_text="Rule not updated")


    def allow_deny_execution_wrapper(self, *args, **kwargs):
        """ This method is a wrapper for the execution of `allow` and `deny` commands for a specific `SLPF Actuator implementation`.

            :param args: Contains the `Action` to be executed (allow or deny) and the `rule number` assigned to this rule.
            :type args: list
            :param kwargs: A dictionary of arguments for the execution of the specific implementation of allow or deny command.
            :type kwargs: dict
        """

        try:
        #   Executing allow/deny command for specific implementation
            function = self.execute_allow_command if args[0] == Actions.allow else self.execute_deny_command
            function(**kwargs)
            logger.info(self.tag + " %s action executed successfully", args[0].__repr__().capitalize())
        except Exception as e:
            logger.info(self.tag + " Execution error for %s action: %s", args[0].__repr__().capitalize(), str(e))
            e.arg = { 'command_action': args[0], 'rule_number': args[1]}
            raise e


    def delete(self, cmd):
        """ `Delete` action

            This method implements the `delete` action: 
            validates and manages delete `Target` and `Args`, 
            gets the `command` with a specific `rule number` from the `database` and recontructs it as an `OpenC2 Command`. 
            Finally sets the delete action to be executed at a specific `start time`.

            :param cmd: The `Command` including `Target` and optional `Args`.
            :type cmd: Command
            :return: A `Response` including the result of the delete command and appropriate status code and messages.
        """

        target = cmd.target.getObj()
        args = cmd.args
        rule_number = int(target)

        try:
        #   Validating target
            if type(target) != slpf.RuleID:
                raise TypeError("Invalid target type")    

        #   Validating args
            if ( ('response_requested' in args and type(args['response_requested']) != ResponseType)
                or ('start_time' in args and type(args['start_time']) != DateTime)):
                raise TypeError("Invalid delete argument type")
        
        #   Checking if the requested command is present in the database
            if not self.db.find_command(rule_number):
                raise
            
        #   Calculating start time
            start_time = args['start_time'] / 1000 if 'start_time' in args else time.time()
            start_time = datetime.fromtimestamp(start_time)

        #   Get and reconstruct command from db
            cmd_data = self.db.get_command(rule_number)
            command_to_delete = self.reconstruct_command(cmd_data)

        #   Managing the scheduler 
            job_ids = {'start_job_id': cmd_data['start_job_id'],
                       'stop_job_id': cmd_data['stop_job_id'],
                       'my_id': self.generate_unique_job_id()}             
            self.scheduler.add_job(self.delete_handler,
                                   'date',
                                   next_run_time=start_time,
                                   kwargs={'command_to_delete': command_to_delete, 'rule_number': rule_number, 'job_ids': job_ids},
                                   id=job_ids['my_id'],
                                   misfire_grace_time=self.misfire_grace_time)
            
            return Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK])
        except TypeError as e:
            return Response(status=StatusCode.BADREQUEST, status_text=str(e))
        except Exception as e:
            return Response(status=StatusCode.INTERNALERROR, status_text="Firewall rule not removed or updated")
        

    def delete_handler(self, command_to_delete, rule_number, job_ids):
        """ This method manages the execution of `delete` command.

            Cancels scheduled `jobs` such as the execution of the command that needs to be deleted if `start time` not expired yet
            or the annulment of the command that needs to be deleted if `stop time` is present and not expired yet. 
            Finally executes the `delete` command for a specific `SLPF Actuator implementation` and 
            deletes the command from the `database`.

            This method can be executed by a `delete` command, an `allow` or `deny` command with a certain `stop time` and from `slpf_exit()` method at SLPF Actuator `shutdown`. 

            :param command_to_delete: The command to delete.
            :type command_to_delete: Command
            :param rule_number: Rule number of the command to delete.
            :type rule_number: RuleID
            :param job_ids: Contains information about `apscheduler job ids`: 
                            `start_job_id` is the id of the job responsible to activate, at a certain `start time`, the OpenC2 allow or deny command, 
                            `stop_job_id` is the id of the job responsible to deactivate, at a certain `stop time`, the OpenC2 allow or deny command. 
                            `my_id` is the id of the job that is executing this function.
            :type job_ids: dict
        """

        try:
            if job_ids['stop_job_id']:
                if self.scheduler.get_job(job_ids['stop_job_id']):
                #   Removing stop job if present
                    self.scheduler.remove_job(job_ids['stop_job_id'])
                else:
                #   An allow action has setted a stop time job that is no longer present in the scheduler
                #   and this is a delete action:
                #   the command has been already removed and the delete action terminate
                    if job_ids['my_id'] and job_ids['my_id'] != job_ids['stop_job_id']:
                        return
            if self.scheduler.get_job(job_ids['start_job_id']):
            #   Removing start job if present
            #   If start job still present in the scheduler the command is not set yet in the specific implementation, only in the database
                self.scheduler.remove_job(job_ids['start_job_id'])
            else:
            #   if start job is not present in the scheduler we have to remove the command from the specific implementation
                self.execute_delete_command(command_to_delete)

        #   Deleting command from database
            logger.info(self.tag + " Deleting command from database")
            self.db.delete_command(rule_number)

            logger.info(self.tag + " Delete action executed successfully")
        except Exception as e:
            logger.info(self.tag + " Execution error for delete action: %s", str(e))
            e.arg = { 'command_action': Actions.delete }
            raise e


    def update(self, cmd):
        """ `Update` action

            This method implements the `update` action: 
            validates and manages update `Target` and `Args` and 
            sets the update action to be executed at a specific `start time`.

            :param cmd: The `Command` including `Target` and optional `Args`.
            :type cmd: Command
            :return: A `Response` including the result of the delete command and appropriate status code and messages.
        """
        try:
            target = cmd.target.getObj()
            args = cmd.args

        #   Validating action, target for specific implementation
            self.validate_action_target_args(action=cmd.action,
                                             target=target,
                                             args=None)

        #   Validating target
            if type(target) != File:
                raise TypeError("Invalid target type")
                            
            if not 'name' in target or not target['name']:
                raise ValueError(StatusCode.BADREQUEST, "Target file name must be specified")
            if type(target['name']) != str:
                raise TypeError("Invalid update argument type")
            
            if 'path' in target and type(target['path']) != str: 
                raise TypeError("Invalid update argument type")
            path = target['path'] if 'path' in target else self.update_directory_path
            abs_path = os.path.join(path, target['name'])
            if not os.path.exists(abs_path):
                raise ValueError(StatusCode.INTERNALERROR, "Cannot access file")

            if 'hashes' in target:
                if 'md5' in target['hashes'] and type(target['hashes']['md5']) != Binaryx:
                    raise TypeError("Invalid update argument type")
                if 'sha1' in target['hashes'] and type(target['hashes']['sha1']) != Binaryx:
                    raise TypeError("Invalid update argument type")
                if 'sha256' in target['hashes'] and type(target['hashes']['sha256']) != Binaryx:
                    raise TypeError("Invalid update argument type")
                
#               Checking hashes
                md5_hash = hashlib.md5() if 'md5' in target['hashes'] else None
                sha1_hash = hashlib.sha1() if 'sha1' in target['hashes'] else None
                sha256_hash = hashlib.sha256() if 'sha256' in target['hashes'] else None

                with open(abs_path, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        if md5_hash:
                            md5_hash.update(chunk)
                        if sha1_hash:
                            sha1_hash.update(chunk)
                        if sha256_hash:
                            sha256_hash.update(chunk)

                if md5_hash and Binaryx(md5_hash.hexdigest()).__str__() != target['hashes']['md5'].__str__():
                    raise ValueError(StatusCode.BADREQUEST, "Invalid md5 hash value")
                if sha1_hash and Binaryx(sha1_hash.hexdigest()).__str__() != target['hashes']['sha1'].__str__():
                    raise ValueError(StatusCode.BADREQUEST, "Invalid sha1 hash value")
                if sha256_hash and Binaryx(sha256_hash.hexdigest()).__str__() != target['hashes']['sha256'].__str__():
                    raise ValueError(StatusCode.BADREQUEST, "Invalid sha256 hash value")

        #   Validating args        
            if 'response_requested' in args: 
                if type(args['response_requested']) != ResponseType:
                    raise TypeError("Invalid update argument type")
                if args['response_requested'] == ResponseType.status:
                    raise ValueError(StatusCode.BADREQUEST, "Response requested cannot be set to status")
            if 'start_time' in args and type(args['start_time']) != DateTime:
                raise TypeError("Invalid update argument type")
            

        #   Calculating start time
            start_time = args['start_time'] / 1000 if 'start_time' in args else time.time()
            start_time = datetime.fromtimestamp(start_time)

        #   Managing the scheduler 
            self.scheduler.add_job(self.update_handler,
                                   'date',
                                   next_run_time=start_time,
                                   kwargs={'name': target['name'], 'path': path},
                                   id=self.generate_unique_job_id(),
                                   misfire_grace_time=self.misfire_grace_time)

        #    return Response(status=StatusCode.PROCESSING, status_text=StatusCodeDescription[StatusCode.PROCESSING])
            return Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK])
        except TypeError as e:
            return Response(status=StatusCode.BADREQUEST, status_text=str(e))
        except ValueError as e:
            return Response(status=e.args[0], status_text=e.args[1])
        except Exception as e:
            return Response(status=StatusCode.INTERNALERROR, status_text="File not updated")

        
    def update_handler(self, **kwargs):
        """ This method manages the execution of `update` command.

            Sets `SLPF Actuator` in `FILE mode` (file rules in use) removing all scheduled commands from the scheduler and all rules from the database and 
            executes the `update` command for a specific `SLPF Actuator implementation`

            :param kwargs: A list of arguments for the execution of the specific implementation of update command.
            :type kwargs: dict
        """

        try:
        #   Setting SLPF Actuator in file mode
            self.mode = SLPFActuator.Mode.file
            logger.info(self.tag + " " + self.mode.value + " mode")            
        #   Cleaning scheduler
            self.scheduler.remove_all_jobs()
        #   Cleaning database: SLPF Actuator now in file mode, al rules managed by file
            self.db.clean_db()
        #   Executing update command for specific implementation
            self.execute_update_command(**kwargs)
            logger.info(self.tag + " Update action executed successfully")
        except Exception as e:
            logger.info(self.tag + " Execution error for update action: %s", str(e))
            e.arg = { 'command_action': Actions.update }
            raise e
          

    def slpf_exit(self):
        """ This method handles SLPF Actuator `shutdown`.

            Deletes non persistent commands from the database, 
            saves persistent commands and scheduled jobs if SLPF Actuator in db mode and 
            turns off the scheduler.
        """
        try:
        #   Deleting non persistent commands    
            logger.info(self.tag + " Deleting non persistent commands")        
            non_persistent_commands = self.db.get_non_persistent_comands()           
            for command in non_persistent_commands:
                job_ids = {'start_job_id': command['start_job_id'],
                           'stop_job_id': command['stop_job_id'],
                           'my_id': None }
                self.delete_handler(command_to_delete=self.reconstruct_command(command),
                                    rule_number=command['rule_number'],
                                    job_ids=job_ids)

        #   Saves persistent commands only if SLPF Actuator is in db mode (there are commands in the database)
        #   If SLPF Actuator is in file mode (empty database, rules managed by file) there is no need to save persistent commands
            logger.info(self.tag + " " + self.mode.value + " mode") 
            if self.mode == SLPFActuator.Mode.db:  
            #   Saving persistent commands            
                self.save_persistent_commands()
            #   Saving persistent jobs
                logger.info(self.tag + " Saving persistent scheduled jobs")  
                persistent_jobs = self.scheduler.get_jobs()
                if persistent_jobs:
                    for job in persistent_jobs:
                        self.db.insert_job(id=job.id,
                                          func_name=job.func.__name__,
                                           next_run_time=job.next_run_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
                                           args=job.args,
                                           kwargs=job.kwargs)                
        #   Shutdown scheduler
            threading.Thread(target=self.scheduler.shutdown).start() 
            logger.info(self.tag + " Shutdown")       
        except Exception as e:
            logger.info(self.tag + " Shutdown error: %s", str(e)) 
            raise e


    def scheduler_listener(self, event):
        """ This method handles success or exceptions of scheduled `apscheduler jobs`.

            :param event: An event triggered by the execution of a job (success or exception).
            :type event: apscheduler.events.JobExecutionEvent
        """

        try:
            if event.exception:
                # allow/deny case
                if hasattr(event.exception, 'arg'):
                    command_action = event.exception.arg.get('command_action')
                    if not command_action:
                        raise
                    if command_action == Actions.allow or command_action == Actions.deny:
                        self.db.delete_command(event.exception.arg.get('rule_number'))
                    elif command_action == Actions.delete:
                        pass
                    elif command_action == Actions.update:
                        pass
        except Exception as e:
            raise e


    def restore_persistent_jobs(self):
        """ This method restores scheduled `apscheduler jobs` not executed yet. """

        try:
            persistent_jobs = self.db.get_jobs()
            for job in persistent_jobs:    
                self.scheduler.add_job(getattr(self, job['func_name']),
                                       'date',
                                       next_run_time=datetime.strptime(job['next_run_time'], '%Y-%m-%d %H:%M:%S.%f'),
                                       args=job['args'],
                                       kwargs=job['kwargs'],
                                       id=job['id'],
                                       misfire_grace_time=self.misfire_grace_time)
            self.db.delete_jobs()
        except Exception as e:
            raise e
        

    def generate_unique_job_id(self):
        """ This method generates an unique id for an `apscheduler job` that has to be scheduled.

            :return: The generated `unique id`.
        """

        while True:
            job_id = str(uuid.uuid4())
            if not self.scheduler.get_job(job_id):
                return job_id


    def db_handler(self, action, target, args, job_ids):
        """ This method handles insertion of commands in the database.

            :param action: Command `Action` to be inserted.
            :type action: Actions
            :param target: Command `Target` to be inserted.
            :type target: IPv4Net/IPv6Net/IPv4Connection/IPv6Connection
            :param args: Command `Args` to be inserted.
            :type args: slpf.Args
            :param job_ids: Contains information about `apscheduler job ids`: 
                            `start_job_id` is the id of the job responsible to activate, at a certain `start time`, the OpenC2 allow or deny command, 
                            `stop_job_id` is the id of the job responsible to deactivate, at a certain `stop time`, the OpenC2 allow or deny command. 
            :type job_ids: dict
        """

        try:
            src = None
            src_port = None
            dst = None
            dst_port = None
            prot = None
            if type(target) == IPv4Connection or type(target) == IPv6Connection:
                if target.src_addr:
                    src = target.src_addr.__str__()
                if target.dst_addr:
                    dst = target.dst_addr.__str__()
                if target.protocol:
                    prot = target.protocol.name
                if target.src_port:
                    src_port = target.src_port
                if target.dst_port:
                    dst_port = target.dst_port
            elif type(target) == IPv4Net or type(target) == IPv6Net:
                dst = target.__str__()

            rule_number = self.db.insert_command(insert_rule=args['insert_rule'] if 'insert_rule' in args else None,
                                                action=action.__repr__(),
                                                drop_process=args['drop_process'].name if 'drop_process' in args else None,
                                                direction=args['direction'].name,
                                                target=target.__class__.__name__,
                                                protocol=prot,
                                                src_addr=src,
                                                src_port=src_port,
                                                dst_addr=dst,
                                                dst_port=dst_port,
                                                start_time=datetime.fromtimestamp(args['start_time']).isoformat(sep=' ', timespec='milliseconds'),
                                                stop_time=datetime.fromtimestamp(args['stop_time']).isoformat(sep=' ', timespec='milliseconds') if 'stop_time' in args else None,
                                                persistent=args['persistent'] if 'persistent' in args else True,
                                                start_job_id=job_ids['start_job_id'],
                                                stop_job_id=job_ids['stop_job_id'])
        except Exception as e:
            raise e
        return rule_number
            

    def reconstruct_command(self, cmd_data):
        """ This method reconstruct an `OpenC2 Command` from `database data`.

            :param cmd_data: Database data of a specific command.
            :type cmd_data: dict

            :return: The reconstructed `OpenC2 Command`.
        """

        if cmd_data['action'] == Actions.allow.name:
            action = Actions.allow
        elif cmd_data['action'] == Actions.deny.name:
            action = Actions.deny
        
        drop_process = None
        if cmd_data['drop_process']:
            if cmd_data['drop_process'] == DropProcess.none.name:
                drop_process = DropProcess.none
            elif cmd_data['drop_process'] == DropProcess.reject.name:
                drop_process = DropProcess.reject
            elif cmd_data['drop_process'] == DropProcess.false_ack.name:
                drop_process = DropProcess.false_ack

        if cmd_data['direction'] == slpf.Direction.ingress.name:
            direction = slpf.Direction.ingress
        elif cmd_data['direction'] == slpf.Direction.egress.name:
            direction = slpf.Direction.egress
        elif cmd_data['direction'] == slpf.Direction.both.name:
            direction = slpf.Direction.both

        if cmd_data['target'] == IPv4Net.__name__ or cmd_data['target'] == IPv6Net.__name__:
        #    if direction == slpf.Direction.ingress or direction == slpf.Direction.both:
        #        addr = cmd_data['src_addr']
        #    elif direction == slpf.Direction.egress:
            addr = cmd_data['dst_addr']

        if cmd_data['target'] == IPv4Net.__name__:
            target = IPv4Net(ipv4_net=addr)
        elif cmd_data['target'] == IPv6Net.__name__:
            target = IPv6Net(ipv6_net=addr)
        elif cmd_data['target'] == IPv4Connection.__name__:
            target = IPv4Connection(protocol=cmd_data['protocol'],
                                    src_addr=cmd_data['src_addr'],
                                    src_port=cmd_data['src_port'],
                                    dst_addr=cmd_data['dst_addr'],
                                    dst_port=cmd_data['dst_port'])
        elif cmd_data['target'] == IPv6Connection.__name__:
            target = IPv6Connection(protocol=cmd_data['protocol'],
                                    src_addr=cmd_data['src_addr'],
                                    src_port=cmd_data['src_port'],
                                    dst_addr=cmd_data['dst_addr'],
                                    dst_port=cmd_data['dst_port'])
        
    #   Just needed args
        args = slpf.Args({'direction': direction})
        if drop_process:
            args['drop_process'] = drop_process
        reconstructed_command = Command(action, target, args)

        return reconstructed_command


    def __notimplemented(self, cmd):
        """ Default response

            Default response returned in case an `Action` is not implemented.
            The `cmd` argument is only present for uniformity with the other handlers.
            :param cmd: The `Command` that triggered the error.
            :return: A `Response` with the appropriate error code.

        """
        return Response(status=StatusCode.NOTIMPLEMENTED, status_text='Command not implemented')

    def __servererror(self, cmd, e):
        """ Internal server error

            Default response in case something goes wrong while processing the command.
            :param cmd: The command that triggered the error.
            :param e: The Exception returned.
            :return: A standard INTERNALSERVERERROR response.
        """
        logger.warn("Returning details of internal exception")
        logger.warn("This is only meant for debugging: change the log level for production environments")
        if(logging.root.level < logging.INFO):
            return Response(status=StatusCode.INTERNALERROR, status_text='Internal server error: ' + str(e))
        else:
            return Response(status=StatusCode.INTERNALERROR, status_text='Internal server error')