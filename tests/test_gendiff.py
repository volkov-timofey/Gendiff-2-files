import pytest

from gendiff.diff_work.pipeline import engine


FORMATTER = 'stylish'
FORMATTER_PLAIN = 'plain'
FORMATTER_JSON = 'json'


@pytest.fixture
def path():
    return 'tests/fixtures/'


@pytest.fixture
def result_empty_one():
    return '{\n  + follow: false\n  + proxy: 123.234.53.22\n}'


@pytest.fixture
def result_test_equal():
    return '{\n    host: hexlet.io\n    timeout: 50\n}'


@pytest.fixture
def path_yaml():
    return 'tests/fixtures/yaml/'


def test_empty(path):
    '''
    Diff two empty files
    '''
    empty_str = '{\n}'
    assert engine(
        path + 'file1_empty.json',
        path + 'file2_empty.json',
        FORMATTER
    ) == empty_str


def test_empty_one(path, result_empty_one):
    '''
    Diff empty and not empty files
    '''
    assert engine(
        path + 'file1_empty.json',
        path + 'f2_full_diff.json',
        FORMATTER
    ) == result_empty_one


def test_equal(
    path,
    result_test_equal
):
    '''
    Diff equal files
    '''
    assert engine(
        path + 'f1_equal.json',
        path + 'f2_equal.json',
        FORMATTER
    ) == result_test_equal


def test_full_diff(path):
    '''
    Diff full difference files
    '''
    with open(f'{path}result_full_diff.txt') as result_full_diff:
        assert engine(
            path + 'f1_full_diff.json',
            path + 'f2_full_diff.json',
            FORMATTER
        ) == result_full_diff.read()


def test_common(path):
    '''
    Diff two files
    '''
    with open(f'{path}result.txt') as result:
        assert engine(
            path + 'f1.json',
            path + 'f2.json',
            FORMATTER
        ) == result.read()


# gendiff_yml
def test_empty_yaml(path_yaml):
    '''
    Diff two empty files
    '''
    empty_str = '{\n}'
    assert engine(
        path_yaml + 'file1_empty.yml',
        path_yaml + 'file2_empty.yml',
        FORMATTER
    ) == empty_str


def test_empty_one_yaml(path_yaml, result_empty_one):
    '''
    Diff empty and not empty files
    '''
    assert engine(
        path_yaml + 'file1_empty.yml',
        path_yaml + 'f2_full_diff.yml',
        FORMATTER
    ) == result_empty_one


def test_equal_yaml(
    path_yaml,
    result_test_equal
):
    '''
    Diff equal files
    '''
    assert engine(
        path_yaml + 'f1_equal.yml',
        path_yaml + 'f2_equal.yml',
        FORMATTER
    ) == result_test_equal


def test_full_diff_yaml(path_yaml):
    '''
    Diff full difference files
    '''
    with open(f'{path_yaml}result_full_diff.txt') as result_full_diff:
        assert engine(
            path_yaml + 'f1_full_diff.yml',
            path_yaml + 'f2_full_diff.yml',
            FORMATTER
        ) == result_full_diff.read()


def test_common_yaml(path_yaml):
    '''
    Diff two files
    '''
    with open(f'{path_yaml}result.txt') as result:
        assert engine(
            path_yaml + 'f1.yml',
            path_yaml + 'f2.yml',
            FORMATTER
        ) == result.read()


def test_not_flatten_yaml(path, path_yaml):
    '''
    Diff two not flatten files (yaml)
    '''
    with open(f'{path}result_not_flatten.txt') as result:
        assert engine(
            path_yaml + 'file1_not_flatten.yml',
            path_yaml + 'file2_not_flatten.yml',
            FORMATTER
        ) == result.read()


def test_not_flatten_json(path):
    '''
    Diff two not flatten files (json)
    '''
    with open(f'{path}result_not_flatten.txt') as result:
        assert engine(
            path + 'file1_not_flatten.json',
            path + 'file2_not_flatten.json',
            FORMATTER
        ) == result.read()


def test_flatten_txt_json(path):
    '''
    Diff two not flatten files (json)
    '''
    with open(f'{path}result_flatten_txt.txt') as result:
        assert engine(
            path + 'file1_not_flatten.json',
            path + 'file2_not_flatten.json',
            FORMATTER_PLAIN
        ) == result.read()


def test_flatten_txt_yaml(path, path_yaml):
    '''
    Diff two not flatten files (yaml)
    '''
    with open(f'{path}result_flatten_txt.txt') as result:
        assert engine(
            path_yaml + 'file1_not_flatten.yml',
            path_yaml + 'file2_not_flatten.yml',
            FORMATTER_PLAIN
        ) == result.read()


def test_json_formatter_json(path):
    '''
    Diff two not flatten files (yaml)
    '''
    with open(f'{path}result_json.txt') as result:
        assert engine(
            path + 'file1_not_flatten.json',
            path + 'file2_not_flatten.json',
            FORMATTER_JSON
        ) == result.read()


def test_yaml_formatter_json(path, path_yaml):
    '''
    Diff two not flatten files (yaml)
    '''
    with open(f'{path}result_json.txt') as result:
        assert engine(
            path_yaml + 'file1_not_flatten.yml',
            path_yaml + 'file2_not_flatten.yml',
            FORMATTER_JSON
        ) == result.read()
