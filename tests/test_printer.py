"""
Test class for ConsolePrinter class
"""
import unittest
import os

from dotenv import load_dotenv

from actions.console_printer import ConsolePrinter

from database.activity import Activity
from database.activity_repository import ActivityRepository

# Load environment variables from .env file
load_dotenv()
user_name = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
database_name = os.getenv('DB_NAME_TEST')


class ConsolePrinterTest(unittest.TestCase):
    """
    Class to test ConsolePrinter class
    """
    def setUp(self):
        self.repository = ActivityRepository()
        self.activity = Activity({'activity': 'test2',
                                  'type': 'test2',
                                  'participants': 1,
                                  'price': 1,
                                  'link': 'test2',
                                  'key': 'test3',
                                  'accessibility': 1})
        self.printer = ConsolePrinter()

    def test_message_to_user(self):
        """
        Test message_to_user method
        :return:
        """
        self.repository.connect(database_name=database_name,
                                user_name=user_name,
                                password=password)

        self.repository.connection.execute('DROP TABLE IF EXISTS activities;')
        self.repository.create_table()

        new_activity = self.repository.save(self.activity)

        self.printer.message_to_user(new_activity)

    def test_error_response_from_api(self):
        """
        Test error_response_from_api method
        :return:
        """
        self.printer.error_response_from_api(
            {'error': 'test error'}
        )


if __name__ == '__main__':
    unittest.main()
