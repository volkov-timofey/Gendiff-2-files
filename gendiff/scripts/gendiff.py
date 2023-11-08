#!/usr/bin/env python3


from gendiff import parse_args, calc_diff


def main() -> None:
    args = parse_args()
    print(calc_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
