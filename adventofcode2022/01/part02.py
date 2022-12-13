import math

data = []
INPUT_PATH: str = 'input'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


def push_back(top_elves: list, new_value):
    for i in range(1, 3):
        if top_elves[i] <= new_value:
            top_elves[i - 1] = top_elves[i]
            top_elves[i] = new_value
        else:
            top_elves[i - 1] = new_value
            break

    return top_elves, top_elves[0]


def solution():
    global data
    top_elves: list = [0] * 3
    min_calories = 0
    curr_calories = 0
    for line in data:
        if line:
            curr_calories += int(line)
        else:
            if curr_calories > min_calories:
                top_elves, min_calories = push_back(top_elves, curr_calories)
            curr_calories = 0
    print(top_elves)
    print(sum(top_elves))


def main():
    read_data()

    # global data

    solution()


if __name__ == '__main__':
    main()
