from gendiff import generate_diff

def test_generate_diff():
    with open('tests/fixtures/plain_result.txt', 'r') as file:
        plain_result = file.read()

    assert str(generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.json', 'plain')) == plain_result
    assert str(generate_diff('gendiff/parsers/file1.yaml', 'gendiff/parsers/file2.yml', 'plain')) == plain_result
    assert str(generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.yml', 'plain')) == plain_result
