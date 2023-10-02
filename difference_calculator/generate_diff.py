from functools import reduce


def is_not_none(dict_: dict, key: str) -> bool:
    """
    key in dict
    """
    return dict_.get(key) is not None


def diff(dict1, dict2):

    def inner(node1, node2):
        intersection_keys = node1.keys() & node2.keys()
        sort_all_keys = sorted(node1.keys() | node2.keys())

        def searcher(key):
            key_in_dict1 = is_not_none(node1, key)

            if key in intersection_keys:

                if node1[key] == node2[key]:
                    return {f'  {key}': node1[key]}

                if (
                    isinstance(
                        node1[key], dict
                    ) and isinstance(
                            node2[key], dict
                          )
                ):
                    return {f'  {key}': inner(node1[key], node2[key])}

                else:
                    return {
                        f'- {key}': node1[key],
                        f'+ {key}': node2[key]
                    }

            else:
                return {f'- {key}': node1[key]} \
                    if key_in_dict1 \
                    else {f'+ {key}': node2[key]}

        result = reduce(lambda x, y: x | y, map(searcher, sort_all_keys), {})
        return result

    return inner(dict1, dict2)
