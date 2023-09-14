"""
Tests for `bored_api_client` package.
"""
import psycopg

from bored_api.activity_repository import ActivityRepository
from dotenv import load_dotenv
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

    def test_connection_to_database(self):
        """
        Test connection to database
        """
        connection = self.api.get_connection(database_name=database_name,
                              user_name=user_name,
                              password=password)

        with connection as conn:
            self.assertIsInstance(conn, psycopg.Connection)

    def test_create_table(self):
        """
        Test create table
        """
        connection = self.api.get_connection(database_name=database_name,
                                             user_name=user_name,
                                             password=password)

        with connection as conn:
            self.api.create_table(conn)


if __name__ == '__main__':
    unittest.main()
