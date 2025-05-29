import sqlite3

class SQLDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_path = 'openc2_commands.db'

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS commands (rule_number INTEGER PRIMARY KEY, command TEXT)''')
        conn.commit()
        conn.close()

    def get_command_from_rule_number(self, rule_number):
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute('SELECT command FROM commands WHERE rule_number = ?', (rule_number,))
            db_result = c.fetchone()
            conn.close()
            return db_result
        except:
            return None

    def delete_command_by_rule_number(self, rule_number):
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute('DELETE FROM commands WHERE rule_number = ?', (rule_number,))
            conn.commit()
            conn.close()
            return 0
        except:
            return -1

    def insert_command(self, iptables_command, rule_number=None):
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            if rule_number is None:
                c.execute('INSERT INTO commands (command) VALUES (?)', (iptables_command,))
            else:
                c.execute('INSERT INTO commands (rule_number, command) VALUES (?, ?)', (rule_number, iptables_command))
            rule_number = c.lastrowid
            conn.commit()
            conn.close()
        except:
            return -1

        return rule_number

    def update_command_by_rule_number(self, rule_number, new_command):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('UPDATE commands SET command = ? WHERE rule_number = ?', (new_command, rule_number))
        conn.commit()
        conn.close()
