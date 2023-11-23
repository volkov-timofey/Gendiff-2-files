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


def get_stylish(diff: dict) -> str:
    """
    Formatter introduced changes
    """

    """
    - get_stylish точка входа
    - look_over - просмотрщик diff и словарей nested
    - format_node - шаблонизатор ответов
    - format_value - форматирование значений

    В plain структура схожая
    """
    return look_over(diff)


def look_over(node, level=0) -> str:
    final_tabulate = f'\n{REPLACER * SPACES_COUNT * level}'
    concat_str = ''.join(list(map(
        lambda key: format_node({key: node[key]}, level=level),
        node
    )))
    result = '{' + concat_str + final_tabulate + '}'
    return result


def format_node(node: dict, level) -> str:
    """
    Return formatted dictionary value
    """

    level += TAB_FIX
    tabulate = REPLACER * (SPACES_COUNT * level - TAB_FIX)

    key, value = next(iter(node.items()))

    action = value.get('action')
    style = DICT_STYLE[action]

    if action == 'nested':
        return (
            f'\n{tabulate}{style}{str(key)}: '
            f'{look_over(value["value"], level)}'
        )

    if action in ('add', 'del', 'unchange'):
        return (
            f'\n{tabulate}{style}{str(key)}: '
            f'{format_value(value["value"], level)}'
        )

    elif action == 'change':
        return (
            f'\n{tabulate}{style["old_value"]}{str(key)}: '
            f'{format_value(value["old_value"], level)}'
            f'\n{tabulate}{style["new_value"]}{str(key)}: '
            f'{format_value(value["new_value"], level)}'
        )


def format_value(node, level=0):
    """
    Return formatted value
    """

    if isinstance(node, dict):
        new_level_dict = level + TAB_FIX
        tabulate_for_dict_value = REPLACER * SPACES_COUNT * new_level_dict
        final_tabulate = f'\n{REPLACER * SPACES_COUNT * level}'

        keys = node.keys()
        values = node.values()

        concat_str = ''.join(list(map(
            lambda key, value: (f'\n{tabulate_for_dict_value}{str(key)}: '
                                f'{format_value(value, new_level_dict)}'
                                ),
            keys,
            values
        )))
        result = '{' + concat_str + final_tabulate + '}'
        return result

    if node is None:
        return 'null'

    elif isinstance(node, bool):
        return str(node).lower()

    else:
        return str(node)
