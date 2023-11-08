REPLACER = ' '
SPACES_COUNT = 2

DICT_STYLE = {
    'add': '+ ',
    'del': '- ',
    'change': {'old_value': '- ', 'new_value': '+ '},
    'unchange': '  '
}


def format_value(node):
    """
    Lower case for bool value
    """
    if node is None:
        return 'null'

    if node is True or node is False:
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

    if isinstance(node[key], dict):
                
        if node[key].get('action') is None:
            sub_json = concate_result_str(
                node[key],
                level
            )
            return f'\n{tabulate_for_dict_value}{str(key)}: {sub_json}'
            
        else:
            action = node[key]['action']
            style = DICT_STYLE[action]

            return (
                f'\n{tabulate}{style["old_value"]}{str(key)}: '
                f'{concate_result_str(node[key]["old_value"], level)}'
                f'\n{tabulate}{style["new_value"]}{str(key)}: '
                f'{concate_result_str(node[key]["new_value"], level)}'
            ) if action == 'change' \
                else (
                    f'\n{tabulate}{style}{str(key)}: '
                    f'{concate_result_str(node[key]["value"], level)}'
            )



    else:
        return (
            f'\n{tabulate_for_dict_value}{str(key)}: '
            f'{concate_result_str(node[key], level)}'
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
