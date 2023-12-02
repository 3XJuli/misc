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
            arr.append(eval(data[i]))
            arr.append(eval(data[i + 1]))
            i += 2
        else:
            i += 1
    return arr


def sorted(l: list, r: list, depth=0) -> Optional[bool]:
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
            rec = sorted(l_entry, r_entry, depth=depth + 1)
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


def merge(left: list, right: list):
    result = []
    while left and right:
        if sorted(left[0], right[0]):
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    if left:
        result = result + left
    if right:
        result = result + right
    return result


def merge_sort(arr: list):
    n = len(arr)
    if n <= 1:
        return arr
    left = []
    right = []

    for i, pair in enumerate(arr):
        if i < n // 2:
            left.append(pair)
        else:
            right.append(pair)
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def solution():
    arr = parse()
    arr.append([[2]])
    arr.append([[6]])
    res = merge_sort(arr)
    total = 1
    for ix, packet in enumerate(res, start=1):
        if packet == [[2]] or packet == [[6]]:
            total *= ix
    print(total)


def main():
    read_data()
    # global data

    solution()


if __name__ == '__main__':
    main()
