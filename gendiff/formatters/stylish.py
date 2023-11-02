def format_value(node):
    """
    Lower case for bool value
    """
    if node is None:
        return str('null')

    if node is True or node is False:
        return str(node).lower()

    else:
        return str(node)


# Есть ли какой нибудь метод namespace, для хранения и передачи аргументов?
# После извлечения функций на уровень модуля, приходится инициализировать
# в каждой функции.
# Такой вариант вложенности функций, был в теории, поэтому он и использовался.
def extract_format_pair(key, node, replacer, spaces_count, level):
    """
    Extracr formatted pair (key, value)
    """
    dict_style = {
        'add': '+ ',
        'del': '- ',
        'change': ['- ', '+ '],
        'unchange': '  '
    }

    tabulate = replacer * spaces_count * level
    tabulate_for_dict_value = tabulate + replacer * 2
    args = [replacer, spaces_count, level + 2]

    if isinstance(node[key], dict):
        sub_json = concate_result_str(
            node[key],
            *args
        )
        return f'\n{tabulate_for_dict_value}{str(key)}: {sub_json}'

    if isinstance(node[key], list):
        flag_action = node[key][0]
        flag_style = dict_style[flag_action]

        return (
            f'\n{tabulate}{flag_style[0]}{str(key)}: '
            f'{concate_result_str(node[key][1], *args)}'
            f'\n{tabulate}{flag_style[1]}{str(key)}: '
            f'{concate_result_str(node[key][2], *args)}'
        ) if flag_action == 'change' \
            else (
                f'\n{tabulate}{flag_style}{str(key)}: '
                f'{concate_result_str(node[key][1], *args)}'
        )

    else:
        return (
            f'\n{tabulate_for_dict_value}{str(key)}: '
            f'{concate_result_str(node[key], *args)}'
        )


def concate_result_str(node, replacer, spaces_count, level=1):

    if isinstance(node, dict):
        final_tabulate = f'\n{replacer*spaces_count*(level-1)}'
        concate_str = ''.join(list(map(
                            lambda key: extract_format_pair(
                                                    key,
                                                    node,
                                                    replacer,
                                                    spaces_count,
                                                    level
                                                ),
                            node
                        )))
        result = '{' + concate_str + final_tabulate + '}'
        return result
    else:
        return format_value(node)


def stylish(diff: dict, replacer: str = ' ', spaces_count: int = 2) -> str:
    """
    Formatter introduced changes
    """
    return concate_result_str(diff, replacer, spaces_count)
