import math
data = []
INPUT_PATH: str = 'input'
n: int = 5000
# INPUT_PATH: str = 'sample'
# n: int = 7


value_to_order: dict[int, int] = {}

index_and_value_to_original: dict[tuple[int, int], int] = {}

original_and_value_to_index: dict[tuple[int, int], int] = {}

zero_org_pos: int = 0
original_data = []

with open(INPUT_PATH, 'r') as f:
    for k, line in enumerate(f.readlines()):
        val = int(line.strip())
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
        total += data[(ix + i*x) % n]
        print(data[(ix + i*x) % n])
    print(total)

def solution():
    for orig_ix, val in enumerate(original_data[:]):
        curr_ix = original_and_value_to_index[orig_ix, val]
        dat = data[curr_ix]
        if dat != val:
            assert False

        new_position: int
        if dat < 0:
            if curr_ix + dat <= 0:
                # new_position = (ix + dat) % n + (ix + dat - 1) // n # we wrap around at least once, but maybe multiple times
                new_position = (curr_ix + dat  + (curr_ix + dat - 1) // n) % n # we wrap around at least once, but maybe multiple times
                wrap_around = True
            else:
                new_position = curr_ix + dat
        else:
            if curr_ix + dat >= n:
                new_position = ((curr_ix + dat ) % n + (curr_ix + dat) // n) % n
                wrap_around = True
            else:
                new_position = curr_ix + dat

        if new_position <= curr_ix:
            # shift right
            for j in range(curr_ix, new_position, -1):
                data[j] = data[j - 1]
                # if indices[value_to_order[data[j - 1]]] >= n:
                #     print('debug')
                # indices[value_to_order[data[j - 1]]] += 1
                # indices[j] -= 1
                index_and_value_to_original[j, data[j]] = index_and_value_to_original[j-1, data[j-1]]
                j_org_ix = index_and_value_to_original[j, data[j]]
                original_and_value_to_index[j_org_ix, data[j]] = j
                # index_and_value_to_original[j, data[j]] = index_and_value_to_original[j - 1, data[j - 1]] - 1
        else:
            # shift left
            for j in range(curr_ix, new_position):
                data[j] = data[j+1]
                index_and_value_to_original[j, data[j]] = index_and_value_to_original[j + 1, data[j + 1]]
                j_org_ix = index_and_value_to_original[j, data[j]]
                original_and_value_to_index[j_org_ix, data[j]] = j

        data[new_position] = dat
        index_and_value_to_original[new_position, dat] = orig_ix
        original_and_value_to_index[orig_ix, dat] = new_position
        # print(data)
    get_grove_coordinates()















if __name__ == '__main__':
    solution()
