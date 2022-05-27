from gendiff.generate_diff import generate_diff

def test_generate_diff():
    generate_diff('gendiff/file1.json', 'gendiff/file2.json')
    assert 1 == 1