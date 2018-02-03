import argparse

def generate_parser(func):
    annotations = func.__annotations__
    parser = argparse.ArgumentParser()
    arg_names = func.__code__.co_varnames
    default_values = func.__defaults__
    for i, name in enumerate(arg_names):
        if name in annotations:
            arg_type = annotations[name]
        else:
            arg_type = str

        if default_values and i >= len(arg_names) - len(default_values):
            name = "--" + name
            default = default_values[i-len(arg_names)+len(default_values)]
        else:
            default = None
        parser.add_argument(name, type=arg_type, default=default)
    return parser

def parse_args(func, args=None):
    parser = generate_parser(func)
    return parser.parse_args(args)

def execute(func):
    return func(**vars(parse_args(func)))
