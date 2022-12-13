import math
from collections import Counter
data = []
INPUT_PATH: str = 'input'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def solution():
    total = 0
    for line in data:
        if len(line) % 2:
            assert False
        leftText = line[:(len(line)//2)]
        rightText = line[len(line)//2:]

        leftCount = set(Counter(leftText).keys())
        rightCount  = set(Counter(rightText).keys())

        intersection: str = leftCount.intersection(rightCount).pop()
        if intersection.islower():
            total += ord(intersection) - 96
        else:
            total += ord(intersection) - 38
    print(total)





def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
