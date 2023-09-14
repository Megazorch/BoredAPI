"""
Main file that connects to Bored API and returns a list of 5 activities and save them to PostgreSQL database.
"""
from bored_api.activity_repository import ActivityRepository
from bored_api.bored_api_client import BoredApiClient
from bored_api.bored_arg_parse import create_parser
from models.activity import Activity
from models.parammeters import GetActivityParams

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def main():
    """
    Main function.
    """
    # Create a parser object
    parser = create_parser()

    # Get Namespace object from parser
    arguments = parser.parse_args()

    # Convert Namespace object to dictionary and store in object
    params = GetActivityParams(**vars(arguments))
    print(params.activity_type,  params.participants)

    # Create an instance of the ActivityRepository class
    database = ActivityRepository

    # Get connection to database
    database.get_connection(database_name=database_name,
                            user_name=user_name,
                            password=password)
"""
    if params.action == 'new':

        # Create an instance of the BoredApiManager class
        client = BoredApiClient()

        # Get an activity
        activity = client.get_activity(params.to_dict())

        # Store activity in Activity class
        activity_obj = Activity(**activity)

        # Add activity to database
        database.insert_activity()

    elif args['action'] == 'list':

        # List all activities from database
        database.list_activities()
"""

if __name__ == "__main__":
    # Get environment variables from .env file
    user_name = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    database_name = os.getenv('DB_NAME')

    main()
