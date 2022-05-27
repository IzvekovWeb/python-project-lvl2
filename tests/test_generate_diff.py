import pytest
from gendiff.generate_diff import generate_diff

def test_generate_diff():
    with open('tests/fixtures/gendiff_result.txt', 'r') as file:
        result = file.read()

    assert generate_diff('gendiff/file1.json', 'gendiff/file2.json') == result


def test_exception():
    # Добавляем: as e. e – произвольное имя переменной содержащей исключение
    with pytest.raises(Exception) as e:
        generate_diff()

    assert str(e.value) == "generate_diff() missing 2 required positional arguments: 'first_file' and 'second_file'"