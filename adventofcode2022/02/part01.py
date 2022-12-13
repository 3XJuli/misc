import math

data = []
INPUT_PATH: str = 'input'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def calcScore(left: str, right: str) -> int:
    left = ord(left) - 64
    right = ord(right) - 87

    # LeftBeats = ((left + 1) % 3) + 1
    left_looses = ((left - 6) % 3) + 1

    if left == right:
        return right + 3
    elif right == left_looses:
        return right + 6
    return right


def solution():
    score = 0
    for line in data:
        score += calcScore(line[0], line[2])

    print(score)


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
