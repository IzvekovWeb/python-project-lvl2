import yaml
import json


def parse_yaml(file):
    return yaml.load(open(file, 'r'), Loader=yaml.Loader)


def parse_json(file):
    return json.load(open(file))


def parse_by_extension(path_file1, path_file2):

    def parse(path_file):
        # Определяем расширение файлов
        ext = path_file[path_file.rfind('.') + 1:]

        # Парсим файл в зависимости от его расширения
        for extension, path in [(ext, path_file)]:
            if extension in ('json'):
                return parse_json(path)
            elif extension in ('yaml', 'yml'):
                return parse_yaml(path)

    file1, file2 = map(parse, [path_file1, path_file2])
    return file1, file2
