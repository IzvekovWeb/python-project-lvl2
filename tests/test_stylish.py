from gendiff.formaters.stylish.stylish import stylish
from gendiff.gendiff import generate_diff

def test_stylish():
    with open('tests/fixtures/stylish_result.txt', 'r') as file:
        result = file.read()

    assert stylish(generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.json', 'stylish')) == result
