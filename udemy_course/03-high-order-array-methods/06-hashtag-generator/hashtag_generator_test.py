import hashtag_generator as h


def test_generating_hashtags():
    assert h.generate_hashtag(' Hello there thanks for trying my Kata') == '#HelloThereThanksForTryingMyKata'
    assert h.generate_hashtag('    Hello     World   ') == '#HelloWorld'
    assert h.generate_hashtag('') is False
    assert h.generate_hashtag('This is a very very very very very very very very very very very very very very long input that should result in a false hashtag because it exceeds the character limit of 140') is False
