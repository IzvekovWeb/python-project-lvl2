from gendiff.parsers.parse import parse_yaml, parse_json


def test_parse():
    with open('tests/fixtures/file1_result.txt', 'r') as file:
        result = file.read()
    assert str(parse_yaml('gendiff/parsers/file1.yml')) == result

    with open('tests/fixtures/file2_result.txt', 'r') as file:
        result = file.read()
    assert str(parse_json('gendiff/parsers/file2.json')) == result
