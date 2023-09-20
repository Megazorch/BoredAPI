"""
Code to parse arguments
"""
import argparse


def create_parser():
    """
    Get argument if exists and returns them.
    """
    def check_value(value: str) -> float:
        """
        Check if value is a positive integer.
        """
        try:
            value = float(value)
            if value < 0:
                raise argparse.ArgumentTypeError(f"{value} is not a positive number")
            elif value > 1:
                raise argparse.ArgumentTypeError(f"{value} is not a number between 0 and 1")
        except ValueError or TypeError as exc:
            raise argparse.ArgumentTypeError(f"'{value}' is not a number")
        return value

    parser = argparse.ArgumentParser(
                        prog='Wrapper for Bored API',
                        description='Gets a random activity from Bored API or finds one by parameter.',  # pylint:  disable=line-too-long
                        usage='main.py',
                        epilog='For more information contact me by email: megazorch@gmail.com')

    subparsers = parser.add_subparsers(dest='action',
                                       help='Choose "new" to get a new activity or "list" to list saved activities.')

    # Subparser for the 'new' command with optional arguments
    new_parser = subparsers.add_parser('new', help='Get a new activity from the Bored API')
    new_parser.add_argument('--type',
                            help='Specify the type of activity (e.g., education, recreational, social)',
                            type=str,
                            choices=["education", "recreational", "social", "diy", "charity",
                                     "cooking", "relaxation", "music", "busywork"],
                            dest='activity_type',
                            default=None)

    new_parser.add_argument('--participants',
                            type=int,
                            choices=range(0, 6),
                            metavar='[0, n]',
                            help='The number of people that this activity could involve',
                            default=None)

    new_parser.add_argument('--price',
                            type=check_value,
                            help='A factor describing the cost of the event with zero being free',
                            metavar='[0.0, 1.0]',
                            default=None)

    new_parser.add_argument('--price_min',
                            type=check_value,
                            help='A factor describing the minimal cost of the event (goes with --price_max)',
                            metavar='[0.0, 1.0]',
                            dest='minprice',
                            default=None)

    new_parser.add_argument('--price_max',
                            type=check_value,
                            help='A factor describing the maximum cost of the event (goes with --price_min)',
                            metavar='[0.0, 1.0]',
                            dest='maxprice',
                            default=None)

    new_parser.add_argument('--accessibility',
                            type=check_value,
                            help='A factor describing how possible an event is to do with zero being the most accessible',
                            metavar='[0.0, 1.0]',
                            default=None)

    new_parser.add_argument('--accessibility_min',
                            type=check_value,
                            help='A factor describing minimum accessibility of an event (goes with --accessibility_max)',
                            metavar='[0.0, 1.0]',
                            dest='minaccessibility',
                            default=None)

    new_parser.add_argument('--accessibility_max',
                            type=check_value,
                            help='A factor describing maximum accessibility of an event (goes with --accessibility_min)',
                            metavar='[0.0, 1.0]',
                            dest='maxaccessibility',
                            default=None)

    # Subparser for the 'list' command with optional arguments
    subparsers.add_parser('list', help='List 5 last saved activities')
    new_parser.add_argument('-v', '--verbose',
                            action='store_true',
                            help='Enable verbose mode')

    # Subparser for the 'list' command
    list_parser = subparsers.add_parser('list', help='List 5 last saved activities')

    list_parser.add_argument('-v', '--verbose',
                             action='store_true',
                             help='Enable verbose mode')


    logger.info('Parser created')
    create_table_parser.add_argument('-v', '--verbose',
                                     action='store_true',
                                     help='Enable verbose mode')

    return parser
