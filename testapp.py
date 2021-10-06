import os

print(os.getenv('TEST'))


class Test:
    def __init__(self) -> None:
        pass


def test(x_pass):
    pass


if __name__ == "__main__":
    t1 = Test()
    t2 = test()
    print(t1)
    print(t2)
