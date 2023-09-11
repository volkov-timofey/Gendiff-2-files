import pytest


from difference_calculator.scripts.gendiff import generate_diff as gendiff


def json_to_str(file_name):
    with open('tests/fixtures/f2_full_diff.txt') as f2_full_diff, \
            open('tests/fixtures/f1_equal.txt') as f1_equal, \
            open('tests/fixtures/f2_equal.txt') as f2_equal, \
            open('tests/fixtures/result_full_diff.txt') as result_full_diff, \
            open('tests/fixtures/result.txt') as result:

        files = {
            'f2_full_diff': f2_full_diff,
            'f1_equal': f1_equal,
            'f2_equal': f2_equal,
            'result_full_diff': result_full_diff,
            'result': result,
        }

        return files[file_name].read()


@pytest.fixture
def path():
    return 'tests/fixtures/'


def test_empty(path):
    '''
    Diff two empty files
    '''
    empty_str = '{\n}'
    assert gendiff(
        path + 'file1_empty.txt',
        path + 'file2_empty.txt'
    ) == empty_str


def test_empty_one(path, result=json_to_str('f2_full_diff')):
    '''
    Diff empty and not empty files
    '''
    assert gendiff(
        path + 'file1_empty',
        path + 'f2_full_diff'
    ) == result


def test_equal(
    path,
    result1=json_to_str('f1_equal'),
    result2=json_to_str('f2_equal')
):
    '''
    Diff equal files
    '''
    assert gendiff(
        path + 'f1_equal.txt',
        path + 'f2_equal.txt'
    ) == result1 == result2


def test_full_diff(
    path,
    result=json_to_str('result_full_diff')
):
    '''
    Diff full difference files
    '''
    assert gendiff(
        path + 'f1_full_diff.txt',
        path + 'f2_full_diff.txt'
    ) == result


def test_common(
    path,
    result=json_to_str('result')
):
    '''
    Diff two files
    '''
    assert gendiff(path + 'f1.txt', path + 'f2.txt') == result
