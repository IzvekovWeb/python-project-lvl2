from gendiff.stylish import stylish


def test_stylish():
    with open('tests/fixtures/stylish_result.txt', 'r') as file:
        result = file.read()
    assert stylish('gendiff/fixtures/gendiff_result.txt') == result
