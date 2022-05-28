from gendiff.parsers.parse import parse_yaml, parse_json


def test_parse():
    yaml_result = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    assert parse_yaml('gendiff/parsers/file1.yaml') == yaml_result

    assert parse_json('gendiff/parsers/file2.json') == \
        {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
