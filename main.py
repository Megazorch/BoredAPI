"""
Main file that connects to Bored API and returns a list of 5 activities and save them to PostgreSQL database.
"""
import os
import logging
from dotenv import load_dotenv

from actions.console_printer import ConsolePrinter
from bored_api.bored_arg_parse import create_parser
from bored_api.parammeters import GetActivityParams
from bored_api.bored_api_client import BoredApiClient
from database.activity_repository import ActivityRepository
from actions.actions import NewAction, ListAction

# Load environment variables
load_dotenv()


def main():
    """
    Main function.
    """
    logger.info('Started')

    # Create a parser object
    parser = create_parser()

    # Get Namespace object from parser
    arguments = parser.parse_args()

    # Convert Namespace object to dictionary and store in object
    params = GetActivityParams(**vars(arguments))

    # Create an instance of the ActivityRepository class
    database = ActivityRepository()

    # Get connection to database
    database.connect(database_name=database_name,
                     user_name=user_name,
                     password=password)

    if params.action == 'new':

        # Create an instance of the BoredApiClient class
        client = BoredApiClient()

        # Get an activity
        activity = client.get_activity(params.to_dict())
        print(activity)
        # Store activity in Activity class
        activity = Activity(activity)

        # Add activity to database
        new_activity = database.save(activity)

        # Print message to the console
        console_printer.message_to_user(new_activity)

        # Finish logging
        logging.info('Finished')

    elif params.action == 'list':

        # List last 5 activities from database
        last_five_activities = database.find_last_five()

        # Print last 5 activities from database to the console
        console_printer.message_to_user(last_five_activities)

        # Finish logging
        logging.info('Finished')


if __name__ == "__main__":
    # Get environment variables from .env file
    user_name = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    database_name = os.getenv('DB_NAME')

    # Create an instance of the ConsolePrinter class
    console_printer = ConsolePrinter()

    # Create a logger
    logger = logging.getLogger('bored_api')
    logger.setLevel(logging.CRITICAL)

    # Create a console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter(fmt='%(asctime)s: %(levelname)s - %(message)s',
                                  datefmt='%d-%b-%y %H:%M:%S')
    ch.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(ch)

    # Start main function
    main()
