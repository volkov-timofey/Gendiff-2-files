from functools import reduce
from gendiff.cli.file_conversion import convert_files
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def extract_value(key, node1, node2):
    """
    Extract value from 2 dictionary
    """
    intersection_keys = node1.keys() & node2.keys()

    if key in intersection_keys:

        value1 = node1[key]
        value2 = node2[key]

        if value1 == value2:
            return {key: {'action': 'unchange', 'value': value1}}

        # if values is dict -> recursion
        if (isinstance(value1, dict) and isinstance(value2, dict)):
            return {key: create_diff_dict(value1, value2)}

        else:
            return {
                key: {
                    'action': 'change',
                    'old_value': value1,
                    'new_value': value2
                }
            }

    if key in node1:
        return {key: {'action': 'del', 'value': node1[key]}}
    
    else:
        return {key: {'action': 'add', 'value': node2[key]}}


def create_diff_dict(node1, node2):
    """
    Create difference dictionary
    """

    sort_all_keys = sorted(node1.keys() | node2.keys())

    result = reduce(
        lambda x, y: x | y,
        map(lambda key: extract_value(key, node1, node2), sort_all_keys),
        {}
    )

    return result


def generate_diff(dict1: dict, dict2: dict, format_name='stylish') -> dict:
    """
    Calculates the difference between files
    result - > dict
    {
    key: ['flag_action', *value]
    }

    flag_action:
    add, unchange, change, del
    """

    styles = {
        'plain': get_plain,
        'json': get_json,
        'stylish': get_stylish
    }

    formatter = styles[format_name]

    # was realise in individual modul
    # but for test need realise here
    '''
    dict1, dict2 = open_check_file(dict1, dict2) \
        if isinstance(dict1, str) and isinstance(dict2, str) \
        else (dict1, dict2)
    '''
    return formatter(create_diff_dict(dict1, dict2))


def calc_diff(file1: str, file2: str, format_name: str) -> str:
    """
    Module for open files,
    calculating the difference
    and formatter result
    """

    file1_dict, file2_dict = convert_files(file1, file2)
    diff_str = generate_diff(file1_dict, file2_dict, format_name)

    return diff_str