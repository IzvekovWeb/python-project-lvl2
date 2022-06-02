from gendiff.formaters.plain.plain import plain
from gendiff.generate_diff import generate_diff

def test_plain():
    with open('tests/fixtures/plain_result.txt', 'r') as file:
        result = file.read()
    # print(plain(generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.json', 'plain')))
    assert plain(generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.json', 'plain')) == result

# test_plain()