from difference_calculator.open_check_file import open_check_file
from difference_calculator.generate_diff import diff
from difference_calculator import stylish


def engine(file1, file2, formatter=stylish) -> str:
    """
    Module for open files,
    calculating the difference
    and formatter result
    """

    f1_dict, f2_dict = open_check_file(file1, file2)
    diff_str = diff(f1_dict, f2_dict, formatter)
    return diff_str
