import mysql.connector

class DBConnection:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "Jash@2512"
        self.database = "sisdb"
        self.conn = None
        self.cursor = None

    def get_connection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        self.get_connection()
        self.cursor.execute(query, params or ())
        self.conn.commit()
        self.disconnect()

    def fetch_results(self, query, params=None):
        self.get_connection()
        self.cursor.execute(query, params or ())
        results = self.cursor.fetchall()
        self.disconnect()
        return results
