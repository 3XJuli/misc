import math
data = []
INPUT_PATH: str = 'input'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def solution():
    global data
    data = data[0]

    moving_window = data[:4]

    for ix, c in enumerate(data):
        if len(set(moving_window)) == 4:
            print(ix)
            return

        moving_window = moving_window[1:] + "" + c
        print(moving_window)

def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
