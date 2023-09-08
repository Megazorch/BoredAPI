"""
Main file that connects to Bored API and returns a list of 5 activities and save them to PostgreSQL database.
"""
from bored_functions import BoredApiManager
import bored_arg_parse


def main():
    """
    Main function.
    """
    # Get Namespace object from parser
    arguments = bored_arg_parse.create_parser().parse_args()

    # Dictionary representation of arguments
    args = vars(arguments)
    print(args)

    # Create an instance of the BoredApiManager class with the specified activity_type
    manager = BoredApiManager(args)

    # Get an activity
    activity = manager.get_activity()

    # Print the activity JSON to the console
    print(activity)


if __name__ == "__main__":
    main()
