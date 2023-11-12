REPLACER = ' '
SPACES_COUNT = 2

DICT_STYLE = {
    'add': '+ ',
    'del': '- ',
    'change': {'old_value': '- ', 'new_value': '+ '},
    'unchange': '  ',
    'nested': ''
}


def format_value(node, level=None):
    """
    Return formatted value
    """
    if isinstance(node, dict):
        return concate_result_str(node, level)

    if node is None:
        return 'null'

    if isinstance(node, bool):
        return str(node).lower()

    else:
        return str(node)


def extract_format_pair(key, node, level):
    """
    Extracr formatted pair (key, value)
    """

    tabulate = REPLACER * SPACES_COUNT * level
    tabulate_for_dict_value = tabulate + REPLACER * SPACES_COUNT
    level = level + SPACES_COUNT
    value = node[key]

    if isinstance(value, dict):

        action = value.get('action')
        style = DICT_STYLE.get(action)

        if action == 'nested':
            sub_json = concate_result_str(value['value'], level)
            return f'\n{tabulate_for_dict_value}{str(key)}: {sub_json}'

        if action in ('add', 'del', 'unchange'):
            return (
                    f'\n{tabulate}{style}{str(key)}: '
                    f'{format_value(value["value"], level)}'
            )

        if action == 'change':
            return (
                f'\n{tabulate}{style["old_value"]}{str(key)}: '
                f'{concate_result_str(value["old_value"], level)}'
                f'\n{tabulate}{style["new_value"]}{str(key)}: '
                f'{concate_result_str(value["new_value"], level)}'
            )

        else:
            return (
                f'\n{tabulate_for_dict_value}{str(key)}: '
                f'{format_value(value, level)}'
            )

    else:
        return (
            f'\n{tabulate_for_dict_value}{str(key)}: '
            f'{format_value(value)}'
        )


def concate_result_str(node, level=1):

    if isinstance(node, dict):
        final_tabulate = f'\n{REPLACER*SPACES_COUNT*(level-1)}'
        concate_str = ''.join(list(map(
            lambda key: extract_format_pair(
                key,
                node,
                level
            ),
            node
        )))
        result = '{' + concate_str + final_tabulate + '}'
        return result
    else:
        return format_value(node)


def get_stylish(diff: dict) -> str:
    """
    Formatter introduced changes
    """
    return concate_result_str(diff)
