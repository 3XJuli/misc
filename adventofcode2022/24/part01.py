import dataclasses
import math
from pprint import pprint
import sys

sys.setrecursionlimit(10000)

data = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample'
# INPUT_PATH: str = 'sample2'

with open(INPUT_PATH, 'r') as f:
    for line in f.readlines():
        data += [line.strip('\n')]

m = len(data)
n = len(data[0])
grid: list[list[list[str]]] = [[list() for _ in range(n)] for _ in range(m)]
for y, line in enumerate(data):
    for x, ch in enumerate(line):
        if ch != '.':
            grid[y][x] = [ch]

# x, y
start = (1, 0)



def _cout(no_grid: int = 0):
    global grid, grids

    if no_grid == 0:
        curr_grid = grid
    else:
        curr_grid = grids[no_grid]
    print(f'--------------------------')
    for row in curr_grid:
        line = ''
        for x in row:
            if len(x) > 1:
                line += str(len(x))
            elif x:
                line += x[0]
            else:
                line += '.'
        print(line)
    print('--------------------------')


grids: list[list[list[list[str]]]] = list()


def calculate_grids():
    global grid, grids, n, m
    old_grid: list[list[list[str]]] = grid
    ix = 0
    while ix == 0 or old_grid != grid:
        grids.append(old_grid)
        new_grid: list[list[list[str]]] = [[list() for _ in range(n)] for _ in range(m)]
        for y, row in enumerate(old_grid):
            for x, chars in enumerate(row):
                for char in chars:
                    try:
                        match char:
                            case 'v':
                                new_grid[y + 1][x].append('v') if old_grid[y + 1][x] != ['#'] else new_grid[1][
                                    x].append(
                                    'v')
                            case '>':
                                new_grid[y][x + 1].append('>') if old_grid[y][x + 1] != ['#'] else new_grid[y][
                                    1].append(
                                    '>')
                            case '<':
                                new_grid[y][x - 1].append('<') if old_grid[y][x - 1] != ['#'] else new_grid[y][
                                    n - 2].append('<')
                            case '^':
                                new_grid[y - 1][x].append('^') if old_grid[y - 1][x] != ['#'] else new_grid[m - 2][
                                    x].append('^')
                            case '#':
                                new_grid[y][x].append('#')
                            case '_':
                                assert False
                    except IndexError:
                        print('debug')
        old_grid = new_grid
        ix += 1


def states():
    pass


global_min: int = math.inf
total_grids: int

cache_line: dict[tuple[int, int, int], int] = dict()


def manhatten_dist(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def create_states(minute: int, x: int, y: int, goal_x: int, goal_y: int, wait: int = 0):
    global grids, total_grids, global_min, cache_line
    # print(x, y, minute)

    if (x, y, minute) in cache_line:
        return cache_line[x, y, minute]

    if manhatten_dist(x, y, goal_x, goal_y) + minute >= global_min:
        return 0

    # no infinite waiting
    if wait == total_grids:
        return 0

    if x == goal_x and y == goal_y:
        return minute-1

    if minute >= 3000:
        return 0

    curr_grid = grids[minute % len(grids)]

    min_value: int = math.inf

    # move up
    if y - 1 >= 0 and not curr_grid[y - 1][x] and (val := create_states(minute + 1, x, y - 1, goal_x, goal_y)):
        min_value = min(min_value, val)
    # move right
    if not curr_grid[y][x + 1] and (val := create_states(minute + 1, x + 1, y, goal_x, goal_y)):
        min_value = min(min_value, val)
    # move left
    if not curr_grid[y][x - 1] and (val := create_states(minute + 1, x - 1, y, goal_x, goal_y)):
        min_value = min(min_value, val)
    # move down
    if y + 1 < m and not curr_grid[y + 1][x] and (val := create_states(minute + 1, x, y + 1, goal_x, goal_y)):
        min_value = min(min_value, val)
    # do nothing
    if not curr_grid[y][x] and (val := create_states(minute + 1, x, y, goal_x, goal_y, wait + 1)):
        min_value = min(min_value, val)
    cache_line[x, y, minute] = min_value

    global_min = min(min_value, global_min)

    return min_value

    # check_right


def solution():
    global start, total_grids, cache_line, global_min
    print(len(grids))
    total_grids = len(grids)
    goal_x = n - 2
    goal_y = m - 1
    min_0 = create_states(0, 1, 0, goal_x, goal_y, wait=0)
    print(min_0)
    cache_line = {}
    global_min = math.inf
    min_1 = create_states(min_0, goal_x, goal_y, 1, 0,   wait=0)
    print(min_1)
    cache_line = {}
    global_min = math.inf
    min_2 = create_states(min_1, 1, 0, goal_x, goal_y, wait=0)
    print(min_2)

def main():
    _cout()
    calculate_grids()
    solution()


if __name__ == '__main__':
    main()
