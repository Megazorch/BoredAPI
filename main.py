"""
Main file that connects to Bored API and returns a list of 5 activities and save them to PostgreSQL database.
"""
import os
import logging

from dotenv import load_dotenv

from actions.console_printer import ConsolePrinter
from actions.main_actions import NewAction, ListAction

from actions.bored_arg_parse import create_parser
from bored_api.parammeters import GetActivityParams
from bored_api.bored_api_client import BoredApiClient

from database.activity_repository import ActivityRepository


# Load environment variables
load_dotenv()


# Configure logging
def configure_logging(verbose):
    """
    Configure logging.

    :param verbose:
    :return:
    """
    # Create a logger
    logger = logging.getLogger('bored_api')
    logger.setLevel(logging.DEBUG if verbose else logging.ERROR)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter(fmt='%(asctime)s: %(levelname)s - %(message)s',
                                  datefmt='%d-%b-%y %H:%M:%S')
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)


def main():
    """
    Main function.
    """
    # Create a parser object
    parser = create_parser()

    # Get Namespace object from parser
    arguments = parser.parse_args()

    # Configure logging based on --verbose option
    configure_logging(arguments.verbose)

    logger = logging.getLogger("bored_api")

    logger.info('Started')

    # Convert Namespace object to dictionary and store in object
    params = GetActivityParams(**vars(arguments))

    # Create an instance of the ActivityRepository class
    database = ActivityRepository()

    # Get connection to database
    database.connect(database_name=database_name,
                     user_name=user_name,
                     password=password,
                     host=host,
                     port=port
                     )

    if params.action == 'new':

        # Create an instance of the BoredApiClient class
        client = BoredApiClient()

        # Create an instance of the NewAction class
        action = NewAction(client=client,
                           repository=database,
                           printer=console_printer)

        # Call the NewAction class
        action(params)

    elif params.action == 'list':

        # Create an instance of the ListAction class
        action = ListAction(repository=database,
                            printer=console_printer)

        # Call the ListAction class
        action(params)

    elif params.action == 'create-table':

        database.create_table()

        logger.info('Finished')


if __name__ == "__main__":
    # Get environment variables from .env file
    user_name = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    database_name = os.getenv('DB_NAME')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    # Create an instance of the ConsolePrinter class
    console_printer = ConsolePrinter()

    # Start main function
    main()
