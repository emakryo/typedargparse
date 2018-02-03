import typing
import argparse


def generate_parser(func):
    annotations = func.__annotations__
    parser = argparse.ArgumentParser()
    arg_names = func.__code__.co_varnames
    default_values = func.__defaults__

    if default_values:
        n_positional = len(arg_names) - len(default_values)
    else:
        n_positional = len(arg_names)

    for i, name in enumerate(arg_names):
        if name in annotations:
            annotation = annotations[name]
        else:
            annotation = str

        if i >= n_positional:
            optional = True
            default = default_values[i-n_positional]
        else:
            optional = False
            default = None

        name, param = parse_params(name, annotation, optional, default)
        parser.add_argument(name, **param)

    return parser


def parse_params(name, annotation, optional, default):
    param = {}

    if optional:
        name = '--' + name

    if annotation == bool:
        if not optional:
            name = "--" + name

        if default == False:
            param['action'] = 'store_false'
        else:
            param['action'] = 'store_true'

    elif is_variable_length_type(annotation):
        param['type'] = annotation.__args__[0]
        param['nargs'] = '*'
        param['default'] = default

    else:
        param['type'] = annotation
        param['action'] = 'store'
        param['default'] = default

    return name, param


def is_variable_length_type(t):
    return (hasattr(t, "__origin__") and
            t.__origin__ in (typing.List, typing.Sequence))


def parse_args(func, args=None):
    parser = generate_parser(func)
    return parser.parse_args(args)


def execute(func):
    return func(**vars(parse_args(func)))
