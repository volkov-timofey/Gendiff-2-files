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

    # не помню в какой момент изучения Python
    # получил информацию, что много if/elif
    # не является хорошим тоном
    # поэтому стараюсь минимизировать
    # как здесь, ниже первого if пройдут
    # только json и yaml, отсюда и поставил else

    if ext == '.json':
        return json.loads(file)

    elif ext in ('.yml', '.yaml'):
        return yaml.safe_load(file)


def convert_file(file_path: str) -> dict:

    return load_file_to_dict(file_path) if load_file_to_dict(file_path) else {}
