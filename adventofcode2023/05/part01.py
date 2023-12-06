import math

data = []
INPUT_PATH: str = "input"
# INPUT_PATH: str = "debug_input"


with open(INPUT_PATH, "r") as f:
    for line in f.readlines():
        data += [line.strip("\n")]


def get_new_seed(seed, map_range):
    for current_range in map_range:
        if current_range[1] <= seed <= (current_range[1] + current_range[2]):
            new_seed = current_range[0] + (seed - current_range[1])
            return new_seed
    return seed


def solution():
    seeds = list(map(int, data[0].split(": ")[1].split()))
    ranges = []
    current_ranges = []
    for line in data[2:]:
        if not len(line):
            ranges.append(current_ranges)
            current_ranges = []
        elif not line[0].isdigit():
            continue
        else:
            range_tuple = list(map(int, line.split()))
            current_ranges.append(range_tuple)

    new_seeds = []
    for map_range in ranges:
        for seed in seeds:
            new_seed = get_new_seed(seed, map_range)
            new_seeds.append(new_seed)
        seeds = new_seeds
        new_seeds = []

    print(min(seeds))


def main():
    # global data

    solution()


if __name__ == "__main__":
    main()
