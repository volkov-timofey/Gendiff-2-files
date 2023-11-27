REPLACER = ' '
SPACES_COUNT = 4

ACTION_STYLES = {
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
    - process_nodes - просмотрщик diff и словарей nested
    - format_node - шаблонизатор ответов
    - format_value - форматирование значений

    В plain структура схожая
    """
    return process_nodes(diff)


def process_nodes(node, level=0) -> str:
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
    key, value = next(iter(node.items()))

    action = value.get('action')
    style = ACTION_STYLES[action]

    level += 1
    # Чтобы вычислить отступ,
    # можно использовать формулу глубина * количество отступов — смещение влево
    # количество пробелов на один уровень — 4, смещение влево — 2.
    # из 6го пункта задания
    # использовал в итоге эту формулу
    tabulate = REPLACER * (SPACES_COUNT * level - len(style))

    if action == 'nested':
        return (
            f'\n{tabulate}{style}{key}: '
            f'{process_nodes(value["value"], level)}'
        )

    if action in ('add', 'del', 'unchange'):
        return (
            f'\n{tabulate}{style}{key}: '
            f'{format_value(value["value"], level)}'
        )

    elif action == 'change':
        return (
            f'\n{tabulate}{style["old_value"]}{key}: '
            f'{format_value(value["old_value"], level)}'
            f'\n{tabulate}{style["new_value"]}{key}: '
            f'{format_value(value["new_value"], level)}'
        )


def format_value(node, level=0):
    """
    Return formatted value
    """

    if isinstance(node, dict):
        level += 1
        tabulate_for_dict_value = REPLACER * (SPACES_COUNT * level)
        final_tabulate = f'\n{REPLACER * (SPACES_COUNT * level - SPACES_COUNT)}'

        keys = node.keys()
        values = node.values()

        concat_str = ''.join(list(map(
            lambda key, value: (f'\n{tabulate_for_dict_value}{key}: '
                                f'{format_value(value, level)}'
                                ),
            keys,
            values
        )))
        result = '{' + concat_str + final_tabulate + '}'
        return result

    if node is None:
        return 'null'

    if isinstance(node, bool):
        return str(node).lower()

    return node
