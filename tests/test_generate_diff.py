import pytest
from gendiff.generate_diff import generate_diff

def test_generate_diff():
    with open('tests/fixtures/gendiff_result.txt', 'r') as file:
        result = file.read()

    assert generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.json') == result
    assert generate_diff('gendiff/parsers/file1.yaml', 'gendiff/parsers/file2.yml') == result
    assert generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.yml') == result


def test_exception():
    # Добавляем: as e. e – произвольное имя переменной содержащей исключение
    with pytest.raises(Exception) as e:
        generate_diff()

    assert str(e.value) == "generate_diff() missing 2 required positional arguments: 'path_file1' and 'path_file2'"
