import unittest, os
from dotenv import load_dotenv
from database.activity import Activity
from actions.console_printer import ConsolePrinter
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
        self.activity = Activity({'activity': 'test',
                                  'type': 'test',
                                  'participants': 1,
                                  'price': 1,
                                  'link': 'test',
                                  'key': 'test1',
                                  'accessibility': 1})
        self.printer = ConsolePrinter()

    def test_message_to_user(self):
        self.repository.connect(database_name=database_name,
                                user_name=user_name,
                                password=password)

        self.repository.connection.execute('DROP TABLE IF EXISTS activities;')
        self.repository.create_table()

        new_activity = self.repository.save(self.activity)

        self.printer.message_to_user(new_activity)

    def test_error_response_from_api(self):
        self.printer.error_response_from_api(
            {'error': 'test error'}
        )


if __name__ == '__main__':
    unittest.main()
