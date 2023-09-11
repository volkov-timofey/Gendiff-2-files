import pytest


from difference_calculator.scripts.gendiff import generate_diff as gendiff


def json_to_str(file_name):
    with open('tests/fixtures/f2_full_diff.json') as f2_full_diff, \
            open('tests/fixtures/f1_equal.json') as f1_equal, \
            open('tests/fixtures/f2_equal.json') as f2_equal, \
            open('tests/fixtures/result_full_diff.json') as result_full_diff, \
            open('tests/fixtures/result.json') as result:

        files = {
            'f2_full_diff': f2_full_diff.read(),
            'f1_equal': f1_equal.read(),
            'f2_equal': f2_equal.read(),
            'result_full_diff': result_full_diff.read(),
            'result': result.read(),
        }

        return files[file_name]


@pytest.fixture
def path():
    return 'tests/fixtures/'


@pytest.fixture
def result_empty_one():
    return '{\n\t+ "host": "hexlet.io",\n\t+ "timeout": 50,\n}'


@pytest.fixture
def result_test_equal():
    return '{\n\t  "host": "hexlet.io",\n\t  "timeout": 50,\n}'


def test_empty(path):
    '''
    Diff two empty files
    '''
    empty_str = '{\n}'
    assert gendiff(
        path + 'file1_empty.json',
        path + 'file2_empty.json'
    ) == empty_str


def test_empty_one(path, result_empty_one):
    '''
    Diff empty and not empty files
    '''
    assert gendiff(
        path + 'file1_empty.json',
        path + 'f2_full_diff.json'
    ) == result_empty_one


def test_equal(
    path,
    result1=json_to_str('f1_equal'),
    result2=json_to_str('f2_equal')
):
    '''
    Diff equal files
    '''
    assert gendiff(
        path + 'f1_equal.json',
        path + 'f2_equal.json'
    ) == result1 == result2


def test_full_diff(
    path,
    result=json_to_str('result_full_diff')
):
    '''
    Diff full difference files
    '''
    assert gendiff(
        path + 'f1_full_diff.json',
        path + 'f2_full_diff.json'
    ) == result


def test_common(
    path,
    result=json_to_str('result')
):
    '''
    Diff two files
    '''
    assert gendiff(path + 'f1.json', path + 'f2.json') == result
