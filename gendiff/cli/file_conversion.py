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


def check_file(file_path: str) -> dict:
    """
    Check file .json, .yml, .yaml
    Output -> dictionary
    """
    ext, file = read_file(file_path)
    
    if ext not in ('.json', '.yml', '.yaml'):
        return None

    if ext == '.json':
        return json.loads(file)
    else:
        return yaml.safe_load(file)

  
def convert_files(file1_path: str, file2_path: str) -> (dict, dict):
    
    dict1 = check_file(file1_path) if check_file(file1_path) else {}
    dict2 = check_file(file2_path) if check_file(file2_path) else {}

    return (dict1, dict2)
