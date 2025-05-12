import sqlite3

class SQLDatabase:
    """
    A simple SQLite database class to manage copied artifacts and process IDs (PIDs).
    """

    def __init__(self, db_name="userdata.db"):
        """
        Initializes the database and ensures required tables exist.

        Args:
            db_name (str): The name of the SQLite database file. Default is 'userdata.db'.
        """
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        """
        Initializes the database by creating necessary tables if they do not exist.
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            
            # Create `files` table
            c.execute('''
                CREATE TABLE IF NOT EXISTS files (
                    uid TEXT,
                    file_path TEXT,
                    file_name TEXT,
                    calculated_hash TEXT,
                    UNIQUE(uid, file_path, file_name)
                )
            ''')

            # Create `pids` table
            c.execute('''
                CREATE TABLE IF NOT EXISTS pids (
                    uid TEXT,
                    pid TEXT UNIQUE,
                    name TEXT NULL
                )
            ''')

            conn.commit()

    def add_file(self, uid, file_path, file_name, calculated_hash):
        """
        Inserts a file record for a given UID, file path, file name, and hash. Throws an error if the file already exists.

        Args:
            uid (str): User identifier.
            file_path (str): The path where the file is stored.
            file_name (str): The name of the file.
            calculated_hash (str): The MD5 hash of the file.
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO files (uid, file_path, file_name, calculated_hash) VALUES (?, ?, ?, ?)", 
                      (uid, file_path, file_name, calculated_hash))
            conn.commit()

    def add_pid(self, uid, pid, name=None):
        """
        Inserts a process ID (PID) for a given UID. Ignores duplicates.

        Args:
            uid (str): User identifier.
            pid (str): Process ID.
            name (str, optional): Name associated with the process. Defaults to None.
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            try:
                c.execute("INSERT INTO pids (uid, pid, name) VALUES (?, ?, ?)", (uid, pid, name))
                conn.commit()
            except sqlite3.IntegrityError:
                pass  # Ignore duplicate entries

    def get_files(self, uid):
        """
        Retrieves all files for a specific UID.

        Args:
            uid (str): User identifier.

        Returns:
            list: A list of tuples containing file_path, file_name, and calculated_hash.
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute("SELECT file_path, file_name, calculated_hash FROM files WHERE uid = ?", (uid,))
            return c.fetchall()

    def get_pids(self, uid):
        """
        Retrieves all PIDs associated with a specific UID.

        Args:
            uid (str): User identifier.

        Returns:
            list: A list of process IDs (as strings).
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute("SELECT GROUP_CONCAT(pid) FROM pids WHERE uid = ?", (uid,))
            result = c.fetchone()
            return result[0].split(',') if result and result[0] else []
    
    def get_pids_and_names(self, uid):
        """
        Retrieves all PIDs associated with a specific UID.

        Args:
            uid (str): User identifier.

        Returns:
            list: A list of process IDs (as strings).
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute("SELECT pid, name FROM pids WHERE uid = ?", (uid,))
            result = c.fetchall()
            # If result contains rows, return a list of tuples with pid and name
            return [(pid, name if name else None) for pid, name in result]

    def get_pid_by_name(self, uid, name):
        """
        Retrieves a PID associated with a specific name and UID.

        Args:
            uid (str): User identifier.
            name (str): Name associated with the process.

        Returns:
            str or None: The process ID if found, otherwise None.
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute("SELECT pid FROM pids WHERE uid = ? AND name = ? LIMIT 1", (uid, name))
            result = c.fetchone()
            return result[0] if result else None

    def delete_file(self, uid, file_path, file_name):
        """
        Deletes a file for a given UID, file path, and file name.

        Args:
            uid (str): User identifier.
            file_path (str): The path where the file is stored.
            file_name (str): The name of the file.
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM files WHERE uid = ? AND file_path = ? AND file_name = ?", 
                      (uid, file_path, file_name))
            conn.commit()

    def delete_pid(self, pid):
        """
        Deletes a PID from the database.

        Args:
            pid (str): The process ID to delete.
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM pids WHERE pid = ?", (pid,))
            conn.commit()

# Example usage
db = SQLDatabase()
