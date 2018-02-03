import typedargparse


def main(num: int):
    print(num + 1)

if __name__ == "__main__":
    typedargparse.execute(main)
