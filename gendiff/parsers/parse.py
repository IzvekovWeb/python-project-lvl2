from yaml import Loader, load


def parse_yaml():
    yaml_f1 = load(open('gendiff/parsers/file1.yaml', 'r'), Loader=Loader)
    yaml_f2 = load(open('gendiff/parsers/file2.yml', 'r'), Loader=Loader)

    print(yaml_f1)
    print()
    print(yaml_f2)

parse_yaml()