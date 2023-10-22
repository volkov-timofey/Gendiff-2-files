def stylish(dict_: dict, replacer: str = ' ', spaces_count: int = 2) -> str:
    """
    Formatter introduced changes
    """

    dict_style = {
        'add': '+ ',
        'del': '- ',
        'change': ['- ', '+ '],
        'unchange': '  '
    }

    def inner(node, level=1):
        if isinstance(node, dict):
            result = '{'

            def walker(key, spaces_count=spaces_count):
                tabulate = replacer*spaces_count*level
                tabulate_for_dict_value = tabulate + replacer * 2

                if isinstance(node[key], dict):
                    sub_json = inner(node[key], level+2)
                    return f'\n{tabulate_for_dict_value}{str(key)}: {sub_json}'

                if isinstance(node[key], list):
                    flag_action = node[key][0]
                    flag_style = dict_style[flag_action]

                    return (
                            f'\n{tabulate}{flag_style[0]}{str(key)}: '
                            f'{inner(node[key][1], level+2)}'
                            f'\n{tabulate}{flag_style[1]}{str(key)}: '
                            f'{inner(node[key][2], level+2)}'
                        ) if flag_action == 'change' \
                        else (
                            f'\n{tabulate}{flag_style}{str(key)}: '
                            f'{inner(node[key][1], level+2)}'
                        )

                else:
                    return (
                            f'\n{tabulate_for_dict_value}{str(key)}: '
                            f'{inner(node[key], level+2)}'
                        )

            result += ''.join(list(map(walker, node)))
            result += f'\n{replacer*spaces_count*(level-1)}' + '}'
            return result
        else:
            return str(node)

    return inner(dict_)
