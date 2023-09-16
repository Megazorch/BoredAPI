import os
import psycopg
from models.activity import Activity


class ActivityRepository:
    """
    Class to manage database connection and CRUD operations.
    """
    def __init__(self):
        # Initialize the connection as None
        self.connection = None
        self.key = ['id', 'activity', 'type', 'participants', 'price', 'link', 'key', 'accessibility', 'created_at']
        self.value = ['№', 'Activity', 'Type', 'Participants', 'Price', 'Link', 'Key', 'Accessibility', 'Created at']
        self.message = ("{id:<3} {activity:<50} {type:<15} {participants:<12} {price:<6}" +
                        "{link:<55} {key:<10} {accessibility:<15}" +
                        "{created_at:<10}\n").format(**dict(zip(self.key, self.value)))

    @staticmethod
    def get_connection(database_name: str, user_name: str, password: str) -> psycopg.Connection:
        """
        Return a database connection.
        """
        path_to_db = f"dbname={database_name} user={user_name} password={password} host=localhost"
        connection = psycopg.connect(path_to_db)
        return connection

    @staticmethod
    def create_table(connection):
        """
        Create a table.
        """
        with connection.cursor() as cursor:
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
            connection.commit()

    def save(self, activity: Activity):
        """
        Insert an activity into the database.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                                INSERT INTO activities (activity, type, participants, price, link, key, accessibility)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)""", Activity.to_tuple())

                self.connection.commit()
                return print("Activity added to database.")
        except psycopg.errors.DatabaseError:
            return print("Error adding activity to database.")

    def find_all(self):
        """
        Select all activities from the database.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("""
                            SELECT * FROM activities""")
            return cursor.fetchall()
