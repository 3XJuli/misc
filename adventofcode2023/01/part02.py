import math

data = []
INPUT_PATH: str = "input"


def read_data():
    global data
    with open(INPUT_PATH, "r") as f:
        for line in f.readlines():
            data += [line.strip("\n")]


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solution():
    ch_sum = 0
    for line in data:
        line_number_array = []
        current_viable_numbers = {}
        for ch in line:
            if 48 <= ord(ch) <= 57:
                line_number_array.append(ch)
            new_current_viable_numbers = {}
            for number_str, int_number in (numbers | current_viable_numbers).items():
                if ch == number_str[0]:
                    if len(number_str) == 1:
                        line_number_array.append(str(int_number))
                        continue
                    new_current_viable_numbers[number_str[1:]] = int_number
            current_viable_numbers = new_current_viable_numbers

        combined = line_number_array[0] + line_number_array[-1]
        ch_sum += int(combined)
    print(ch_sum)


def main():
    read_data()

    # global data

    solution()


if __name__ == "__main__":
    main()
