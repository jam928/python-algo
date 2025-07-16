class TestCase:
    def __init__(self, expected, actual):
        self.expected = expected
        self.actual = actual

    def assertEqual(self, actual, expected):
        assert actual == expected