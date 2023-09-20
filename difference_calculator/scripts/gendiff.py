#!/usr/bin/env python3


from difference_calculator.parser import create_parser
from difference_calculator.generate_diff import generate_diff


def main() -> None:
    parser = create_parser()
    print(generate_diff(parser.first_file, parser.second_file))


if __name__ == '__main__':
    main()
