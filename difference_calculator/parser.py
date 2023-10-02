import argparse


from difference_calculator import FORMATTER


def create_parser() -> object:
    """
    Parser arguments
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default=FORMATTER
    )

    return parser.parse_args()
