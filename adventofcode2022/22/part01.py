import math
from pprint import pprint

data = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample1'

with open(INPUT_PATH, 'r') as f:
    for line in f.readlines():
        data += [line.strip('\n')]

pw: str = ''

n: int = 0
m: int = len(data) - 2
for ix, line in enumerate(data):
    if ix == len(data) - 1:
        pw = line
    else:
        if line and len(line) >= n:
            n = len(line)

grid = [[' ' for _ in range(n)] for _ in range(m)]

for y, line in enumerate(data[:m]):
    for x, ch in enumerate(line):
        grid[y][x] = ch

start_point: tuple[int, int] = [(x, 0) for x, ch in enumerate(grid[0]) if ch == '.'][0]
print(start_point)


def _cout():
    global grid
    for x in grid:
        print(''.join(x))


_cout()


def get_step_size(direction: int) -> tuple[int, int]:
    match direction:
        case 0:
            return 1, 0
        case 1:
            return 0, 1
        case 2:
            return -1, 0
        case 3:
            return 0, -1
        case _:
            assert False


def move(curr_position: tuple[int, int], step_size: tuple[int, int], steps: int) -> tuple[int, int]:
    curr_step = steps
    while curr_step > 0:
        new_x, new_y = (curr_position[0] + step_size[0]) % n, (curr_position[1] + step_size[1]) % m
        while grid[new_y][new_x] == ' ':
            new_x, new_y = (new_x + step_size[0]) % n, (new_y + step_size[1]) % m

        if grid[new_y][new_x] == '.':
            curr_position = new_x, new_y
            curr_step -= 1
        else:
            return curr_position[0], curr_position[1]
    return curr_position[0], curr_position[1]


def solution():
    global n, m, grid, pw, start_point

    # 0 = r, 1 = d, 2 = l, 3 = u
    direction: int = 0
    curr_position: tuple[int, int] = start_point
    i = 0
    while i < len(pw):
        ch = pw[i]
        if ch == 'R':
            direction = (direction + 1) % 4
            i += 1
        elif ch == 'L':
            direction = (direction - 1) % 4
            i += 1
        else:
            number_str = ''
            while i < len(pw) and pw[i] != 'L' and pw[i] != 'R':
                number_str += pw[i]
                i += 1
            steps: int = int(number_str)
            step_size = get_step_size(direction)
            curr_position = move(curr_position, step_size, steps)

    result = 1000 * (curr_position[1] + 1) + 4 * (curr_position[0] + 1) + direction
    print(result)


def main():
    solution()


if __name__ == '__main__':
    main()
