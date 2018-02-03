import unittest
import io
from typedargparse import parse_args
from .utility import CaptureOutput, TestParser

def one_str(text: str):
    pass

def two_str(text1: str, text2: str):
    pass

class TestPositional(TestParser):

    def test_one_str(self):
        self.assertParsed(one_str, 'foo', {'text': 'foo'})

    def test_one_str_error(self):
        self.assertExit(one_str, '')

    def test_two_str(self):
        self.assertParsed(two_str, 'foo bar', {'text1': 'foo', 'text2': 'bar'})

    def test_two_str_error(self):
        test_cases = [
            '',
            'foo'
        ]
        for args in test_cases:
            with self.subTest(args=args):
                self.assertExit(two_str, '')


if __name__ == "__main__":
    unittest.main()
