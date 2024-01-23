from anagram_grouping import anagram_grouping

def test_anagram_grouping():
    result1 = anagram_grouping(['cat', 'act', 'dog', 'god', 'tac'])
    result2 = anagram_grouping(['listen', 'silent', 'enlist', 'hello', 'world'])

    assert result1 == [['cat', 'act', 'tac'], ['dog', 'god']]
    assert result2 == [['listen', 'silent', 'enlist'], ['hello'], ['world']]
