import typedargparse

def main(text: str, x: int=10, option:bool=False):
    if option:
        print(text)
    else:
        print(x + 3)

if __name__ == "__main__":
    typedargparse.execute(main)
