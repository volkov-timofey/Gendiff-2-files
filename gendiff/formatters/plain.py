def format_value(node):
    """
    Lower case for bool value
    """
    if isinstance(node, str):
        return f"'{node}'"

    if node is None:
        return 'null'

    if isinstance(node, bool):
        return str(node).lower()

    if isinstance(node, dict):
        return '[complex value]'

    else:
        return str(node)


def output_plain(action: str, path: str, value: dict) -> str:
    """
    Function for create correct answer
    """
    # path[1:] for delate '.' in path '.common.setting5'
    path = f"'{path[1:]}'"
    value = {
        key: format_value(value[key]) for key in value
    }

    if action == 'add':
        return f'Property {path} was added with value: {value["value"]}'

    elif action == 'del':
        return f'Property {path} was removed'

    elif action == 'change':
        return (
            f'Property {path} was updated. '
            f'From {value["old_value"]} to {value["new_value"]}'
        )


def extract_format_pair(key, diff, path):
    """
    Extract format result for key (path) and value/values
    """

    path += f'.{str(key)}'
    value = diff[key]
    action = value['action']

    if action == 'nested':
        return get_plain(value['value'], path)

    elif action in ['add', 'del', 'change']:
        return output_plain(action, path, value)


def get_plain(diff: dict, path: str = '') -> str:
    """
    Plain formatter for visual changes in files
    """
    list_result = [
        _ for _ in map(
            lambda key: extract_format_pair(key, diff, path), diff
        ) if _
    ]
    return '\n'.join(list_result)
