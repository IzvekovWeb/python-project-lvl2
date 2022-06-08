from gendiff.formaters.stylish.stylish import stylish
from gendiff.gendiff import generate_diff

def test_stylish():
    with open('tests/fixtures/result_stylish', 'r') as file:
        result = file.read()

    assert stylish(generate_diff('gendiff/parsers/file1.yml', 'gendiff/parsers/file2.yml', 'stylish')) == result
