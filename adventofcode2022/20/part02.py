import math

data = []
INPUT_PATH: str = 'input'
n: int = 5000
# INPUT_PATH: str = 'sample1'
# n: int = 7


value_to_order: dict[int, int] = {}

index_and_value_to_original: dict[tuple[int, int], int] = {}

original_and_value_to_index: dict[tuple[int, int], int] = {}

zero_org_pos: int = 0
original_data = []

# definitely a lot of overhead after looking at solutions.
# we really don't need to move everything everytime as I did explicitely
# its enough to del the current ix and add the new one (this makes moving easy)

with open(INPUT_PATH, 'r') as f:
    for k, line in enumerate(f.readlines()):
        val = int(line.strip()) * 811589153
        data.append(val)
        if val in value_to_order:
            assert False

        if val == 0:
            zero_org_pos = k
        index_and_value_to_original[k, val] = k
        original_and_value_to_index[k, val] = k
    original_data = data.copy()


def get_grove_coordinates():
    global zero_org_pos

    total = 0
    ix = original_and_value_to_index[zero_org_pos, 0]

    for i, x in enumerate([1000] * 3, start=1):
        total += data[(ix + i * x) % n]
        # print(data[(ix + i * x) % n])
    print(total)


def solution():
    # print(data)
    for _ in range(10):
        for orig_ix, dat in enumerate(original_data):
            curr_ix = original_and_value_to_index[orig_ix, dat]
            new_position: int = (curr_ix + dat) % (n - 1)

            if new_position <= curr_ix:
                for j in range(curr_ix, new_position, -1):
                    data[j] = data[j - 1]
                    index_and_value_to_original[j, data[j]] = index_and_value_to_original[j - 1, data[j - 1]]
                    original_and_value_to_index[index_and_value_to_original[j, data[j]], data[j]] = j
            else:
                for j in range(curr_ix, new_position):
                    data[j] = data[j + 1]
                    index_and_value_to_original[j, data[j]] = index_and_value_to_original[j + 1, data[j + 1]]
                    original_and_value_to_index[index_and_value_to_original[j, data[j]], data[j]] = j

            data[new_position] = dat
            index_and_value_to_original[new_position, dat] = orig_ix
            original_and_value_to_index[orig_ix, dat] = new_position
    get_grove_coordinates()


if __name__ == '__main__':
    solution()
