import os
import psycopg
from models.activity import Activity
from prettytable import PrettyTable


class ActivityRepository:
    """
    Class to manage database connection and CRUD operations.
    """
    def __init__(self):
        # Initialize the connection as None
        self.connection = None
        self.console_table = PrettyTable()
        self.console_table.field_names = ['№', 'Activity', 'Type', 'Participants', 'Price', 'Link', 'Key',
                                          'Accessibility', 'Created at']

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
                # Execute the SQL query to check if the table exists
                cursor.execute(
                    f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'activities')")

                # Fetch the result
                table_exists = cursor.fetchone()[0]

                if table_exists is True:
                    cursor.execute("""
                                    INSERT INTO activities (activity, type, participants, price, link, key, accessibility)
                                    VALUES (%(activity)s,
                                            %(type)s,
                                            %(participants)s,
                                            %(price)s,
                                            %(link)s,
                                            %(key)s,
                                            %(accessibility)s);
                                            """, activity.dict())

                    # print(f"Activity added to database.")
                    cursor.execute("SELECT * FROM activities ORDER BY created_at DESC LIMIT 1;")
                    new_activity = cursor.fetchall()
                    self.connection.commit()

                    # Print the result
                    self.message_to_user(new_activity)
                    return f"Activity added to database."
                else:
                    self.create_table()
                    self.save(activity)     # recursive call to save the activity
                    # print(f"Activity added to database.")
                    return f"Activity added to database."
        except psycopg.errors.DatabaseError:
            self.connection.rollback()
            print(f"Error adding activity to database.")
            return f"Error adding activity to database."

    def message_to_user(self, cursor_data: tuple) -> None:
        """
        Return the message to the user.
        """
        for row in cursor_data:
            row = list(row)
            # row[-1] is the created_at column
            row[-1] = row[-1].strftime('%Y-%m-%d %H:%M:%S')
            self.console_table.add_row(row)

        return print(self.console_table)

    def find_all(self):
        """
        Select all activities from the database.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("""
                            SELECT * FROM activities;""")
            all_activities = cursor.fetchall()

            return self.message_to_user(all_activities)

    def find_last_five(self):
        """
        Select last five activities from the database.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("""
                            SELECT * FROM activities ORDER BY created_at DESC LIMIT 5;""")
            last_five_activities = cursor.fetchall()

            return self.message_to_user(last_five_activities)
