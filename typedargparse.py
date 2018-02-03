import argparse

def generate_parser(func):
    annotations = func.__annotations__
    parser = argparse.ArgumentParser()
    arg_names = func.__code__.co_varnames
    default_values = func.__defaults__
    for i, name in enumerate(arg_names):
        param = {}

        if name in annotations:
            param['type'] = annotations[name]
        else:
            param['type'] = str

        if default_values and i >= len(arg_names) - len(default_values):
            name = "--" + name
            param['default'] = default_values[i-len(arg_names)+len(default_values)]
        else:
            param['default'] = None

        if param['type'] == bool:
            if name[0:2] != "--":
                name = "--" + name

            if param['default'] == False:
                param['action'] = 'store_false'
            else:
                param['action'] = 'store_true'

            del param['type']
            del param['default']

        else:
            param['action'] = 'store'

        parser.add_argument(name, **param)
    return parser

def parse_args(func, args=None):
    parser = generate_parser(func)
    return parser.parse_args(args)

def execute(func):
    return func(**vars(parse_args(func)))
