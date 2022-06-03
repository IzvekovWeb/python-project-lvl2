

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

    return make_plain(tree, [])


def create_string(path, item, name):
    change = item['change']

    if len(path) > 0:
        path = f"'{'.'.join(path)}.{name}'"
    else:
        path = f"'{name}'"

    value = item['child']
    if isinstance(value, dict):
        value = '[complex value]'
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
    if value in dict_:
        return dict_[value]
    return f"'{str(value)}'"
