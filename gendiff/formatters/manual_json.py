def json(
    dict_: dict,
    replacer: str = ' ',
    spaces_count: int = 2
) -> str:
    """
    Formatter json valid string
    """
    def inner(node, level=1):

        if isinstance(node, dict):
            result = '{'

            def walker(key, spaces_count=spaces_count):
                tabulate = replacer * spaces_count * level
                new_level = level + spaces_count

                # recursion if value/es dict
                if isinstance(node[key], dict):
                    sub_json = inner(node[key], new_level)
                    return f'\n{tabulate}"{str(key)}": {sub_json},'

                # recursion for create sub_string result
                if isinstance(node[key], list):

                    return (
                        f'\n{tabulate}"{str(key)}": '
                        f'[{inner(node[key][1], new_level)}, '
                        f'{inner(node[key][2], new_level)}],'
                    ) if len(node[key]) > 2 \
                        else (
                            f'\n{tabulate}"{str(key)}": '
                            f'{inner(node[key][1], new_level)},'
                    )

                # for not intersection keys
                else:
                    return (
                        f'\n{tabulate}"{str(key)}": '
                        f'{inner(node[key], new_level)},'
                    )

            result += ''.join(list(map(walker, node)))
            # result[:-1] for delate ',' after last value
            result = result[:-1] + f'\n{replacer*spaces_count*(level-1)}' + '}'
            return result
        else:
            return (
                f'"{str(node)}"'
                if type(node) not in (int, float)
                else str(node)
            )

    return inner(dict_)
