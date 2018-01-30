import unittest
import io
from typedargparse import parse_args
from .utility import CaptureOutput

def one_str(text: str):
    pass

def two_str(text1: str, text2: str):
    pass

class TestPositional(unittest.TestCase):

    def test_one_str(self):
        args_list = 'foo'.split()
        parsed_args = parse_args(one_str, args=args_list)
        self.assertEqual(parsed_args.text, args_list[0])

    def test_one_str_error(self):
        args_list = []
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                args = parse_args(one_str, args=args_list)

    def test_two_str(self):
        args_list = 'foo bar'.split()
        args = parse_args(two_str, args=args_list)
        self.assertEqual(args.text1, args_list[0])
        self.assertEqual(args.text2, args_list[1])

    def test_two_str_error_no_arg(self):
        args_list = []
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                args = parse_args(two_str, args=args_list)

    def test_two_str_error_one_arg(self):
        args_list = 'foo'.split()
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                args = parse_args(two_str, args=args_list)


if __name__ == "__main__":
    unittest.main()
