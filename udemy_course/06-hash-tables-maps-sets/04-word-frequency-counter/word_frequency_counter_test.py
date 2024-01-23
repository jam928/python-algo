from word_frequency_counter import word_frequency_counter


def test_word_frequency_counter():
    input_text = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away."
    expected_output = {
        'the': 4,
        'quick': 1,
        'brown': 1,
        'fox': 2,
        'jumps': 1,
        'over': 1,
        'lazy': 1,
        'dog': 2,
        'barks': 1,
        'and': 1,
        'runs': 1,
        'away': 1,
    }

    result = word_frequency_counter(input_text)
    assert result == expected_output


def test_word_frequency_counter_empty_input():
    input_text = ''
    expected_output = {}

    result = word_frequency_counter(input_text)
    assert result == expected_output


def test_word_frequency_counter_single_word():
    input_text = 'hello'
    expected_output = {
        'hello': 1,
    }

    result = word_frequency_counter(input_text)
    assert result == expected_output
