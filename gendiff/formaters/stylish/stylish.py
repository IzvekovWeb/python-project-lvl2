from gendiff.formaters.to_str import to_str


def stylish(value, replacer=' ', space_count=2, _lvl=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            if _lvl == 1:
                result += f'{replacer * 2}{to_str(el)}: '
            else:
                result += f'{replacer * 2}{replacer * 4 * (_lvl - 1)}{to_str(el)}: ' # noqa
            result += stylish(val, replacer, space_count, _lvl + 1) + '\n'
        result += f"{replacer * 4 * (_lvl - 1)}" + '}'
    else:
        result = to_str(value)
    return result
