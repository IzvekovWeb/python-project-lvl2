

def plain(tree): # noqa

    def make_plain(node, path):
        if isinstance(node, dict):
            result = ''
            for name, item in node.items():
                if name == 'change':
                    continue
                if item['change'] == 'added' or item['change'] == 'removed':
                    result += create_string(path, item, name)
                    continue
                if isinstance(item['child'], dict):
                    if item['change'] == 'updated':
                        result += create_string(path, item, name)
                    else:
                        path.append(name)
                        result += make_plain(item['child'], path)
                        path.pop()
                else:
                    result += create_string(path, item, name)
        else:
            result = node
        return result

    result = make_plain(tree, [])
    n_index = result.rfind('\n')
    if (n_index + 1) == len(result):
        result = result[:-1]

    return result


def create_string(path, item, name): # noqa
    change = item['change']

    if len(path) > 0:
        path = f"'{'.'.join(path)}.{name}'"
    else:
        path = f"'{name}'"

    def is_complex(value):
        for val in value.values():
            if isinstance(val, dict):
                return True
        return False

    value = item['child']
    if isinstance(value, dict):
        is_comlex = is_complex(value)
        if is_comlex:
            value = '[complex value]'
        else:
            value = to_str(value)
    else:
        value = to_str(value)

    string = f"Property {path} was {change}"
    if change == 'updated':
        to = to_str(item['to'])
        string += f". From {value} to {to}"
    elif change == 'added':
        string += f" with value: {value}"
    elif change is None:
        return ''
    string += '\n'

    return string


def to_str(value):
    dict_ = {False: 'false', True: 'true', None: 'null'}
    if (isinstance(value, bool) or value is None) and\
            value in dict_:
        return dict_[value]
    return f"'{str(value)}'"
