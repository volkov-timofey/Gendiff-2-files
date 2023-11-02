import json
import yaml
from os.path import splitext


def open_check_file(f1_path: str, f2_path: str) -> (dict, dict):
    """
    Check and open file .json, .yml, .yaml
    Output -> dictionary
    """

    def inner(path: str) -> dict | None:

        with open(path) as file:
            _, ext = splitext(path)
            if ext not in ('.json', '.yml', '.yaml'):
                return None
            else:
                return json.load(file) \
                    if ext == '.json' \
                    else yaml.safe_load(file)
            # имелся ввиду этот вариант, но обработка пустого файла не проходит
            # либо json ругается
            # return json.load(file) or yaml.safe_load(file) or {}

    dict1 = inner(f1_path) if inner(f1_path) else {}
    dict2 = inner(f2_path) if inner(f2_path) else {}

    return (dict1, dict2)
