import math

import re

data = []
INPUT_PATH: str = "debug_input"
INPUT_PATH: str = "input"


with open(INPUT_PATH, "r") as f:
    for line in f.readlines():
        data += [line.strip("\n")]


colors = {"red": 12, "green": 13, "blue": 14}


def game(game_data) -> bool:
    for sub_game in game_data.split("; "):
        sub_colors = sub_game.split(", ")
        for sub_color in sub_colors:
            n, actual_color = sub_color.split()
            for i, (color, max_color) in enumerate(colors.items()):
                if actual_color.endswith(color):
                    if int(n) > int(max_color):
                        return False
    return True


def solution():
    out = 0
    for i, line in enumerate(data):
        game_id = i + 1
        game_data = line.split(": ")[1]
        if game(game_data):
            out += game_id
    print(out)


def main():
    # global data

    solution()


if __name__ == "__main__":
    main()
