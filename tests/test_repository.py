"""
Tests for `bored_api_client` package.
"""
import unittest
import os

import psycopg

from dotenv import load_dotenv

from database.activity import Activity
from database.activity_repository import ActivityRepository


# Load environment variables from .env file
load_dotenv()
user_name = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
database_name = os.getenv('DB_NAME_TEST')


class RepositoryTests(unittest.TestCase):
    """
    Tests for `bored_api_client` package.
    """
    def setUp(self):
        self.repository = ActivityRepository()
        self.repository.connect(database_name=database_name,
                                user_name=user_name,
                                password=password)
        self.activity = Activity({'activity': 'test',
                                  'type': 'test',
                                  'participants': 1,
                                  'price': 1,
                                  'link': 'test',
                                  'key': 'test1',
                                  'accessibility': 1})

    def test_connection_to_database(self):
        """
        Test connection to database
        """
        with self.repository.connection as conn:
            self.assertIsInstance(conn, psycopg.Connection)

    def test_create_table(self):
        """
        Test create table
        """
        with self.repository.connection.cursor() as conn:
            conn.execute("DROP TABLE IF EXISTS activities;")

            self.repository.create_table()

            conn.execute("""
                        SELECT EXISTS (
                        SELECT 1
                        FROM information_schema.tables
                        WHERE table_name = 'activities'
                        );""")
            result = conn.fetchone()[0]

            self.assertEqual(result, True)

    def test_save_activity(self):
        """
        Test save activity
        """
        new_activity = self.repository.save(self.activity)

        self.assertEqual([new_activity.activity, new_activity.activity_type,
                          new_activity.participants, new_activity.price,
                          new_activity.link, new_activity.key,
                          new_activity.accessibility],
                         ['test', 'test', 1, 1, 'test', 'test1', 1])

        self.repository.clear_table()

    def test_find_all(self):
        """
        Test find all activities
        """
        self.repository.save(self.activity)

        all_activities = self.repository.find_all()

        activity = all_activities[0]

        self.assertEqual([activity.activity, activity.activity_type,
                          activity.participants, activity.price,
                          activity.link, activity.key,
                          activity.accessibility],
                         ['test', 'test', 1, 1, 'test', 'test1', 1])

        self.repository.clear_table()

    def test_five_last_five(self):
        """
        Test find five latest activities
        """
        self.repository.save(self.activity)

        all_activities = self.repository.find_last_five()
        activity = all_activities[0]

        self.assertEqual([activity.activity, activity.activity_type,
                          activity.participants, activity.price,
                          activity.link, activity.key,
                          activity.accessibility],
                         ['test', 'test', 1, 1, 'test', 'test1', 1])

        self.repository.clear_table()


if __name__ == '__main__':
    unittest.main()
