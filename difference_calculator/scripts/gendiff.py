#!/usr/bin/env python3

import argparse
import json


def create_parser() -> object:
    """
    Parser arguments
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


def is_not_none(dict_: dict, key: str) -> bool:
    """
    key in dict
    """
    return dict_.get(key) is not None


def generate_diff(file1: str, file2: str) -> str:
    """
    Compares two configuration files and shows a difference.
    """

    diff_two_files = '{'

    f1_dict = json.load(open(file1))
    f2_dict = json.load(open(file2))

    intersection_items = dict(f1_dict.items() & f2_dict.items())
    f1_diff = dict(f1_dict.items() ^ intersection_items.items())
    f2_diff = dict(f2_dict.items() ^ intersection_items.items())

    sort_all_keys = sorted(f1_dict.keys() | f2_dict.keys())

    for key in sort_all_keys:

        # if have itersection key
        if is_not_none(intersection_items, key):
            diff_two_files += f'\n\t  {key}: {intersection_items[key]}'

        # if the key is in both config files and values different
        elif (
            is_not_none(f1_diff, key)
            ) & (
            is_not_none(f2_diff, key)
        ):

            diff_two_files += (
                f'\n\t- {key}: {f1_diff[key]}\n\t+ {key}: {f2_diff[key]}'
            )

        # if the key is in one of the config files
        else:
            diff_two_files += f'\n\t- {key}: {f1_diff[key]}' if (
                is_not_none(f1_diff, key)
            ) else f'\n\t+ {key}: {f2_diff[key]}'

    diff_two_files += '\n}'

    return diff_two_files


def main() -> None:
    parser = create_parser()
    print(generate_diff(parser.first_file, parser.second_file))


if __name__ == '__main__':
    main()
