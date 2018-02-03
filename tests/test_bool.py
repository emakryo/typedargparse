import unittest
import io
from typedargparse import parse_args
from .utility import CaptureOutput, TestParser

def bool_positional(flag: bool):
    pass

def bool_true(flag: bool=True):
    pass

def bool_false(flag: bool=False):
    pass

class TestBool(TestParser):
    def test_bool_positional(self):
        test_cases = {
            "--flag": {'flag': True},
            "": {'flag': False},
        }
        for args, expected in test_cases.items():
            with self.subTest(args=args):
                self.assertParsed(bool_positional, args, expected)

    def test_true(self):
        test_cases = {
            "--flag": {'flag': True},
            "": {'flag': False},
        }
        for args, expected in test_cases.items():
            with self.subTest(args=args):
                self.assertParsed(bool_true, args, expected)

    def test_false(self):
        test_cases = {
            "--flag": {'flag': False},
            "": {'flag': True},
        }
        for args, expected in test_cases.items():
            with self.subTest(args=args):
                self.assertParsed(bool_false, args, expected)

if __name__ == "__main__":
    unittest.main()
