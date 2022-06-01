from gendiff.generate_diff import generate_diff


def stylish(value, replacer = ' ', space_count = 2, _lvl = 1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            if _lvl == 1:
                result += f'{replacer * 2}{to_str(el)}: '
            else:
                result += f'{replacer * 2}{replacer * 4 * (_lvl-1)}{to_str(el)}: '
            result += stylish(val, replacer, space_count, _lvl+1) + '\n'
        result += f"{replacer * 4 * (_lvl-1)}" + '}'
    else:
        result = to_str(value)
    return result


def to_str(value):
    dict_ = {False: 'false', True: 'true', None: 'null'}
    if value in dict_:
        return dict_[value]
    return str(value)

a = generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.json')
stylish(a)
