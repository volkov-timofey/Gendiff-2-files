import json
import yaml
from os.path import splitext


def read_file(file_path: str) -> (str, str):
    """
    Read file to str
    """
    with open(file_path) as file:
        _, ext = splitext(file_path)
        return (ext, file.read())


def load_file_to_dict(file_path: str) -> dict:
    """
    Check file .json, .yml, .yaml
    Output -> dictionary
    """
    ext, file = read_file(file_path)

    if ext == '.json':
        return json.loads(file)

    elif ext in ('.yml', '.yaml'):
        return yaml.safe_load(file)


def convert_file(file_path: str) -> dict:

    dict_file = load_file_to_dict(file_path)

    if dict_file:
        return dict_file

    else:
        return {}
