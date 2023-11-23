PATH = ''


def get_plain(diff: dict) -> str:
    """
    Plain formatter for visual changes in files
    """
    return look_over(diff)


def look_over(node, path=PATH) -> str:
    list_result = [
        _ for _ in map(
            lambda key: format_node({key: node[key]}, path), node
        ) if _
    ]
    return '\n'.join(list_result)


def format_node(node, path) -> str:

    key, value = next(iter(node.items()))

    path += f'.{str(key)}'

    action = value.get('action')

    if action == 'nested':
        return look_over(value['value'], path)

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


def format_value(node) -> str:
    """
    Return formatted value
    """
    if isinstance(node, dict):
        return '[complex value]'

    if isinstance(node, str):
        return f"'{node}'"

    if node is None:
        return 'null'

    if isinstance(node, bool):
        return str(node).lower()

    else:
        return str(node)
