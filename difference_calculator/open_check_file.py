import json
import yaml


def open_check_file(file1: str, file2: str) -> (dict, dict):
    """
    Check and open file .json, .yml, .yaml
    Output -> dictionary
    """

    suffix = ('.json', '.yml', '.yaml')
    if file1.endswith(suffix) and file2.endswith(suffix):
        f1_dict = json.load(open(file1)) \
            if file1.endswith('.json') \
            else yaml.safe_load(open(file1)) \
            if yaml.safe_load(open(file1)) \
            else {}
        f2_dict = json.load(open(file2)) \
            if file2.endswith('.json') \
            else yaml.safe_load(open(file2)) \
            if yaml.safe_load(open(file2)) \
            else {}
    else:
        print('Please check files .json or .yaml, .yml')
        open_check_file(file1, file2)

    return (f1_dict, f2_dict)
