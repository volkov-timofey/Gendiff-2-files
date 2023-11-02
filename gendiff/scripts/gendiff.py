#!/usr/bin/env python3


from gendiff import parse_args, pipeline


def main() -> None:
    args = parse_args()
    print(pipeline(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
