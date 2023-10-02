from difference_calculator.open_check_file import open_check_file
from difference_calculator.generate_diff import diff


def engine(file1, file2, formatter):

    f1_dict, f2_dict = open_check_file(file1, file2)
    diff_dict = diff(f1_dict, f2_dict)
    return formatter(diff_dict)
