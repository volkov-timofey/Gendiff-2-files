from functools import reduce
from gendiff.open_check_file import open_check_file


def is_not_none(dict_: dict, key: str) -> bool:
    """
    key in dict
    """
    return dict_.get(key) is not None


def generate_diff(dict1: dict, dict2: dict, formatter=None) -> dict:
    """
    Calculates the difference between files
    result - > dict
    {
    key: ['flag_action', *value]
    }

    flag_action:
    add, unchange, change, del
    """

    dict1, dict2 = open_check_file(dict1, dict2) \
        if isinstance(dict1, str) and isinstance(dict2, str) \
        else (dict1, dict2)

    def inner(node1, node2):

        intersection_keys = node1.keys() & node2.keys()
        sort_all_keys = sorted(node1.keys() | node2.keys())

        def searcher(key):
            """
            Function searcher, for concate result
            """
            key_in_dict1 = is_not_none(node1, key)

            if key in intersection_keys:

                if node1[key] == node2[key]:
                    return {key: ['unchange', node1[key]]}

                # if values is dict -> recursion
                if (
                    isinstance(
                        node1[key], dict
                    ) and isinstance(
                            node2[key], dict
                          )
                ):
                    return {key: inner(node1[key], node2[key])}

                else:
                    return {
                        key: ['change', node1[key], node2[key]]
                    }

            else:
                return {key: ['del', node1[key]]} \
                    if key_in_dict1 \
                    else {key: ['add', node2[key]]}

        result = reduce(lambda x, y: x | y, map(searcher, sort_all_keys), {})
        return result

    return formatter(inner(dict1, dict2))
