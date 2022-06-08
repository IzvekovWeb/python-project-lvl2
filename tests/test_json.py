from gendiff.formaters._json._json import _json
from gendiff.gendiff import generate_diff


def tn():
    with open('tests/fixtures/json_result.txt', 'r') as file:
        result = file.read()
    assert _json(generate_diff('gendiff/parsers/file1.yml', 'gendiff/parsers/file2.json', 'json')) == result
