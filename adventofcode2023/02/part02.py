import math
from functools import reduce
import re
import operator

data = []
INPUT_PATH: str = "input"
INPUT_PATH: str = "debug_input"


with open(INPUT_PATH, "r") as f:
    for line in f.readlines():
        data += [line.strip("\n")]


colors = ["red", "green", "blue"]


def game(game_data) -> int:
    color_max = [0, 0, 0]
    for sub_game in game_data.split("; "):
        sub_colors = sub_game.split(", ")
        for sub_color in sub_colors:
            n, actual_color = sub_color.split()
            for i, color in enumerate(colors):
                if actual_color.endswith(color):
                    color_max[i] = max(color_max[i], int(n))
    return reduce(operator.mul, color_max)


def solution():
    out = 0
    for line in data:
        game_data = line.split(": ")[1]
        out += game(game_data)

    print(out)


def main():
    solution()


if __name__ == "__main__":
    main()
