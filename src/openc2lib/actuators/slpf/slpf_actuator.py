""" Skeleton `Actuator` for SLPF profile

    This module provides an example to create an `Actuator` for the SLPF profile.
    It only answers to the request for available features.
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

from .sql_database import SQLDatabase

from openc2lib import ArrayOf,ActionTargets, TargetEnum, Nsid, Version,Actions, Command, Response, StatusCode, StatusCodeDescription, Features, ResponseType, Feature, IPv4Net, IPv4Connection , IPv6Net, IPv6Connection, DateTime, Duration, Binaryx, L4Protocol, Port
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

# An implementation of the slpf profile. 
class SLPFActuator:
    """ Iptables SLPF implementation

        This class provides an implementation of the SLPF `Actuator` for iptables.
    """

    def __init__(self,hostname, named_group, asset_id, asset_tuple, db_name, db_path, db_commands_table_name, db_jobs_table_name, misfire_grace_time):
        # Needed in development phase
        # otherwise werkzeug development server launches the function twice
        # that is bad for the scheduler
        if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            MY_IDS['hostname'] = hostname
            MY_IDS['named_group'] = named_group
            MY_IDS['asset_id'] = asset_id
            MY_IDS['asset_tuple'] = asset_tuple

            try:
#               Initializing database
                self.db_path = db_path if db_path else os.path.dirname(os.path.abspath(__file__))
                self.db_name = db_name if db_name else "slpf_commands.sqlite"
                if not os.path.exists(self.db_path):
                    raise
                self.db_commands_table_name = db_commands_table_name if db_commands_table_name else "iptables_commands"
                self.db_jobs_table_name = db_jobs_table_name if db_jobs_table_name else "iptables_jobs"         
                self.db = SQLDatabase(os.path.join(self.db_path, self.db_name), self.db_commands_table_name, self.db_jobs_table_name)
#               Restoring persistent commands
                self.restore_persistent_commands()                
#               Initializing scheduler   
                self.misfire_grace_time = misfire_grace_time # 1 day
                self.scheduler = BackgroundScheduler()
                self.scheduler.add_listener(lambda event: self.scheduler_listener(event), EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
                self.restore_persistent_jobs()
                self.scheduler.start()
#               Registering exit function
                atexit.register(self.slpf_exit)
            except Exception as e:
                raise e
            

    def execute_allow_command(self, target, direction):
        pass

    def execute_deny_command(self, target, direction, drop_process):
        pass

    def execute_delete_command(self, command_to_delete):
        pass

    def execute_update_command(self, name, path=None, hashes=None):
        pass

    def save_persistent_commands(self):
        pass

    def restore_persistent_commands(self):
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
        """ Query action

            This method implements the `query` action.
            :param cmd: The `Command` including `Target` and optional `Args`.
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
        try:
            return self.allow_deny_handler(self.execute_allow_command.__name__, cmd)
        except Exception as e:
            return self.__servererror(cmd, e)


    def deny(self, cmd):
        try:
            return self.allow_deny_handler(self.execute_deny_command.__name__, cmd)           
        except Exception as e:
            return self.__servererror(cmd, e)


    # args[0]: the function to be executed (allow/deny)
    # args[1]: rule number assigned to this rule
    def allow_deny_execution_handler(self, *args, **kwargs):
        try:
            function = getattr(self, args[0])
            function(**kwargs)
        #    args[0](**kwargs)
        except Exception as e:
            command_action = Actions.allow if args[0].__name__ == self.execute_allow_command.__name__ else Actions.deny
            e.arg = { 'command_action': command_action,
                    'rule_number': args[1]}
            raise e
        

    def allow_deny_handler(self, function_to_execute, cmd):
        try:
            action = cmd.action
            target = cmd.target.getObj()
            args = cmd.args

        #   Validating args
            if ( ('response_requested' in args and args['response_requested'].__class__ != ResponseType)
                or ('insert_rule' in args and args['insert_rule'].__class__ != slpf.RuleID)
                or ('direction' in args and args['direction'].__class__ != slpf.Direction)
                or ('persistent' in args and args['persistent'].__class__ != bool)
                or ('drop_process' in args and args['drop_process'].__class__ != DropProcess)
                or ('start_time' in args and args['start_time'].__class__ != DateTime)
                or ('stop_time' in args and args['stop_time'].__class__ != DateTime)
                or ('duration' in args and args['duration'].__class__ != Duration)):
                    raise KeyError

            if 'insert_rule' in args:
                if args['response_requested'] != ResponseType.complete:
                        raise KeyError
                if self.db.find_command(args['insert_rule']):
                    raise ValueError(StatusCode.NOTIMPLEMENTED, "Rule number currently in use")

            if ('start_time' in args) and ('stop_time' in args): 
                if 'duration' in args:
                    raise KeyError
                if args['start_time'] > args['stop_time']:
                    raise KeyError
            if'stop_time' in args and (args['stop_time'] < time.time() * 1000):
                raise KeyError  
       
        #   Setting default args values
            if not 'direction' in args:
                args['direction'] = slpf.Direction.both
            if action == Actions.deny and not 'drop_process' in args:
                args['drop_process'] = DropProcess.none

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

        #   Generating job ids
            job_ids = {'start_job_id': self.generate_unique_job_id(self.scheduler)}
            job_ids['stop_job_id'] = self.generate_unique_job_id(self.scheduler) if 'stop_time' in args else None
            job_ids['my_id'] = job_ids['start_job_id']

        #   Inserting commands in db   
            rule_number = self.db_handler(action, target, args, job_ids)

        #   Managing the scheduler    
            temp_args = {'direction': args['direction']}
            if 'drop_process' in args:
                temp_args['drop_process'] = args['drop_process']
            start_time = datetime.fromtimestamp(args['start_time'])            
            self.scheduler.add_job(self.allow_deny_execution_handler,
                                   'date',
                                   next_run_time=start_time,
                                   args=[function_to_execute, rule_number],
                                   kwargs={'target': target, **temp_args},
                                   id=job_ids['my_id'],
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
                                       id=job_ids['my_id'],
                                       misfire_grace_time=self.misfire_grace_time)              
            
            res = slpf.Results(rule_number=slpf.RuleID(rule_number))
            return Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK], results=res)
        except ValueError as e:
            return Response(status=e.args[0], status_text=e.args[1])
        except KeyError as e:
            return Response(status=StatusCode.BADREQUEST, status_text="Invalid allow/deny argument")
        except Exception as e:
            return Response(status=StatusCode.INTERNALERROR, status_text="Rule not updated")


    def delete(self, cmd):
        target = cmd.target.getObj()
        args = cmd.args
        rule_number = int(target)

        try:
        #   Validating args
            if ( ('response_requested' in args and args['response_requested'].__class__ != ResponseType)
                or ('start_time' in args and args['start_time'].__class__ != DateTime)):
                raise KeyError
            
        #   Calculating start time
            start_time = args['start_time'] / 1000 if 'start_time' in args else time.time()
            start_time = datetime.fromtimestamp(start_time)

        #   Get and reconstruct command from db
            cmd_data = self.db.get_command(rule_number)
            command_to_delete = self.reconstruct_command(cmd_data)

        #   Managing the scheduler 
            job_ids = {'start_job_id': cmd_data['start_job_id'],
                       'stop_job_id': cmd_data['stop_job_id'],
                       'my_id': self.generate_unique_job_id(self.scheduler)}             
            self.scheduler.add_job(self.delete_handler,
                                   'date',
                                   next_run_time=start_time,
                                   kwargs={'command_to_delete': command_to_delete, 'rule_number': rule_number, 'job_ids': job_ids},
                                   id=job_ids['my_id'],
                                   misfire_grace_time=self.misfire_grace_time)
            
            return Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK])
        except KeyError as e:
            return Response(status=StatusCode.BADREQUEST, status_text="Invalid delete argument")
        except Exception as e:
            return Response(status=StatusCode.INTERNALERROR, status_text="Firewall rule not removed or updated")
        

    def delete_handler(self, command_to_delete, rule_number, job_ids=None):
        try:
            # In slpf_exit job_ids not passed as an argument
            if job_ids:
                if job_ids['stop_job_id']:
                    if self.scheduler.get_job(job_ids['stop_job_id']):
                        self.scheduler.remove_job(job_ids['stop_job_id'])
                    else:
                        if job_ids['my_id'] and job_ids['my_id'] != job_ids['stop_job_id']:
                            return
                if self.scheduler.get_job(job_ids['start_job_id']):
                    self.scheduler.remove_job(job_ids['start_job_id'])
                else:
                    self.execute_delete_command(command_to_delete)
        
            self.db.delete_command(rule_number)
        except Exception as e:
            e.arg = { 'command_action': Actions.delete }
            raise e


    def update(self, cmd):
        try:
            target = cmd.target.getObj()
            args = cmd.args

        #   Validating args                
            if not 'name' in target or not target['name']:
                raise KeyError
            if target['name'].__class__ != str:
                raise KeyError
            
            abs_path = target['name'] if not 'path' in target else os.path.join(target['path'], target['name'])
            
            if 'path' in target: 
                if target['path'].__class__ != str:
                    raise KeyError
            if not os.path.exists(abs_path):
                raise ValueError(StatusCode.INTERNALERROR, "Cannot access file")

            if 'hashes' in target:
                if 'md5' in target['hashes'] and target['hashes']['md5'].__class__ != Binaryx:
                    raise KeyError
                if 'sha1' in target['hashes'] and target['hashes']['sha1'].__class__ != Binaryx:
                    raise KeyError
                if 'sha256' in target['hashes'] and target['hashes']['sha256'].__class__ != Binaryx:
                    raise KeyError
                
            if 'response_requested' in args: 
                if args['response_requested'].__class__ != ResponseType or args['response_requested'] == ResponseType.status:
                    raise KeyError
            if 'start_time' in args and args['start_time'].__class__ != DateTime:
                raise KeyError

        #   Calculating start time
            start_time = args['start_time'] / 1000 if 'start_time' in args else time.time()
            start_time = datetime.fromtimestamp(start_time)

        #   Managing the scheduler 
            self.scheduler.add_job(self.execute_update_command_wrapper,
                                   'date',
                                   next_run_time=start_time,
                                   kwargs=target,
                                   id=self.generate_unique_job_id(self.scheduler),
                                   misfire_grace_time=self.misfire_grace_time)

        #    return Response(status=StatusCode.PROCESSING, status_text=StatusCodeDescription[StatusCode.PROCESSING])
            return Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK])
        except ValueError as e:
            return Response(status=e.args[0], status_text=e.args[1])
        except KeyError as e:
            return Response(status=StatusCode.BADREQUEST, status_text="Invalid update argument")
        except Exception as e:
            return Response(status=StatusCode.INTERNALERROR, status_text="File not updated")

        
