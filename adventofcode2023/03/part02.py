from collections import defaultdict

data = []
INPUT_PATH: str = "input"
# INPUT_PATH: str = "debug_input"


with open(INPUT_PATH, "r") as f:
    for line in f.readlines():
        data += [line.strip("\n")]


pattern: str = r"(\d+)"


def solution():
    max_y = len(data) - 1
    max_x = len(data[0]) - 1

    total_sum: int = 0

    gears = defaultdict(list)

    for y, line in enumerate(data):
        number_str = ""
        number_gears = set()

        for x, ch in enumerate(line):
            if ch.isdigit():
                number_str += ch
                if y < max_y and (data[y + 1][x] == "*"):
                    number_gears.add((y + 1, x))
                if x < max_x and (data[y][x + 1] == "*"):
                    number_gears.add((y, x + 1))
                if y < max_y and x < max_x and (data[y + 1][x + 1] == "*"):
                    number_gears.add((y + 1, x + 1))
                if y > 0 and x < max_x and (data[y - 1][x + 1] == "*"):
                    number_gears.add((y - 1, x + 1))
                if y > 0 and (data[y - 1][x] == "*"):
                    number_gears.add((y - 1, x))
                if y > 0 and x > 0 and (data[y - 1][x - 1] == "*"):
                    number_gears.add((y - 1, x - 1))
                if x > 0 and (data[y][x - 1] == "*"):
                    number_gears.add((y, x - 1))
                if x > 0 and y < max_y and (data[y + 1][x - 1] == "*"):
                    number_gears.add((y + 1, x - 1))

            else:
                if number_gears:
                    for gear in number_gears:
                        gears[gear].append(int(number_str))
                number_str = ""
                number_gears = set()
        if number_gears:
            for gear in number_gears:
                gears[gear].append(int(number_str))
        number_str = ""

    for gear, numbers in gears.items():
        if len(numbers) == 2:
            total_sum += numbers[0] * numbers[1]

    print(total_sum)


def main():
    # global data

    solution()


if __name__ == "__main__":
    main()
