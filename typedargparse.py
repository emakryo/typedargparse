import argparse

def generate_parser(func):
    annotations = func.__annotations__
    parser = argparse.ArgumentParser()
    for arg_name in func.__code__.co_varnames:
        if arg_name in annotations:
            arg_type = annotations[arg_name]
        else:
            arg_type = str
        parser.add_argument(arg_name, type=arg_type)
    return parser

def parse_args(func, args=None):
    parser = generate_parser(func)
    return parser.parse_args(args)

def execute(func):
    return func(**vars(parse_args(func)))
