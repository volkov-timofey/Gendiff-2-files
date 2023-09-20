from difference_calculator.open_check_file import open_check_file


def is_not_none(dict_: dict, key: str) -> bool:
    """
    key in dict
    """
    return dict_.get(key) is not None


def generate_diff(file1: str, file2: str) -> str:
    """
    Compares two configuration files and shows a difference.
    """

    f1_dict, f2_dict = open_check_file(file1, file2)

    diff_two_files = '{'

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
