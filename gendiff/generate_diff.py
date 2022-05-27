import json


def generate_diff(first_file, second_file):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))

    f1_keys = list(file1.keys())
    f2_keys = list(file2.keys())

    all_keys = sorted(set(f1_keys + f2_keys))

    res = '{\n'
    for key in all_keys:
        if key in file1:
            if key in file2:
                # Ключ есть в обоих файлах
                if file1[key] == file2[key]:
                    # Значения равны
                    res += f'   {key}: {file1[key]}\n'
                else:
                    # Значения различные
                    res += f' - {key}: {file1[key]}\n'
                    res += f' + {key}: {file2[key]}\n'
            else:
                # Ключ только в 1м файле
                res += f' - {key}: {file1[key]}\n'
        else:
            # Ключ только во 2м файле
            res += f' + {key}: {file2[key]}\n'

    res += '}'
    print(res)
    return res
