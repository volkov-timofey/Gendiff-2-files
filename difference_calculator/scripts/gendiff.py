#!/usr/bin/env python3


from difference_calculator import create_parser, engine


def main() -> None:
    parser = create_parser()
    print(engine(parser.first_file, parser.second_file, parser.format))


if __name__ == '__main__':
    main()
