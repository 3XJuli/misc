import math
from typing import Optional
from pprint import pprint

data = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample2'
rounds: int = 10

with open(INPUT_PATH, 'r') as f:
    for line in reversed(f.readlines()):
        data += [line.strip('\n')]

elves: dict[tuple[int, int], tuple[int, int]] = dict()

direction_queue: list = ['N', 'S', 'W', 'E']

for y, line in enumerate(data):
    for x, ch in enumerate(line):
        if ch == '#':
            elves[x, y] = (x, y)


def check_direction(x: int, y: int, direction: str, directions: tuple[int, ...]) -> \
        Optional[tuple[int, int]]:
    match direction:
        case 'N':
            return (x, y + 1) if sum(directions[0:3]) == 3 else None
        case 'S':
            return (x, y - 1) if sum(directions[4:7]) == 3 else None
        case 'W':
            return (x - 1, y) if (directions[6] and directions[7] and directions[0]) else None
        case 'E':
            return (x + 1, y) if sum(directions[2:5]) == 3 else None
        case _:
            assert False


# def propagate_block():
#     pass

def new_spot(direction):
    pass


# NW / N / NE / E / SE / S / SW / W
def check_directions(x: int, y: int) -> tuple[int, ...]:
    global elves
    dirs = [1] * 8
    j = 0
    for i in (1, -1):
        if (x - i, y + i) in elves:
            dirs[j] = 0
        j += 1
        if (x, y + i) in elves:
            dirs[j] = 0
        j += 1
        if (x + i, y + i) in elves:
            dirs[j] = 0
        j += 1
        if (x + i, y) in elves:
            dirs[j] = 0
        j += 1
    return tuple(dirs)

def _cout(r = 0):
    min_x = min_y = math.inf
    max_x = max_y = -math.inf
    global elves
    for elf_x, elf_y in elves.keys():
        min_x = min(elf_x, min_x)
        min_y = min(elf_y, min_y)
        max_x = max(elf_x, max_x)
        max_y = max(elf_y, max_y)

    grid = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for elf_x, elf_y in elves.keys():
        grid[elf_y - min_y][elf_x - min_x] = '#'
    print(f'--------- Round: {r} ------------')
    for row in reversed(grid):
        line = ''
        for x in row:
            line += x
        print(line)
    print('--------------------------')


def solution():
    global elves
    min_x = min_y = math.inf
    max_x = max_y = -math.inf
    for r in range(rounds):
        proposed_spots: set[tuple[int, int]] = set()
        blocked_spots: set[tuple[int, int]] = set()
        proposed_spot_to_elf: dict[tuple[int, int], tuple[int, int]] = dict()
        for elf_x, elf_y in elves.keys():
            directions = check_directions(elf_x, elf_y)
            if sum(directions) == 8:
                continue
            for direction in direction_queue:
                if prop_spot := check_direction(elf_x, elf_y, direction, directions):
                    if prop_spot in proposed_spots:
                        blocked_spots.add(prop_spot)
                        blocked_spots.add((elf_x, elf_y))
                        earlier_elf = proposed_spot_to_elf[prop_spot]
                        blocked_spots.add(proposed_spot_to_elf[prop_spot])
                        elves[earlier_elf] = earlier_elf

                        break
                    elves[elf_x, elf_y] = prop_spot
                    proposed_spots.add(prop_spot)
                    proposed_spot_to_elf[prop_spot] = (elf_x, elf_y)
                    break
        new_elves: dict[tuple[int, int], tuple[int, int]] = dict()
        for original_elf_pos, new_elf_pos in elves.items():
            new_elves[new_elf_pos] = new_elf_pos
        if len(new_elves) < len(elves):
            assert False
        elves = new_elves
        new_last = direction_queue.pop(0)
        direction_queue.append(new_last)
    for elf_x, elf_y in elves.keys():
        min_x = min(elf_x, min_x)
        min_y = min(elf_y, min_y)
        max_x = max(elf_x, max_x)
        max_y = max(elf_y, max_y)


    rectangle_area = (max_x - min_x + 1) * (max_y - min_y + 1)
    print(rectangle_area - len(elves))


def main():
    # global data

    solution()


if __name__ == '__main__':
    main()
