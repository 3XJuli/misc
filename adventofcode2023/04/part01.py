import math

data = []
INPUT_PATH: str = "input"
# INPUT_PATH: str = "debug_input"


with open(INPUT_PATH, "r") as f:
    for line in f.readlines():
        data += [line.strip("\n")]


def solution():
    out = 0
    for _, line in enumerate(data):
        card_data = line.split(": ")[1]
        winning_numbers_raw, my_numbers_raw = card_data.split(" | ")

        winning_numbers = set(winning_numbers_raw.split())

        my_numbers = list(my_numbers_raw.split())

        worth = 0
        for number in my_numbers:
            if number in winning_numbers:
                worth = max(worth * 2, 1)
        out += worth

    print(out)


def main():
    # global data

    solution()


if __name__ == "__main__":
    main()
