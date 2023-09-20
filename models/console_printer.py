"""
Console output:
"""
import logging
from prettytable import PrettyTable


class ConsolePrinter:
    """
    Class to print messages to the console
    """
    def __init__(self):
        self.console_table = PrettyTable()
        self.console_table.field_names = ['№', 'Activity', 'Type', 'Participants', 'Price', 'Link', 'Key',
                                          'Accessibility', 'Created at']

        logging.info('Console printer initialized.')

    def message_to_user(self, cursor_data: list[tuple]) -> None:
        """
        Return the message to the user.
        """
        for row in cursor_data:
            row = list(row)
            row[-1] = row[-1].strftime('%Y-%m-%d %H:%M:%S')     # row[-1] is the created_at column
            self.console_table.add_row(row)

        logging.info('Message to user printed.')
        print(self.console_table)