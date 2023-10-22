from gendiff.open_check_file import open_check_file
from gendiff.gendiff import generate_diff
from gendiff import stylish


def engine(file1, file2, formatter=stylish) -> str:
    """
    Module for open files,
    calculating the difference
    and formatter result
    """

    f1_dict, f2_dict = open_check_file(file1, file2)
    diff_str = generate_diff(f1_dict, f2_dict, formatter)
    return diff_str
