#!/usr/bin/python3
def sequence():
    a = 0
    while True:
        a += 1
        yield a


if __name__ == '__main__':
    seq = sequence()

    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
