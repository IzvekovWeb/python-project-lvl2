from gendiff.formaters.to_str import to_str


def plain(tree):

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
                else:
                    result += create_string(path, item, name)
                
        else:
            result = to_str(node)
        return result

    res = make_plain(tree, [])

    print(res)
    return res


def create_string(path, item, name):
    change = item['change']
    path = f"{'.'.join(path)}.{name}"
    value = item['child']
    if isinstance(value, dict):
        value = '[complex value]'
    value = to_str(value)

    string = f"Property {path} was {change}"
    if change == 'updated':
        to = to_str(item['to'])
        string += f". From {value} to {to}"
    elif change == 'added':
        string += f" with value: {value}"
    elif change == None:
        return ''
    
    string += '\n'

    return string


rr = {'common': {'change': None, 'child': {'follow': {'change': 'added', 'child': False}, 'setting1': {'change': None, 'child': 'Value 1'}, 'setting2': {'change': 'removed', 'child': 200}, 'setting3': {'change': 'updated', 'child': True, 'to': None}, 'setting4': {'change': 'added', 'child': 'blah blah'}, 'setting5': {'change': 'added', 'child': {'key5': 'value5'}}, 'setting6': {'change': None, 'child': {'doge': {'change': None, 'child': {'wow': {'change': 'updated', 'child': '', 'to': 'so much'}}}, 'key': {'change': None, 'child': 'value'}, 'ops': {'change': 'added', 'child': 'vops'}}}}}, 'group1': {'change': None, 'child': {'baz': {'change': 'updated', 'child': 'bas', 'to': 'bars'}, 'foo': {'change': None, 'child': 'bar'}, 'nest': {'change': 'updated', 'child': {'key': 'value'}, 'to': 'str'}}}, 'group2': {'change': 'removed', 'child': {'abc': 12345, 'deep': {'id': 45}}}, 'group3': {'change': 'added', 'child': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}
plain(rr)