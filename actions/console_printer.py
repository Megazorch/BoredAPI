"""
Console output:
"""
import logging
from prettytable import PrettyTable

from database.activity import Activity

logger = logging.getLogger("bored_api")


class ConsolePrinter:
    """
    Class to print messages to the console
    """
    def __init__(self):
        self.console_table = PrettyTable()
        self.console_table.field_names = ['№', 'Activity', 'Type', 'Participants', 'Price', 'Link', 'Key',
                                          'Accessibility', 'Created at']

        logger.info('Console printer initialized.')

    def message_to_user(self, cursor_data: Activity | list[Activity]) -> None:
        """
        Return the message to the user.
        """
        if isinstance(cursor_data, Activity):
            self.console_table.add_row(cursor_data.to_list())
            logger.info('Message to user printed.')
            print(self.console_table)
        else:
            for activity in cursor_data:
                row_as_list = activity.to_list()
                row_as_list[-1] = row_as_list[-1].strftime('%Y-%m-%d %H:%M:%S')     # row[-1] is the created_at column
                self.console_table.add_row(row_as_list)
            logger.info('Message to user printed.')
            print(self.console_table)

    @staticmethod
    def error_response_from_api(error_message: dict) -> None:
        """
        Return the error message from the API.
        """
        logger.error(error_message['error'])
        print(error_message['error'])
