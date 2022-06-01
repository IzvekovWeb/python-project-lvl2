from gendiff.formaters.plain import plain
from gendiff.generate_diff import generate_diff

def test_plain():
    with open('tests/fixtures/plain_result.txt', 'r') as file:
        result = file.read()

    assert plain(generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.json')) == result
