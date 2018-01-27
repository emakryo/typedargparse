import argparse

def execute(func):
    annotations = func.__annotations__
    parser = argparse.ArgumentParser()
    for arg_name in func.__code__.co_varnames:
        parser.add_argument(arg_name)
    func(**vars(parser.parse_args()))
