from permutations import permutations


def test_permutations():
    assert permutations('abc') == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert permutations('dog') == ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']
    assert permutations('') == ['']
