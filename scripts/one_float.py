import typedargparse


def main(num: float):
    print(num + 1)

if __name__ == "__main__":
    typedargparse.execute(main)
