# typedargparse

Simple wrapper for argparse.
This module automatically generate parser from type-annotated function and execute.

## Requirements

* python >= 3.5

## Example

```python
# example.py
import typing
from typedargparse import execute

def main(nums: typing.List[int], mean: bool):
    if mean:
        print(sum(nums)/len(nums))
    else:
        print(sum(nums))

if __name__ == "__main__":
    execute(main)
```

This script `example.py` takes an option `--mean` and an arbitrary number of arguments.
Therefore, it is executed as follows:

```
$ python example.py 1 2 3
6
$ python example.py --mean 2 3 4
3.0
```

## Supported annotation

### callable (`int`, `str`, etc.)

Arguments are converted by callable. (default: `str`)

### `bool`

Note that `bool` annotation behave in a different way than other callable annotations.
Boolean arguments are treated as *flag*, i.e. they do not take any optional values.
Positional arguments annotated with `bool` is treated as
optional arguments with default value `False`.
The value is set as follows:

|default value| With flag | Without flag |
|-------------|---------- |--------------|
| `True`      | `False`   | `True`       |
| `False`     | `True`    | `False`      |

### `typing.List`, `typing.Sequence`

Multiple arguments can be parsed by `typing.List` or `typing.Sequence`.
Each argument is converted by the argument of the generic type annotation.


## Development

### Install

```
$ python setup.py develop
```

### Test

```
$ python -m unittest tests
```

### Uninstall

```
$ python setup.py develop --uninstall
```
