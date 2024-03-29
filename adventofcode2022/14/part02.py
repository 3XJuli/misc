import math
from pprint import pprint

data = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample1'


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]


min_x = 500
min_y = 0
max_y = max_x = -1

start_s = [500, 0]

n = m = 1

global grid


def parse():
    global data
    for ix, line in enumerate(data):
        line = line.split(' -> ')
        line = [[int(i) for i in coord.split(',')] for coord in line]
        data[ix] = line

    global min_y, max_y, min_x, max_x
    global n, m
    for line in data:
        for coord in line:
            min_y = min(coord[1], min_y)
            max_y = max(coord[1], max_y)
            min_x = min(coord[0], min_x)
            max_x = max(coord[0], max_x)
    m = max_y - min_y + 1 + 2
    n = (m-1) * 2 + 1
    global grid
    grid = [n * [0] for i in range(m)]

    global start_s
    shift = (n - 1) // 2 - (start_s[0] - min_x)
    for ix, col in enumerate(grid[-1]):
        grid[-1][ix] = 1
    for line in data:
        last_coord: list = list()
        for coord in line:
            grid[coord[1] - min_y][coord[0] - min_x + shift] = 1
            if last_coord:
                minxx = min(last_coord[0], coord[0])
                maxxx = max(last_coord[0], coord[0])
                minyy = min(last_coord[1], coord[1])
                maxyy = max(last_coord[1], coord[1])
                for x in range(minxx, maxxx + 1):
                    for y in range(minyy, maxyy + 1):
                        grid[y - min_y][x - min_x +  shift] = 1
            last_coord = coord
    start_s[0] = start_s[0] - min_x + shift
    start_s[1] = start_s[1] - min_y
    grid[start_s[1]][start_s[0]] = 2


def fall(pos: list, depth=0):
    global grid
    x = pos[0]
    y = pos[1]

    try:
        if not grid[y + 1][x]:
            return fall([x, y + 1], depth=1)
        elif not grid[y + 1][x - 1]:
            return fall([x - 1, y + 1], depth=1)
        elif not grid[y + 1][x + 1]:
            return fall([x + 1, y + 1], depth=1)
        else:
            if depth==0 and pos == start_s:
                return False
            grid[y][x] = 2
            return True
    except IndexError:
        return False


def drop_sand():
    return fall(start_s)


def solution():
    total = 1
    while fall(start_s):
        total += 1
    plot()
    print(total)


def plot():
    global grid
    print('#' * 10)
    for row in grid:
        line = ''
        for col in row:
            if col == 2:
                line += 'o'
            elif col:
                line += '#'
            else:
                line += '.'
        print(line)


def main():
    read_data()
    parse()
    solution()


if __name__ == '__main__':
    main()
