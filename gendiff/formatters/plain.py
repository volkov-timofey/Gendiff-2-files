def get_plain(diff: dict) -> str:
    """
    Plain formatter for visual changes in files
    """
    return format_value(diff)


def format_value(node, path: str = '') -> str:

    if isinstance(node, dict):
        list_result = [
            _ for _ in map(
                lambda key: format_dictionary({key: node[key]}, path), node
            ) if _
        ]
        return '\n'.join(list_result)

    if isinstance(node, str):
        return f"'{node}'"

    if node is None:
        return 'null'

    if isinstance(node, bool):
        return str(node).lower()

    else:
        return str(node)


def format_dictionary(node: dict, path: str) -> str:
    """
    Return formatted dictionary value
    """

    key, value = next(iter(node.items()))
    path += f'.{str(key)}'

    if isinstance(value, dict):
        action = value.get('action')

        if action == 'nested':
            return format_value(value['value'], path)

        elif action == 'add':
            return (
                f"Property '{path[1:]}' was added with value: "
                f"{format_value(value['value'])}"
            )

        elif action == 'del':
            return f"Property '{path[1:]}' was removed"

        elif action == 'change':
            return (
                f"Property '{path[1:]}' was updated. "
                f"From {format_value(value['old_value'])} to "
                f"{format_value(value['new_value'])}"
            )

    else:
        return '[complex value]'
