from gendiff.diff_work.gendiff import generate_diff
from gendiff.diff_work.pipeline import pipeline
from gendiff.cli.cli import parse_args

from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


__all__ = (
    'generate_diff',
    'parse_args',
    'pipeline',
    'stylish',
    'plain',
    'json'
)
