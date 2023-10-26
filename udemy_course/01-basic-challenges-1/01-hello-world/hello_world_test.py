import pytest
import hello_world


def test_return_hello_world_as_a_string():
    result = hello_world.hello_world()
    assert result == 'Hello World!'
