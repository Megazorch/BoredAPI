"""
Code to parse arguments
"""
import argparse


def create_parser():
    """
    Get argument if exists and returns them.
    """
    # my_program new --type education --participants 1 --price_min 0.1 --price_max 30 --accessibility_min 0.1 --accessibility_max 0.5
    def check_positive(value):
        """
        Check if value is a positive integer.
        :param value:
        :return:
        """
        try:
            value = int(value)
            if value <= 0:
                raise argparse.ArgumentTypeError("{} is not a positive integer".format(value))
        except ValueError:
            raise Exception("{} is not an integer".format(value))
        return value

    parser = argparse.ArgumentParser(
                        prog='Wrapper for Bored API',
                        description='Gets a random activity from Bored API or finds one by parameter. ',
                        usage='bored_main.py [options]',
                        epilog='For more information contact me by email: megazorch@gmail.com')

    parser.add_argument('new',
                        help='Get a new activity and add it to the database',
                        nargs='?',
                        default=None)

    parser.add_argument('--type',
                        help='Activity type',
                        type=str,
                        choices=["education", "recreational", "social", "diy", "charity",
                                 "cooking", "relaxation", "music", "busywork"],
                        default=None)

    parser.add_argument('--participants',
                        type=check_positive,
                        help='Number of participants',
                        default=None)

    parser.add_argument('--price',
                        type=float,
                        help='Price of the activity',
                        #choices=range(0, 2),
                        default=None)

    parser.add_argument('--price_min',
                        type=float,
                        help='Minimal price of the activity',
                        #choices=range(0, 2),
                        default=None)

    parser.add_argument('--price_max',
                        type=float,
                        help='Maximal price of the activity',
                        #choices=range(0, 2),
                        default=None)

    parser.add_argument('--accessibility',
                        type=float,
                        help='Accessibility of the activity',
                        #choices=range(0, 2),
                        default=None)

    parser.add_argument('--accessibility_min',
                        type=float,
                        help='Minimal accessibility of the activity',
                        #choices=range(0, 2),
                        default=None)

    parser.add_argument('--accessibility_max',
                        type=float,
                        help='Maximal accessibility of the activity',
                        #choices=range(0, 2),
                        default=None)

    return parser