#   To manage update exceptions
    def execute_update_command_wrapper(self, **kwargs):
        try:
            self.execute_update_command(**kwargs)
        except Exception as e:
            e.arg = { 'command_action': Actions.update }
            raise e
          

    def slpf_exit(self):
        try:
#           Deleting non persistent commands            
            non_persistent_commands = self.db.get_non_persistent_comands()           
            for command in non_persistent_commands:
                job_ids = {'start_job_id': command['start_job_id'],
                           'stop_job_id': command['stop_job_id']}
                self.delete_handler(command_to_delete=self.reconstruct_command(command),
                                    rule_number=command['rule_number'],
                                    job_ids=job_ids)

            self.save_persistent_commands()

#           Saving persistent jobs
            persistent_jobs = self.scheduler.get_jobs()
            if persistent_jobs:
                for job in persistent_jobs:
                    self.db.insert_job(id=job.id,
                                       func_name=job.func.__name__,
                                       next_run_time=job.next_run_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
                                       args=job.args,
                                       kwargs=job.kwargs)
#           Shutdown scheduler
            threading.Thread(target=self.scheduler.shutdown).start()       
        except Exception as e:
            print("HEREEEEEE")
            print("------->", str(e))
            raise e


    def scheduler_listener(self, event):
        try:
            if event.exception:
                # allow/deny case
                if hasattr(event.exception, 'arg'):
                    command_action = event.exception.arg.get('command_action')
                    if not command_action:
                        raise
                    if command_action == Actions.allow or command_action == Actions.deny:
                        self.db.delete_command(event.exception.arg.get('rule_number'))
                #        return Response(status=StatusCode.INTERNALERROR, status_text="Rule not updated")

                    elif command_action == Actions.delete:
                #        return Response(status=StatusCode.INTERNALERROR, status_text="Firewall rule not removed or updated")
                        pass
                    elif command_action == Actions.update:
                #        return Response(status=StatusCode.INTERNALERROR, status_text="File not updated")
                        pass
            else:
        #        return Response(status=StatusCode.OK, status_text=StatusCodeDescription[StatusCode.OK])
                pass
        except Exception as e:
            raise e


    def restore_persistent_jobs(self):
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
        

    def generate_unique_job_id(self, scheduler):
        while True:
            job_id = str(uuid.uuid4())
            if not scheduler.get_job(job_id):
                return job_id


    def db_handler(self, action, target, args, job_ids):     
        try:
            src = None
            src_port = None
            dst = None
            dst_port = None
            prot = None
            if isinstance(target, IPv4Connection) or isinstance(target, IPv6Connection):
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
            elif isinstance(target, IPv4Net) or isinstance(target, IPv6Net):
                if args['direction'] == slpf.Direction.ingress or args['direction'] == slpf.Direction.both:
                    src = target.__str__()
                if args['direction'] == slpf.Direction.egress or args['direction'] == slpf.Direction.both:
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
            if direction == slpf.Direction.ingress or direction == slpf.Direction.both:
                addr = cmd_data['src_addr']
            elif direction == slpf.Direction.egress:
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