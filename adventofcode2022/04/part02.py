import math
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
        line = line.split(',')
        leftleft, leftright = line[0].split('-')
        rightleft, rightright = line[1].split('-')

        leftset = set(range(int(leftleft), int(leftright)+1))
        rightset = set(range(int(rightleft), int(rightright)+1))

        if leftset.intersection(rightset):
            total += 1

    print(total)


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
