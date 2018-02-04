import io
import sys
import unittest
from typedargparse import TypedArgumentParser as Parser


class CaptureOutput:
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        sys.stdout.flush()
        sys.stderr.flush()
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        sys.stdout = self._stdout
        sys.stderr = self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr


class TestParser(unittest.TestCase):
    def assertParsed(self, func, args, expected):
        parsed = Parser(func).parse_args(args.split())
        self.assertEqual(vars(parsed), expected)

    def assertExit(self, func, args):
        stderr = io.StringIO()
        with CaptureOutput(stderr=stderr):
            with self.assertRaises(SystemExit):
                Parser(func).parse_args(args.split())
