import math

from operator import add
from functools import reduce

data = []
INPUT_PATH: str = "input"
# INPUT_PATH: str = "input_debug"


with open(INPUT_PATH, "r") as f:
    for i, line in enumerate(f.readlines()):
        effective_data = line.strip("\n").split(":")[1].split(" ")
        effective_data = [spl for spl in effective_data if spl != ""]

        data.append(int(reduce(add, effective_data)))


def solution():
    out = 1

    total_time = data[0]
    record_distance = data[1]
    number_options = 0
    for pressed_time in range(total_time):
        potential_distance = (total_time - pressed_time) * (pressed_time)
        if potential_distance > record_distance:
            number_options += 1
    out *= number_options
    print(out)


def main():
    solution()


if __name__ == "__main__":
    main()
