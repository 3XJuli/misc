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
    elves_counter = 0
    curr_set: set = set()
    total = 0
    for line in data:
        if not elves_counter:
            curr_set = set(Counter(line).keys())
            elves_counter += 1
        elif elves_counter == 1:
            curr_set = curr_set.intersection(set(Counter(line).keys()))
            elves_counter += 1
        else:
            badge: str = curr_set.intersection(set(Counter(line).keys())).pop()
            if badge.islower():
                total += ord(badge) - 96
            else:
                total += ord(badge) - 38
            elves_counter = 0

    print(total)


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
