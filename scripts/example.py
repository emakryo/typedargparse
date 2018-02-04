import typing
from typedargparse import execute

def main(nums: typing.List[int], mean: bool):
    if mean:
        print(sum(nums)/len(nums))
    else:
        print(sum(nums))

if __name__ == "__main__":
    execute(main)
