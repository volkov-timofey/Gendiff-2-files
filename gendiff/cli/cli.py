import argparse


def parse_args() -> object:
    """
    Parser arguments
    """
    args = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    args.add_argument('first_file', type=str)
    args.add_argument('second_file', type=str)
    args.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish',
        type=str
    )

    return args.parse_args()
