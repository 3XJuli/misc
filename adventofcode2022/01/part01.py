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
    max_calories = 0
    curr_calories = 0
    for line in data:
        if line:
            curr_calories += int(line)
        else:
            if curr_calories > max_calories:
                max_calories = curr_calories
            curr_calories = 0
    print(max_calories)


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
