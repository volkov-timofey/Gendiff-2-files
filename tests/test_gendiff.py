import pytest

from gendiff.diff_work.pipeline import pipeline


path_yaml = 'tests/fixtures/yaml/'
path = 'tests/fixtures/'
FORMATTER_STYLISH = 'stylish'
FORMATTER_PLAIN = 'plain'
FORMATTER_JSON = 'json'

test_array = [
    (path + 'file1_empty.json',
    path + 'file2_empty.json',
    FORMATTER_STYLISH,
    path + 'result_empty.txt'),
    (path + 'file1_empty.json',
    path + 'f2_full_diff.json',
    FORMATTER_STYLISH, 
    path + 'result_empty_one.txt'),
    (path + 'f1_equal.json',
    path + 'f2_equal.json',
    FORMATTER_STYLISH,
    path + 'result_equal.txt'),
    (path + 'f1_full_diff.json',
    path + 'f2_full_diff.json',
    FORMATTER_STYLISH,
    path + 'result_full_diff.txt'),
    (path + 'f1.json',
    path + 'f2.json',
    FORMATTER_STYLISH,
    path + 'result.txt'),
    (path_yaml + 'file1_empty.yml',
    path_yaml + 'file2_empty.yml',
    FORMATTER_STYLISH,
    path + 'result_empty.txt'),
    (path_yaml + 'file1_empty.yml',
    path_yaml + 'f2_full_diff.yml',
    FORMATTER_STYLISH, 
    path + 'result_empty_one.txt'),
    (path_yaml + 'f1_equal.yml',
    path_yaml + 'f2_equal.yml',
    FORMATTER_STYLISH,
    path + 'result_equal.txt'),
    (path_yaml + 'f1_full_diff.yml',
    path_yaml + 'f2_full_diff.yml', 
    FORMATTER_STYLISH,
    path_yaml + 'result_full_diff.txt'),
    (path_yaml + 'f1.yml', 
    path_yaml + 'f2.yml', 
    FORMATTER_STYLISH,
    path_yaml + 'result.txt'),
    (path_yaml + 'file1_not_flatten.yml',
    path_yaml + 'file2_not_flatten.yml',
    FORMATTER_STYLISH,
    path + 'result_not_flatten.txt'),
    (path + 'file1_not_flatten.json',
    path + 'file2_not_flatten.json',
    FORMATTER_STYLISH,
    path + 'result_not_flatten.txt'),
    (path + 'file1_not_flatten.json',
    path + 'file2_not_flatten.json',
    FORMATTER_PLAIN,
    path + 'result_flatten_txt.txt'),
    (path_yaml + 'file1_not_flatten.yml',
    path_yaml + 'file2_not_flatten.yml',
    FORMATTER_PLAIN,
    path + 'result_flatten_txt.txt'),
    (path + 'file1_not_flatten.json',
    path + 'file2_not_flatten.json',
    FORMATTER_JSON,
    path + 'result_json.txt'),
    (path_yaml + 'file1_not_flatten.yml',
    path_yaml + 'file2_not_flatten.yml',
    FORMATTER_JSON,
    path + 'result_json.txt')
]

@pytest.mark.parametrize(
    'path_f1, path_f2, formatter_name, result',
    test_array
)
def test_function(path_f1, path_f2, formatter_name, result):
    with open(result) as result:
        assert pipeline(
            path_f1,
            path_f2,
            formatter_name
        ) == result.read()