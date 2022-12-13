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

        if int(leftleft) <= int(rightleft) and int(leftright) >= int(rightright):
            total += 1
        elif int(rightleft) <= int(leftleft) and int(rightright) >= int(leftright):
            total += 1
    print(total)


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
