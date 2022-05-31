from gendiff.parsers.parse import parse_by_extension
import json

def generate_diff(path_file1, path_file2):
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
                        res[key] =  struct_1[key]
                    else:
                        # Значения различные
                        if isinstance(struct_1[key], dict) \
                            and isinstance(struct_2[key], dict):

                            subval = make_diff(struct_1[key], struct_2[key])
                            res[key] =  subval
                        else:
                            res[key] =  {
                                    'value_1': struct_1[key], 
                                    'value_2': struct_2[key],
                                    'status': 'diff_val'
                                }
                else:
                    # Ключ только в 1м файле
                    res[key] =  {'value': struct_1[key], 'status': '-'}
            else:
                # Ключ только во 2м файле
                res[key] =  {'value': struct_2[key], 'status': '+'}

        return res

    result = make_diff(file1, file2)

    print(json.dumps(result, indent=4, sort_keys=True))
    return result
