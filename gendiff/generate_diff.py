from gendiff.parsers.parse import parse_by_extension
from gendiff.formaters.stylish.stylish import stylish
from gendiff.formaters.plain.plain import plain


def generate_diff(path_file1, path_file2, format):
    if format == 'stylish':
        return stylish(create_diff(path_file1, path_file2))
    else:
        return plain(create_diff(path_file1, path_file2))


def create_diff(path_file1, path_file2): # noqa
    file1, file2 = parse_by_extension(path_file1, path_file2)

    def make_diff(struct_1, struct_2):
        f1_keys = list(struct_1.keys())
        f2_keys = list(struct_2.keys())

        all_keys = sorted(set(f1_keys + f2_keys))

        res = {}
        for key in all_keys:
            if key in struct_1:
                if key in struct_2:
                    # Ключ есть в обоих файлах
                    if struct_1[key] == struct_2[key]:
                        # Значения равны
                        res[key] = {'change': None, 'child': struct_1[key]}
                    else:
                        # Значения различные
                        if isinstance(struct_1[key], dict) and \
                                isinstance(struct_2[key], dict):

                            sub_val = make_diff(struct_1[key], struct_2[key])
                            res[key] = {'change': None, 'child': sub_val}
                        else:
                            res[key] = {
                                'change': 'updated',
                                'child': struct_1[key],
                                'to': struct_2[key]
                            }
                else:
                    # Ключ только в 1м файле
                    res[key] = {'change': 'removed', 'child': struct_1[key]}
            else:
                # Ключ только во 2м файле
                res[key] = {'change': 'added', 'child': struct_2[key]}
        return res
    return make_diff(file1, file2)


def add_space(value):
    if isinstance(value, dict):
        result = {}
        for el, val in value.items():
            result[f"  {el}"] = add_space(val) if isinstance(val, dict) else val
        return result
    return value
