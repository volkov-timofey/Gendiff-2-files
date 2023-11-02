def format_value(node):
    """
    Lower case for bool value
    """
    if isinstance(node, str):
        return f"'{node}'"

    if node is None:
        return str('null')

    if node is True or node is False:
        return str(node).lower()

    else:
        return str(node)


def output_plain(
    flag_action: str,
    path: str,
    value
) -> str:
    """
    Function for create correct answer
    """
    # path[1:] for delate '.' in path '.common.setting5'
    path = f"'{path[1:]}'"
    value = [
        '[complex value]'
        if isinstance(_, dict)
        else format_value(_)
        for _ in value
    ]

    if flag_action == 'add':
        return f'Property {path} was added with value: {value[0]}'

    elif flag_action == 'del':
        return f'Property {path} was removed'

    elif flag_action == 'change':
        val_1, val_2 = value
        return f'Property {path} was updated. From {val_1} to {val_2}'
    else:
        return ''


def plain(diff: dict) -> str:
    """
    Plain formatter for visual changes in files
    """

    def inner(node, path=''):

        def walker(key, path=path):
            """
            Get path from key and value
            """
            path += f'.{str(key)}'

            if isinstance(node[key], dict):
                return inner(node[key], path)

            if isinstance(node[key], list):
                flag_action, value = node[key][0], node[key][1:]

                return output_plain(flag_action, path, value)

        result = '\n'.join(list(map(walker, node)))

        return result.replace('\n\n', '\n')

    return inner(diff)
