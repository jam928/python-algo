import unittest
from unittest.mock import patch

import count_down as cd  # assuming count_down is a function in count_down module

class TestCountDown(unittest.TestCase):

    original_print = None
    patcher = None
    mock_print = None

    @classmethod
    def setUpClass(cls):
        global print
        # Mock print to prevent prints from cluttering the test output
        cls.original_print = print
        print = cls.mock_print = unittest.mock.Mock()
        cls.patcher = patch('builtins.print', cls.mock_print)
        cls.patcher.start()

    @classmethod
    def tearDownClass(cls):
        # Restore print after all tests are done
        cls.patcher.stop()
        print = cls.original_print

    def test_count_down(self):
        cd.count_down(3)
        self.mock_print.assert_has_calls([
            unittest.mock.call(3),  # 3 is printed first
            unittest.mock.call(2),  # 2 is printed next
            unittest.mock.call(1),  # 1 is printed last
            unittest.mock.call('All done!')  # 'All done!' is printed after counting down
        ])

    def test_count_down_zero_negative(self):
        cd.count_down(0)
        self.mock_print.assert_called_with('All done!')  # 'All done!' is printed when num is 0

        self.mock_print.reset_mock()  # Reset the previous prints
        cd.count_down(-1)
        self.mock_print.assert_called_with('All done!')  # 'All done!' is printed when num is negative

if __name__ == '__main__':
    unittest.main()
