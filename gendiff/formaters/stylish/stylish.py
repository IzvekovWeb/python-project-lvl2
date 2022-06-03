
def stylish(json): # noqa

    def make_stylish(node, lvl, spacer=' '):
        if isinstance(node, dict):
            result = '{\n'
            for name, item in node.items():
                if isinstance(item, dict) and 'child' in item:
                    result += create_string(item, name, lvl, spacer, item['change']) # noqa
                    if item['change'] != 'updated':
                        result += str((make_stylish(item['child'], lvl + 1))) + "\n" # noqa
                else:
                    result += just_print(node, lvl, spacer, False)
                    break
            lvl -= 1
            if lvl == 0:
                result += f"{make_space(lvl, spacer)}" + "}"
            else:
                result += f"{make_space(lvl, spacer)}" + "  }"
        else:
            result = to_str(node)

        return result

    return make_stylish(json, lvl=1)


def create_string(item, name, lvl, spacer, change): # noqa
    space = make_space(lvl, spacer)

    string = ''
    if change == 'updated':
        if isinstance(item, dict) and 'child' in item:
            if isinstance(item['child'], dict):
                string += space + '- ' + name + ': ' +\
                    '{\n' + just_print(item['child'], lvl + 1, spacer)
            else:
                string += space + '- ' + name + ': ' +\
                    just_print(item['child'], lvl, spacer) + '\n'

        else:
            string += space + '- ' + name + ': ' + item['child'] + '\n'

        if isinstance(item, dict) and 'to' in item:
            if isinstance(item['to'], dict):
                string += space + '+ ' + name + ': ' +\
                    '{\n' + just_print(item['to'], lvl + 1, spacer)
            else:
                string += space + '+ ' + name + ': ' +\
                    just_print(item['to'], lvl, spacer) + '\n'
        else:
            string += space + '+ ' + name + ': ' + item['to'] + '\n'
    elif change == 'added':
        string += space + '+ ' + name + ': '
    elif change is None:
        string += space + '  ' + name + ': '
    elif change == 'removed':
        string += space + '- ' + name + ': '

    return string


def just_print(node, indent, spacer, close=True):
    if isinstance(node, dict):
        res = ''
        for key, value in node.items():
            res += spacer * 4 * indent + str(key) + ": "
            if isinstance(value, dict):
                res += '{\n'
                res += just_print(value, indent + 1, spacer)
            else:
                res += to_str(value) + "\n"
        if close:
            res += spacer * 4 * (indent - 1) + '}\n'
        return res
    else:
        return to_str(node)


def make_space(lvl, spacer):
    return f"{spacer * 2}{spacer * 4 * (lvl - 1)}"\
        if lvl > 0 else ''


def to_str(value):
    dict_ = {False: 'false', True: 'true', None: 'null'}
    if (isinstance(value, bool) or value is None) and\
            value in dict_:
        return dict_[value]
    return str(value)
