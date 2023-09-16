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

    def connect(self,
                database_name: str,
                user_name: str,
                password: str):
        """
        Create a connection to the PostgreSQL database.
        """
        path_to_db = f"dbname={database_name} user={user_name} password={password} host=localhost"
        try:
            self.connection = psycopg.connect(path_to_db)
            return f'Successfully connected to database "{database_name}".'
        except psycopg.errors.DatabaseError:
            return f'Error connecting to database "{database_name}".'

    def create_table(self) -> str:
        """
        Create a table.
        """
        with self.connection.cursor() as cursor:
            try:
                cursor.execute("""
                            CREATE TABLE activities (
                            id SERIAL PRIMARY KEY,
                            activity TEXT NOT NULL,
                            type VARCHAR(15) NOT NULL,
                            participants INTEGER NOT NULL,
                            price REAL NOT NULL,
                            link TEXT,
                            key TEXT NOT NULL,
                            accessibility REAL NOT NULL,
                            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                            UNIQUE (key));"""
                               )
            except psycopg.errors.DuplicateTable:
                self.connection.rollback()
                return f"Table has already created."

            self.connection.commit()
            return f"Table has been created."

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
