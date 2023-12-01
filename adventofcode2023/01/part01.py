import math

data = []
INPUT_PATH: str = "input"


def read_data():
    global data
    with open(INPUT_PATH, "r") as f:
        for line in f.readlines():
            data += [line.strip("\n")]


def solution():
    ch_sum = 0
    for line in data:
        line_number_array = []
        for ch in line:
            if 48 <= ord(ch) <= 57:
                line_number_array.append(ch)

        combined = line_number_array[0] + line_number_array[-1]
        ch_sum += int(combined)
    print(ch_sum)


def main():
    read_data()

    # global data

    solution()


if __name__ == "__main__":
    main()
