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

    total_sum = 0
    for y, line in enumerate(data):
        number_valid = False
        number_str = ""

        for x, ch in enumerate(line):
            if ch.isdigit():
                number_str += ch
                if y < max_y and not (
                    data[y + 1][x] == "." or data[y + 1][x].isdigit()
                ):
                    number_valid = True
                if x < max_x and not (
                    data[y][x + 1] == "." or data[y][x + 1].isdigit()
                ):
                    number_valid = True
                if (
                    y < max_y
                    and x < max_x
                    and not (data[y + 1][x + 1] == "." or data[y + 1][x + 1].isdigit())
                ):
                    number_valid = True
                if (
                    y > 0
                    and x < max_x
                    and not (data[y - 1][x + 1] == "." or data[y - 1][x + 1].isdigit())
                ):
                    number_valid = True
                if y > 0 and not (data[y - 1][x] == "." or data[y - 1][x].isdigit()):
                    number_valid = True
                if (
                    y > 0
                    and x > 0
                    and not (data[y - 1][x - 1] == "." or data[y - 1][x - 1].isdigit())
                ):
                    number_valid = True
                if x > 0 and not (data[y][x - 1] == "." or data[y][x - 1].isdigit()):
                    number_valid = True

                if (
                    x > 0
                    and y < max_y
                    and not (data[y + 1][x - 1] == "." or data[y + 1][x - 1].isdigit())
                ):
                    number_valid = True

            else:
                if number_str and number_valid:
                    total_sum += int(number_str)
                number_str = ""
                number_valid = False
        if number_str and number_valid:
            total_sum += int(number_str)
        number_str = ""
        number_valid = False

    print(total_sum)


def main():
    # global data

    solution()


if __name__ == "__main__":
    main()
