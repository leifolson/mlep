import os


def do_dummy() -> str:
    return 'ran dummy'


if __name__ == '__main__':
    print(os.listdir())
else:
    do_dummy()
