import math
from pprint import pprint

data = []
INPUT_PATH: str = 'input'
dimension: int = 50
# INPUT_PATH: str = 'sample1'
# dimension: int = 50

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


def manhatten_distance(x1: int, y1: int, x2: int, y2: int):
    return abs(x1 - x2) + abs(y1 - y2)


# def rotate_90_degree():


# connected_cubes: top, right, down, left
class Side(object):
    def __init__(self, grid: list[list[str]], id: int, x: int, y: int):
        self.grid = grid
        self.x = x
        self.y = y
        self.id = id

    def __post_init__(self):
        self.connected_cubes = [-1] * 4
        if self.id == 0:
                    # x, y, z
            self.a = (0, 0, 1)
            self.b = 0
            self.r = (1, 0)
            self.l = (-1, 0)
            self.u = (0, 1)
            self.d = (0, -1)
        else:
            self.determine_sides()

    def determine_sides(self):
        for side in sides:
            if side.id == self.id:
                continue
            if manhatten_distance(side.x, side.y, self.x, self.y) == 1:
                if self.x > side.x:
                    if sum(self.connected_cubes) == -4:
                        self.r = side.r
                    if side.id == 0:
                        side.
                    self.connected_cubes[] = side.id
                    side.connected_cubes[3] = self.id
                elif self.y >  side.y:
                    if sum(self.connected_cubes) == -4:
                        ...
                    self.connected_cubes[0] = side.id
                    side.connected_cubes[2] = self.id
                else:
                    assert False



    def __hash__(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)


#    1
#  4 0 2
#    3
#    5
sides: list[Side, Side, Side, Side, Side, Side] = list()

grid = [[' ' for _ in range(n)] for _ in range(m)]

grids = [[[['' for _ in range(dimension)] for _ in range(dimension)] for _ in range(n // dimension)] for _ in
         range(m // dimension)]

for y, line in enumerate(data[:m]):
    for x, ch in enumerate(line):
        if ch != ' ':
            grid = grids[y // dimension][x // dimension]
            grid[y % dimension][x % dimension] = ch

start_point: tuple[int, int] = [(x, 0) for x, ch in enumerate(grid[0]) if ch == '.'][0]


def _cout_grids():
    global grids
    for y in range(len(grids)):
        for x in range(len(grids[0])):
            if grids[y][x][0][0]:
                print('1', end=' ')
            else:
                print('0', end=' ')
        print('')


ix = 0
for y in range(len(grids)):
    for x in range(len(grids[0])):
        if grids[y][x][0][0]:
            side = Side(grids[y][x], ix, x, y)
            ix += 1


def _cout():
    global sides

    for x in grid:
        print(''.join(x))


# _cout()


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
