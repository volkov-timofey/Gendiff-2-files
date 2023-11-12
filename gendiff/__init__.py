from gendiff.gen_diff import generate_diff
from gendiff.cli.cli import parse_args

from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


__all__ = (
    'generate_diff',
    'parse_args',
    'get_stylish',
    'get_plain',
    'get_json'
)
