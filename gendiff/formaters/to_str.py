def to_str(value):
    dict_ = {False: 'false', True: 'true', None: 'null'}
    if value in dict_:
        return dict_[value]
    return f"'{str(value)}'"
