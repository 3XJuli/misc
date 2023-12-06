import math

data = []
INPUT_PATH: str = "input"
# INPUT_PATH: str = "input_debug"


with open(INPUT_PATH, "r") as f:
    for i, line in enumerate(f.readlines()):
        effective_data = line.strip("\n").split(":")[1].split(" ")
        effective_data = [int(spl) for spl in effective_data if spl != ""]

        data.append(effective_data)


def solution():
    times = data[0]
    distances = data[1]

    out = 1

    for i, total_time in enumerate(times):
        record_distance = distances[i]
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
