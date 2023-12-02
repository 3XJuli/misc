import math
data = []
INPUT_PATH: str = 'input'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def solution():
    return 0


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
