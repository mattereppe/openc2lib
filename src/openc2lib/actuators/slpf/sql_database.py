import sqlite3
import pickle

class SQLDatabase:

    def __init__(self, db_abs_path, commands_table_name, jobs_table_name):
        try:
            self.db_abs_path = db_abs_path
            self.commands_table_name = commands_table_name
            self.jobs_table_name = jobs_table_name

            conn = sqlite3.connect(self.db_abs_path)
            c = conn.cursor()
            c.execute(f'''CREATE TABLE IF NOT EXISTS {self.commands_table_name} 
                    (rule_number INTEGER PRIMARY KEY,
                    action TEXT,
                    drop_process TEXT,
                    direction TEXT,
                    target TEXT,
                    protocol TEXT,
                    src_addr TEXT,
                    src_port INTEGER,
                    dst_addr TEXT,
                    dst_port INTEGER,
                    start_time TEXT,
                    stop_time TEXT,
                    persistent INTEGER,
                    start_job_id TEXT,
                    stop_job_id TEXT)''')
            
            c.execute(f'''CREATE TABLE IF NOT EXISTS {self.jobs_table_name}
                    (id TEXT PRIMARY KEY,
                    func_name TEXT,
                    next_run_time TEXT,
                    args BLOB,
                    kwargs BLOB)''')
            
            conn.commit()
        except sqlite3.Error as e:
            raise e
        finally:
            conn.close()


    def insert_command(self, insert_rule, action, drop_process, direction, target, persistent, src_addr, dst_addr, start_time, stop_time, start_job_id, stop_job_id, protocol, src_port, dst_port): # protocol=None, src_port=None, dst_port=None
        try:
            conn = sqlite3.connect(self.db_abs_path)
            c = conn.cursor()
            c.execute(f'''INSERT INTO {self.commands_table_name} 
                          (rule_number, action, drop_process, direction, target, protocol, src_addr, src_port, dst_addr, dst_port, start_time, stop_time, persistent, start_job_id, stop_job_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (insert_rule, action, drop_process, direction, target, protocol, src_addr, src_port, dst_addr, dst_port, start_time, stop_time, persistent, start_job_id, stop_job_id))
            rule_number = c.lastrowid
            conn.commit()
            return rule_number
        except sqlite3.Error as e:
            raise e
        finally:
            conn.close()

    def get_command(self, rule_number):
        try:
            conn = sqlite3.connect(self.db_abs_path)
            c = conn.cursor()
            c.execute(f'SELECT * FROM {self.commands_table_name} WHERE rule_number = ?', (rule_number,))
            db_result = c.fetchone()
            return self.recreate_command(db_result)
        except sqlite3.Error as e:
            raise e
        finally:
            conn.close()

    def delete_command(self, rule_number):
        try:
            conn = sqlite3.connect(self.db_abs_path)
            c = conn.cursor()
            c.execute(f'DELETE FROM {self.commands_table_name} WHERE rule_number = ?', (rule_number,))
            conn.commit()
        except sqlite3.Error as e:
            raise e
        finally:
            conn.close()
    
    def find_command(self, rule_number):
        try:
            conn = sqlite3.connect(self.db_abs_path)
            c = conn.cursor()
            c.execute(f'SELECT 1 FROM {self.commands_table_name} WHERE rule_number = ?', (rule_number,))
            found = c.fetchone()
            return found is not None
        except sqlite3.Error as e:
            raise e
        finally:
            conn.close()

    
    def get_non_persistent_comands(self):
        try:
            conn = sqlite3.connect(self.db_abs_path)
            c = conn.cursor()
            c.execute(f'SELECT * FROM {self.commands_table_name} WHERE persistent = 0')
            non_persistent = c.fetchall()
            result = []
            for command in non_persistent:
                result.append(self.recreate_command(command))
            return result
        except sqlite3.Error as e:
            raise e
        finally:
            conn.close()

    def recreate_command(self, command):
        return {
            'rule_number': command[0],
            'action': command[1],
            'drop_process': command[2],
            'direction': command[3],
            'target': command[4],
            'protocol': command[5],
            'src_addr': command[6],
            'src_port': command[7],
            'dst_addr': command[8],
            'dst_port': command[9],
            'start_time': command[10],
            'stop_time': command[11],
            'persistent': command[12],
            'start_job_id': command[13],
            'stop_job_id': command[14]
        }
    
    def insert_job(self, id, func_name, next_run_time, args, kwargs):
        try:
            conn = sqlite3.connect(self.db_abs_path)
            print("---->", conn)
            
            args_blob = pickle.dumps(args)
            kwargs_blob = pickle.dumps(kwargs)

            c = conn.cursor()
            c.execute(f'''INSERT INTO {self.jobs_table_name} 
                          (id, func_name, next_run_time, args, kwargs) VALUES (?, ?, ?, ?, ?)''',
                            (id, func_name, next_run_time, args_blob, kwargs_blob))
            conn.commit()
        except sqlite3.Error as e:
            raise e
        finally:
            conn.close()
    
    def get_jobs(self):
        try:
            conn = sqlite3.connect(self.db_abs_path)
            c = conn.cursor()
            c.execute(f'SELECT * FROM {self.jobs_table_name}')
            jobs = c.fetchall()
            result = []
            for job in jobs:
                result.append(self.recreate_job(job))
            return result
        except sqlite3.Error as e:
            raise e
        finally:
            conn.close()

    def delete_jobs(self):
        try:
            conn = sqlite3.connect(self.db_abs_path)
            c = conn.cursor()
            c.execute(f'DELETE FROM {self.jobs_table_name}')
            conn.commit()
        except sqlite3.Error as e:
            raise e
        finally:
            conn.close()

    def recreate_job(self, job):
        return {
            'id': job[0],
            'func_name': job[1] ,
            'next_run_time': job[2],
            'args': pickle.loads(job[3]),
            'kwargs': pickle.loads(job[4])
        }
            