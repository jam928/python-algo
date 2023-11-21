import title_case as tc
import pytest


def test_converting_string_to_title_case():
    assert tc.title_case("hello world") == 'Hello World'
    assert tc.title_case("javascript programming") == 'Javascript Programming'
    assert tc.title_case("openai chatbot") == 'Openai Chatbot'
    assert tc.title_case("I'm a little tea pot") == "I'm A Little Tea Pot"
    assert tc.title_case("sHoRt AnD sToUt") == "Short And Stout"
    assert tc.title_case("HERE IS MY HANDLE HERE IS MY SPOUT") == 'Here Is My Handle Here Is My Spout'

