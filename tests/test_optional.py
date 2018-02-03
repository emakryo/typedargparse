import unittest
import io
from typedargparse import parse_args
from .utility import CaptureOutput

def one(text: str="foo"):
    pass

def two(text: str="foo", num: int=1):
    pass

def two_mixed(text: str, num: int=1):
    pass

class TestOptional(unittest.TestCase):
    def test_one(self):
        args_list = "--text bar".split()
        args = parse_args(one, args_list)
        self.assertEqual(args.text, args_list[1])

    def test_one_with_no_arg(self):
        args_list = []
        args = parse_args(one, args_list)
        self.assertEqual(args.text, "foo")

    def test_one_no_flag_error(self):
        args_list = "foo".split()
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                args = parse_args(one, args=args_list)

    def test_one_unknown_flag_error(self):
        args_list = "--num 3".split()
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                args = parse_args(one, args=args_list)

    def test_two(self):
        args_list = "--text bar --num 3".split()
        args = parse_args(two, args_list)
        self.assertEqual(args.text, args_list[1])
        self.assertEqual(args.num, int(args_list[3]))

    def test_two_with_first_arg(self):
        args_list = "--text bar".split()
        args = parse_args(two, args_list)
        self.assertEqual(args.text, args_list[1])
        self.assertEqual(args.num, 1)

    def test_two_with_second_arg(self):
        args_list = "--num 3".split()
        args = parse_args(two, args_list)
        self.assertEqual(args.text, "foo")
        self.assertEqual(args.num, int(args_list[1]))

    def test_two_with_no_arg(self):
        args_list = []
        args = parse_args(two, args_list)
        self.assertEqual(args.text, "foo")
        self.assertEqual(args.num, 1)

    def test_two_no_flag_error(self):
        args_list = ["bar"]
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                args = parse_args(one, args=args_list)

    def test_two_unknown_flag_error(self):
        args_list = ["--bar"]
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                args = parse_args(one, args=args_list)

    def test_two_mixed(self):
        args_lists = ["bar --num 3".split(),
                      "--num 3 bar".split()]
        for args_list in args_lists:
            with self.subTest(args_list):
                args = parse_args(two_mixed, args_list)
                self.assertEqual(args.text, "bar")
                self.assertEqual(args.num, 3)

    def test_two_mixed_with_only_positional(self):
        args_list = ["bar"]
        args = parse_args(two_mixed, args_list)
        self.assertEqual(args.text, "bar")
        self.assertEqual(args.num, 1)

    def test_two_mixed_with_only_optional(self):
        args_list = "--num 3".split()
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                args = parse_args(two_mixed, args=args_list)

    def test_two_mixed_with_no_arg(self):
        args_list = []
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                args = parse_args(two_mixed, args=args_list)


if __name__ == "__main__":
    unittest.main()
