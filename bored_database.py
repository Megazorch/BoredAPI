import os
import psycopg


class BoredApiDatabase:
    """
    Class to manage database connection and CRUD operations.
    """
    def __init__(self, response_data):
        """
        Create a database connection.
        :param response_data:
        """
        self.response_data = [data for data in response_data.values()]

        self.database_name = os.getenv('DB_NAME')
        self.user_name = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')
        self.connection = psycopg.connect(database=self.database_name, user=self.user_name, password=self.password)

    def create_table(self):
        """
        Create a table.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS activities (
                            id SERIAL PRIMARY KEY,
                            activity TEXT NOT NULL,
                            type VARCHAR(15) NOT NULL,
                            participants INTEGER NOT NULL,
                            price REAL NOT NULL,
                            link TEXT,
                            key TEXT NOT NULL,
                            accessibility REAL NOT NULL,
                            UNIQUE (key))"""
                           )
            self.connection.commit()

    def insert_activity(self, response_data):
        """
        Insert an activity into the database.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                                INSERT INTO activities (activity, type, participants, price, link, key, accessibility)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)""", response_data)

                self.connection.commit()
                return print("Activity added to database.")
        except psycopg.errors.DatabaseError:
            return print("Error adding activity to database.")

    def select_all_activities(self):
        """
        Select all activities from the database.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("""
                            SELECT * FROM activities""")
            return cursor.fetchall()
