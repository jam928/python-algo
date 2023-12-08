import highest_scoring_word as h


def test_find_the_highest_scoring_word():
    assert h.highest_scoring_word('hello my name is xavier') == 'xavier'
    assert h.highest_scoring_word('what time are we climbing up the volcano') == 'volcano'
    assert h.highest_scoring_word('take me to semynak') == 'semynak'
