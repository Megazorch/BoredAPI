"""
Tests for `bored_api_client` package.
"""
from bored_api.activity_repository import ActivityRepository
from models.activity import Activity
from dotenv import load_dotenv
import psycopg
import unittest
import os

# Load environment variables from .env file
load_dotenv()
user_name = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
database_name = os.getenv('DB_NAME_TEST')


class BoredApiClientTests(unittest.TestCase):
    """
    Tests for `bored_api_client` package.
    """
    def setUp(self):
        self.api = ActivityRepository()
        self.api.connect(database_name=database_name,
                         user_name=user_name,
                         password=password)

    def test_connection_to_database(self):
        """
        Test connection to database
        """
        with self.api.connection as conn:
            self.assertIsInstance(conn, psycopg.Connection)

    def test_create_table(self):
        """
        Test create table
        """
        try:
            self.assertEqual(self.api.create_table(),
                             f"Table has been created.")
        except Exception:
            self.assertEqual(self.api.create_table(),
                             f"Table has already created.")

    def test_save_activity(self):
        """
        Test save activity
        """
        activity = Activity({'activity': 'test',
                             'type': 'test',
                             'participants': 1,
                             'price': 1,
                             'link': 'test',
                             'key': 'test1',
                             'accessibility': 1})

        self.assertEqual(self.api.save(activity), f"Activity added to database.")

    def test_find_all(self):
        """
        Test find all activities
        """
        for record in self.api.find_all():
            self.assertIsInstance(record, tuple)

    def test_five_last(self):
        """
        Test find five latest activities
        """
        print(self.api.find_last_five())


if __name__ == '__main__':
    unittest.main()
