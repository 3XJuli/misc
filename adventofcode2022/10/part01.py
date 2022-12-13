import math

data = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def solution():
    c = 20
    ix = 0
    total = 0
    X = 1
    skip = False
    for line in data:
        if not skip:
            if ix > 220:
                return total
            if ix % 40 == 20:
                total += ix * X
        skip = False

        addx = line[:4] == 'addx'
        if addx:

            for i in range(2):
                ix += 1
                if ix > 220:
                    return total
                if ix % 40 == 20:
                    total += ix * X
            skip = True
            X = X + int(line[5:])
        else:
            ix += 1
    return total


def main():
    read_data()

    # global data

    y = solution()
    print(y)

if __name__ == '__main__':
    main()
