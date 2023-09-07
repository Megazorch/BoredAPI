"""
Main file that connects to Bored API and returns a list of 5 activities and save them to PostgreSQL database.
"""
import bored_functions
import bored_arg_parse


def main():
    """
    Main function.
    """
    arguments = bored_arg_parse.create_parser()
    if arguments is not None:
        bored_functions.get_activity(arguments)
    # else:
        # activate_console()


if __name__ == "__main__":
    main()
