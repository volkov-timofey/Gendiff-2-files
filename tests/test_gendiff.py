import pytest

from gendiff.gen_diff import generate_diff


PATH_YAML = 'tests/fixtures/yaml/'
PATH = 'tests/fixtures/'
FORMATTER_STYLISH = 'stylish'
FORMATTER_PLAIN = 'plain'
FORMATTER_JSON = 'json'

test_array = [
    (f'{PATH}file1_empty.json',
     f'{PATH}file2_empty.json',
     FORMATTER_STYLISH,
     f'{PATH}result_empty.txt'),
    (f'{PATH}file1_empty.json',
     f'{PATH}f2_full_diff.json',
     FORMATTER_STYLISH,
     f'{PATH}result_empty_one.txt'),
    (f'{PATH}f1_equal.json',
     f'{PATH}f2_equal.json',
     FORMATTER_STYLISH,
     f'{PATH}result_equal.txt'),
    (f'{PATH}f1_full_diff.json',
     f'{PATH}f2_full_diff.json',
     FORMATTER_STYLISH,
     f'{PATH}result_full_diff.txt'),
    (f'{PATH}f1.json',
     f'{PATH}f2.json',
     FORMATTER_STYLISH,
     f'{PATH}result.txt'),
    (f'{PATH_YAML}file1_empty.yml',
     f'{PATH_YAML}file2_empty.yml',
     FORMATTER_STYLISH,
     f'{PATH}result_empty.txt'),
    (f'{PATH_YAML}file1_empty.yml',
     f'{PATH_YAML}f2_full_diff.yml',
     FORMATTER_STYLISH,
     f'{PATH}result_empty_one.txt'),
    (f'{PATH_YAML}f1_equal.yml',
     f'{PATH_YAML}f2_equal.yml',
     FORMATTER_STYLISH,
     f'{PATH}result_equal.txt'),
    (f'{PATH_YAML}f1_full_diff.yml',
     f'{PATH_YAML}f2_full_diff.yml',
     FORMATTER_STYLISH,
     f'{PATH_YAML}result_full_diff.txt'),
    (f'{PATH_YAML}f1.yml',
     f'{PATH_YAML}f2.yml',
     FORMATTER_STYLISH,
     f'{PATH_YAML}result.txt'),
    (f'{PATH_YAML}file1_not_flatten.yml',
     f'{PATH_YAML}file2_not_flatten.yml',
     FORMATTER_STYLISH,
     f'{PATH}result_not_flatten.txt'),
    (f'{PATH}file1_not_flatten.json',
     f'{PATH}file2_not_flatten.json',
     FORMATTER_STYLISH,
     f'{PATH}result_not_flatten.txt'),
    (f'{PATH}file1_not_flatten.json',
     f'{PATH}file2_not_flatten.json',
     FORMATTER_PLAIN,
     f'{PATH}result_flatten_txt.txt'),
    (f'{PATH_YAML}file1_not_flatten.yml',
     f'{PATH_YAML}file2_not_flatten.yml',
     FORMATTER_PLAIN,
     f'{PATH}result_flatten_txt.txt'),
    (f'{PATH}file1_not_flatten.json',
     f'{PATH}file2_not_flatten.json',
     FORMATTER_JSON,
     f'{PATH}result_json.txt'),
    (f'{PATH_YAML}file1_not_flatten.yml',
     f'{PATH_YAML}file2_not_flatten.yml',
     FORMATTER_JSON,
     f'{PATH}result_json.txt')
]


@pytest.mark.parametrize(
    'path_f1, path_f2, formatter_name, result',
    test_array
)
def test_function(path_f1, path_f2, formatter_name, result):
    with open(result) as result:
        assert generate_diff(
            path_f1,
            path_f2,
            formatter_name
        ) == result.read()
