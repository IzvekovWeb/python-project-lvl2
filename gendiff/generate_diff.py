from gendiff.parsers.parse import parse_by_extension


def generate_diff(path_file1, path_file2): # noqa
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
                        res[f"  {key}"] = add_space(struct_1[key])
                    else:
                        # Значения различные
                        if isinstance(struct_1[key], dict) and \
                                isinstance(struct_2[key], dict):

                            subval = make_diff(struct_1[key], struct_2[key])
                            res[f"  {key}"] = subval
                        else:
                            res[f"- {key}"] = add_space(struct_1[key])
                            res[f"+ {key}"] = add_space(struct_2[key])
                else:
                    # Ключ только в 1м файле
                    res[f"- {key}"] = add_space(struct_1[key])
            else:
                # Ключ только во 2м файле
                res[f"+ {key}"] = add_space(struct_2[key])

        return res

    result = make_diff(file1, file2)
    return result


def add_space(value):
    if isinstance(value, dict):
        result = {}
        for el, val in value.items():
            if isinstance(val, dict):
                result[f"  {el}"] = add_space(val)
            else:
                result[f"  {el}"] = val
        return result
    return value
