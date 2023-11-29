import count_vowels as cv


def test_count_vowels_in_str():
    assert cv.count_vowels("Hello World!") == 3
    assert cv.count_vowels("JavaScript") == 3
    assert cv.count_vowels("OpenAI Chatbot") == 6
    assert cv.count_vowels("Coding Challenge") == 5
