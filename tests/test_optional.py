import unittest
import io
from typedargparse import parse_args
from .utility import CaptureOutput

def one_str(text: str="foo"):
    pass

class TestOptional(unittest.TestCase):
    def test_one(self):
        args_list = "--text bar".split()
        args = parse_args(one_str, args_list)
        self.assertEqual(args.text, args_list[1])

    def test_one_no_arg(self):
        args_list = []
        args = parse_args(one_str, args_list)
        self.assertEqual(args.text, "foo")

    def test_one_no_flag_error(self):
        args_list = "foo".split()
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                args = parse_args(one_str, args=args_list)

if __name__ == "__main__":
    unittest.main()
