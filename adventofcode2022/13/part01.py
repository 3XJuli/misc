import math
from typing import Optional

data = []
INPUT_PATH: str = 'input'


# INPUT_PATH: str = 'sample1'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def parse():
    i = 0
    arr = []
    b = False
    while i < len(data):
        if data[i]:
            arr.append((eval(data[i]), eval(data[i + 1])))
            i += 2
        else:
            i += 1
    return arr


def solve(l: list, r: list, depth=0) -> Optional[bool]:
    ix = 0
    while ix < min(len(l), len(r)):
        l_entry = l[ix]
        r_entry = r[ix]

        # int - list => list - list
        if type(l_entry) == int and type(r_entry) == list:
            l_entry = [l_entry]
        # list - int => list - list
        elif type(l_entry) == list and type(r_entry) == int:
            r_entry = [r_entry]
        # int - int
        if type(l_entry) == int:
            if l_entry < r_entry:
                return True
            if l_entry > r_entry:
                return False
        # list - list
        elif type(l_entry) == list:
            rec = solve(l_entry, r_entry, depth=depth + 1)
            if rec is not None:
                return rec
        else:
            assert False

        ix += 1

    if len(l) < len(r):
        return True
    elif len(l) > len(r):
        return False
    else:
        if depth == 0:
            assert False


def solution():
    arr = parse()
    total = 0
    print(arr)
    for ix, prob in enumerate(arr, start=1):
        if ix == 4:
            print('debug')
        total += ix if solve(prob[0], prob[1]) else 0
        print(total)
    print(total)


def main():
    read_data()
    # global data

    solution()


if __name__ == '__main__':
    main()
