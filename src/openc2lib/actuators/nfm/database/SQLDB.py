import sqlite3

class SQLDatabase:
    """
    A simple SQLite database class to manage copied artifacts and process IDs (PIDs).
    """

    def __init__(self, db_name="nfmdata.db"):
        """
        Initializes the database and ensures required tables exist.

        Args:
            db_name (str): The name of the SQLite database file. Default is 'nfmdata.db'.
        """
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        """
        Initializes the database by creating necessary tables if they do not exist.
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()

            # Create `pids` table
            c.execute('''
                CREATE TABLE IF NOT EXISTS pids (
                    uid TEXT,
                    pid TEXT UNIQUE,
                    monitor_id TEXT NULL
                )
            ''')

            conn.commit()

    def add_pid(self, uid, pid, monitor_id=None):
        """
        Inserts a process ID (PID) for a given UID. Ignores duplicates.

        Args:
            uid (str): User identifier.
            pid (str): Process ID.
            monitor_id (str, optional): Monitor ID associated with the process. Defaults to None.
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            try:
                c.execute("INSERT INTO pids (uid, pid, monitor_id) VALUES (?, ?, ?)", (uid, pid, monitor_id))
                conn.commit()
            except sqlite3.IntegrityError:
                pass  # Ignore duplicate entries
            
    def get_pid_by_monitor_id(self, uid, monitor_id):
        """
        Retrieves a PID associated with a specific monitor ID and UID.

        Args:
            uid (str): User identifier.
            monitor_id (str): Monitor ID associated with the process.

        Returns:
            str or None: The process ID if found, otherwise None.
        """
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute("SELECT pid FROM pids WHERE uid = ? AND monitor_id = ? LIMIT 1", (uid, monitor_id))
            result = c.fetchone()
            return result[0] if result else None

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

