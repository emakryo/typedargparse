import unittest
import io
from typedargparse import parse_args
from .utility import CaptureOutput

def bool_positional(flag: bool):
    pass

def bool_true(flag: bool=True):
    pass

def bool_false(flag: bool=False):
    pass

class TestBool(unittest.TestCase):
    def test_bool_positional(self):
        args_list = ["--flag"]
        args = parse_args(bool_positional, args_list)
        self.assertEqual(args.flag, True)

    def test_bool_positional_no_arg(self):
        args_list = []
        args = parse_args(bool_positional, args_list)
        self.assertEqual(args.flag, False)

    def test_true(self):
        args_list = ["--flag"]
        args = parse_args(bool_true, args_list)
        self.assertEqual(args.flag, True)

    def test_true_no_arg(self):
        args_list = []
        args = parse_args(bool_true, args_list)
        self.assertEqual(args.flag, False)

    def test_false(self):
        args_list = ["--flag"]
        args = parse_args(bool_false, args_list)
        self.assertEqual(args.flag, False)

    def test_false_no_arg(self):
        args_list = []
        args = parse_args(bool_false, args_list)
        self.assertEqual(args.flag, True)

if __name__ == "__main__":
    unittest.main()
