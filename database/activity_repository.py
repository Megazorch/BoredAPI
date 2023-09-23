"""
Repository that save and retrieve data from PostgreSQL database.
"""
import logging
import psycopg
from database.activity import Activity

logger = logging.getLogger("bored_api")


class ActivityRepository:
    """
    Class to manage database connection and CRUD operations.
    """
    def __init__(self):
        # Initialize the connection as None
        self.connection = None

        logger.info('Initialized ActivityRepository')

    def connect(self,
                database_name: str,
                user_name: str,
                password: str,
                host: str = 'localhost',
                port: str = '5432'
                ):
        """
        Create a connection to the PostgreSQL database.
        """
        path_to_db = f"dbname={database_name} user={user_name} password={password} host={host} port={port}"
        try:
            self.connection = psycopg.connect(path_to_db)
            logger.info(f'Successfully connected to database "{database_name}".')
        except psycopg.errors.DatabaseError:
            logger.error(f'Did not managed to connect to database "{database_name}".')

    def create_table(self) -> None:
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
                self.connection.commit()
                logger.info("The table 'activities' - created.")
                print("The table 'activities' is successfully created.")

            except psycopg.errors.DuplicateTable:
                self.connection.rollback()
                logger.warning("The table 'activities' already exists.")
                print("The table 'activities' already exists.")

    def save(self, activity: Activity) -> Activity:
        """
        Insert an activity into the database.
        """

        try:
            with self.connection.cursor() as cursor:

                cursor.execute("""
                                INSERT INTO activities (activity, type, participants,
                                                        price, link, key, accessibility)
                                VALUES (%(activity)s,
                                        %(type)s,
                                        %(participants)s,
                                        %(price)s,
                                        %(link)s,
                                        %(key)s,
                                        %(accessibility)s)
                                RETURNING id, created_at;
                                        """, {'activity': activity.activity,
                                              'type': activity.activity_type,
                                              'participants': activity.participants,
                                              'price': activity.price,
                                              'link': activity.link,
                                              'key': activity.key,
                                              'accessibility': activity.accessibility})

                id_and_created_at = cursor.fetchone()

                self.connection.commit()
                logger.info(f"Activity: {activity.activity} - inserted.\nReturn value: {id_and_created_at}")

                updated_activity = Activity({'id': id_and_created_at[0],
                                             'activity': activity.activity,
                                             'type': activity.activity_type,
                                             'participants': activity.participants,
                                             'price': activity.price,
                                             'link': activity.link,
                                             'key': activity.key,
                                             'accessibility': activity.accessibility,
                                             'created_at': id_and_created_at[1]})

                return updated_activity

        except psycopg.errors.UniqueViolation:
            self.connection.rollback()

            logger.warning(f"Activity: {activity.activity} - already exists.")

            existing_activity = self.find_by_key(key=activity.key)

            return existing_activity

    def find_all(self) -> list[Activity]:
        """
        Select all activities from the database.
        """
        cur = self.connection.execute("SELECT * FROM activities;")

        all_activities = cur.fetchall()
        list_of_all_activities = []

        for row in all_activities:
            activity = Activity({'id': row[0], 'activity': row[1], 'type': row[2],
                                 'participants': row[3], 'price': row[4], 'link': row[5],
                                 'key': row[6], 'accessibility': row[7], 'created_at': row[8]})
            list_of_all_activities.append(activity)

        return list_of_all_activities

    def find_last_five(self) -> list[Activity]:
        """
        Select last five activities from the database.
        """
        cur = self.connection.execute("SELECT * FROM activities ORDER BY created_at DESC LIMIT 5;")

        last_five_activities = cur.fetchall()
        list_of_last_five_activities = []

        for row in last_five_activities:
            logger.debug(f"Last five activities: {row[1]}\n{row[2]}\n{row[3]}\n{row[4]}\n{row[5]}\n{row[6]}\n{row[7]}")
            new_activity = Activity({'id': row[0], 'activity': row[1], 'type': row[2],
                                     'participants': row[3], 'price': row[4], 'link': row[5],
                                     'key': row[6], 'accessibility': row[7], 'created_at': row[8]})
            list_of_last_five_activities.append(new_activity)

        return list_of_last_five_activities

    def find_by_key(self, key: str) -> list[tuple]:
        """
        Select activity by key from the database.
        """
        cur = self.connection.execute("SELECT * FROM activities WHERE key = %(key)s;", {'key': key})

        activity = cur.fetchall()

        return activity

    def clear_table(self) -> None:
        """
        Delete all activities from the database.
        """
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM activities;")
            self.connection.commit()

            logger.info("The table 'activities' - cleared.")
            print("The table 'activities' is successfully cleared.")
