def stylish(dict_, replacer=' ', spaces_count=2):

    def inner(node, level=1):
        if isinstance(node, dict):
            result = '{'

            def walker(key, spaces_count=spaces_count):
                tabulate = replacer*spaces_count*level

                if not key.startswith(('- ', '  ', '+ ')):
                    tabulate += replacer*2

                if isinstance(node[key], dict):
                    sub_json = inner(node[key], level+2)
                    return f'\n{tabulate}{str(key)}: {sub_json}'

                else:
                    return f'\n{tabulate}{str(key)}: {node[key]}'

            result += ''.join(list(map(walker, node)))
            result += f'\n{replacer*spaces_count*(level-1)}' + '}'
            return result
        else:
            return str(node)

    return inner(dict_)
