REPLACER = ' '
SPACES_COUNT = 2
TAB_FIX = 2

DICT_STYLE = {
    'add': '+ ',
    'del': '- ',
    'change': {'old_value': '- ', 'new_value': '+ '},
    'unchange': '  ',
    'nested': '  '
}


def format_value_dictionary(node: dict, level=None) -> str:
    """
    Return formatted dictionary value
    """

    level += TAB_FIX
    tabulate = REPLACER * (SPACES_COUNT * level - TAB_FIX)
    tabulate_for_dict_value = REPLACER * (SPACES_COUNT * level)

    key, value = next(iter(node.items()))

    if isinstance(value, dict):

        if value.get('action'):
            action = value['action']
            style = DICT_STYLE[action]

            if action in ('add', 'del', 'unchange', 'nested'):
                return (
                    f'\n{tabulate}{style}{str(key)}: '
                    f'{format_value(value["value"], level)}'
                )

            if action == 'change':
                return (
                    f'\n{tabulate}{style["old_value"]}{str(key)}: '
                    f'{format_value(value["old_value"], level)}'
                    f'\n{tabulate}{style["new_value"]}{str(key)}: '
                    f'{format_value(value["new_value"], level)}'
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


def format_value(node, level=0):
    """
    Return formatted value
    """
    if isinstance(node, dict):
        final_tabulate = f'\n{REPLACER * SPACES_COUNT * level}'
        concat_str = ''.join(list(map(
            lambda key: format_value_dictionary({key: node[key]}, level=level),
            node
        )))
        result = '{' + concat_str + final_tabulate + '}'
        return result

    if node is None:
        return 'null'

    elif isinstance(node, bool):
        return str(node).lower()

    else:
        return str(node)


def get_stylish(diff: dict) -> str:
    """
    Formatter introduced changes
    """

    """
    Пересобрал оба форматтера stylish и plain,
    получилась более организованная логика кода,

    если что то не корректно понял, высылайте замечания
    поправлю)
    """
    return format_value(diff)
