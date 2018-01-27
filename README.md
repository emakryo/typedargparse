# typedargparse

Simple wrapper for argparse.
This module automatically generate parser from type-annotated function.

## Requirements

* python >= 3.5

## Usage

```
# test.py
from typedargparse import execute

def main(text: str, x: int=10, option:bool=False):
    if option:
        print(txt)
    else:
        print(x + 3)


if __name__ == "__main__":
    execute(main)
```

This script `test.py` takes options `--text`, `--x`, `--option`.
Therefore, it is executed by

```
$ python test.py --text foo --x 20 --option
```

## Development

### Install

```
$ python setup.py develop
```

### Test

```
$ cd tests; python -m unittest
```

### Uninstall

```
$ python setup.py develop --uninstall
```
