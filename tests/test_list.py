import unittest
from typing import List
from .utility import TestParser


def list_str(texts: List[str]):
    pass


def list_str_opt(texts: List[str]=['a']):
    pass


def list_int(nums: List[int]):
    pass


class TestList(TestParser):
    def test_list_str(self):
        test_cases = {
            "foo": {'texts': ['foo']},
            "foo bar": {'texts': ['foo', 'bar']},
            "": {'texts': []}
        }

        for args, expected in test_cases.items():
            with self.subTest(args=args):
                self.assertParsed(list_str, args, expected)

    def test_list_int(self):
        test_cases = {
            "4": {'nums': [4]},
            "1 5 10": {'nums': [1, 5, 10]},
            "": {'nums': []}
        }

        for args, expected in test_cases.items():
            with self.subTest(args=args):
                self.assertParsed(list_int, args, expected)

    def test_list_str_opt(self):
        test_cases = {
            "--texts foo": {'texts': ['foo']},
            "--texts foo bar": {'texts': ['foo', 'bar']},
            "": {'texts': ['a']}
        }

        for args, expected in test_cases.items():
            with self.subTest(args=args):
                self.assertParsed(list_str_opt, args, expected)

if __name__ == "__main__":
    unittest.main()
