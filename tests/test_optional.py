import unittest
import io
from .utility import CaptureOutput, TestParser


def one(text: str="foo"):
    pass


def two(text: str="foo", num: int=1):
    pass


def two_mixed(text: str, num: int=1):
    pass


class TestOptional(TestParser):
    def test_one(self):
        test_cases = {
            '--text bar': {'text': 'bar'},
            '': {'text': 'foo'}
        }
        for args, expected in test_cases.items():
            with self.subTest(args=args):
                self.assertParsed(one, args, expected)

    def test_one_error(self):
        test_cases = [
            'foo',
            '--num 3'
        ]
        for args in test_cases:
            with self.subTest(args=args):
                self.assertExit(one, args)

    def test_two(self):
        test_cases = {
            '--text bar --num 3': {'text': 'bar', 'num': 3},
            '--text bar': {'text': 'bar', 'num': 1},
            '--num 3': {'text': 'foo', 'num': 3},
            '': {'text': 'foo', 'num': 1}
        }
        for args, expected in test_cases.items():
            with self.subTest(args=args):
                self.assertParsed(two, args, expected)

    def test_two_error(self):
        test_cases = [
            "bar",
            "--bar"
        ]
        for args in test_cases:
            with self.subTest(args=args):
                self.assertExit(two, args)

    def test_two_mixed(self):
        test_cases = {
            'bar --num 3': {'text': 'bar', 'num': 3},
            '--num 3 bar': {'text': 'bar', 'num': 3},
            'bar': {'text': 'bar', 'num': 1},
        }
        for args, expected in test_cases.items():
            with self.subTest(args=args):
                self.assertParsed(two_mixed, args, expected)

    def test_two_mixed_error(self):
        test_cases = [
            "--bar",
            '--num 3',
            ''
        ]
        for args in test_cases:
            with self.subTest(args=args):
                self.assertExit(two_mixed, args)


if __name__ == "__main__":
    unittest.main()
